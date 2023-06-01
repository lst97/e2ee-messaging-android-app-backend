import json
from flask import Blueprint, jsonify, request
from api.helpers.database_helper import DbHelper
from api.helpers.response_helper import ResponseHelper, StatusCode, StatusMessage
from utils.hash import Hash
import base64
from api.models.user import User
from PIL import Image
import io
    

user_controller = Blueprint('user_controller', __name__)

engine = DbHelper.Engine()
session = DbHelper.Session()

def is_valid_image(image_bytes):
    try:
        # Open the image using PIL
        image = Image.open(io.BytesIO(image_bytes))
        # Check if the image can be loaded and has a valid format
        return True
    except (OSError, IOError):
        return False

@user_controller.route('/users', methods=['GET', 'POST'])
def get_all_users():
    if request.method == 'GET':
        users = session.query(User).all()

        user_list = []
        for user in users:
            user_dict = user.__dict__
            user_dict.pop('_sa_instance_state', None)
            user_list.append(user_dict)

        return jsonify(ResponseHelper(StatusCode.OK, StatusMessage.OK, user_list).to_dict()), 200
    
    # create user
    elif request.method == 'POST':
        request_json = request.json
        data = json.loads(request_json['data'])
        metadata = json.loads(request_json['metadata'])
        image_base64 = data['picture']
        if image_base64 == "":
            image_bytes = None
        else:
            image_bytes = base64.b64decode(image_base64)
            if not is_valid_image(image_bytes):
                return jsonify(ResponseHelper(StatusCode.BAD_REQUEST, StatusMessage.BAD_REQUEST, "Invalid image").to_dict()), 400

        user = User(
            uuid=data['uuid'],
            hash=Hash.hash_string(data['uuid']),
            name=data['name'],
            picture=image_bytes,
            ip_address=request.remote_addr,
            key_pair=data['public_key'],
            registered_id=data['registered_id']
        )

        session.add(user)
        session.commit()

        user_dict = user.__dict__
        user_dict.pop('_sa_instance_state', None)

        return jsonify(ResponseHelper(StatusCode.OK, StatusMessage.OK, user_dict).to_dict()), 200

@user_controller.route('/users/<string:user_uuid>', methods=['GET'])
def get_user_id(user_uuid):
    user = session.query(User).filter_by(uuid=user_uuid).first()

    user_dict = user.__dict__
    user_dict.pop('_sa_instance_state', None)

    return jsonify(ResponseHelper(StatusCode.OK, StatusMessage.OK, user_dict).to_dict()), 200


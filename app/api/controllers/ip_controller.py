from flask import Blueprint, request, jsonify
from api.helpers.response_helper import ResponseHelper, StatusCode, StatusMessage

ip_controller = Blueprint('ip_controller', __name__)

@ip_controller.route('/ip/client', methods=['GET'])
def get_client_ip():
    client_ip = request.remote_addr
    return jsonify(ResponseHelper(StatusCode.OK, StatusMessage.OK, client_ip).to_dict()), 200
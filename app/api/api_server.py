from flask import Flask, jsonify
from utils.logger import Logger
from api.controllers.user_controller import user_controller
from api.controllers.ip_controller import ip_controller
from dotenv import load_dotenv
from api.helpers.response_helper import ResponseHelper, StatusCode, StatusMessage
import os

logger = Logger(__name__)

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs/.env'))

API_PREFIX = os.getenv('API_PREFIX')

SSL_CONTEXT = (os.path.join(os.path.dirname(os.path.dirname(__file__)), 'certs/api/cert.pem'), os.path.join(os.path.dirname(os.path.dirname(__file__)), 'certs/api/key.pem'))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret key'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32 MB


app.register_blueprint(user_controller, url_prefix=API_PREFIX)
app.register_blueprint(ip_controller, url_prefix=API_PREFIX)

@app.route('/')
def test():
    return jsonify(ResponseHelper(StatusCode.OK, StatusMessage.OK, "PASS!").to_dict()), 200
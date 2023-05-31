from flask import Flask
from utils.logger import Logger
from .controllers.user_controller import user_controller
from dotenv import load_dotenv
import os

logger = Logger(__name__)

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs/.env'))

API_PREFIX = os.getenv('API_PREFIX')
app = Flask(__name__)
app.register_blueprint(user_controller, prefix=API_PREFIX)

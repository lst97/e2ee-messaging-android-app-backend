from flask import Flask
from utils.logger import Logger
from app.api.controllers.user_controller import user_controller
from dotenv import load_dotenv
import os

logger = Logger(__name__)

load_dotenv()


app = Flask(__name__)
app.register_blueprint(user_controller)


if __name__ == '__main__':
    logger.info('Starting app...')
    app.run()
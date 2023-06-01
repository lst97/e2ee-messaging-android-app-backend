from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
from utils.logger import Logger

import dotenv
import os

logger = Logger(__name__)
# dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), 'configs/.env'))

# db_username = os.getenv('DB_USERNAME')
# db_password = os.getenv('DB_PASSWORD')
# db_host = os.getenv('DB_HOST')
# db_port = os.getenv('DB_PORT')
# db_name = os.getenv('DB_NAME')
# db_type = os.getenv('DB_TYPE')

# load_dotenv()

DB_TYPE='postgresql'
DB_HOST='0.0.0.0'
DB_PORT=5432
DB_NAME='e2ee'

DB_USERNAME='postgres'
DB_PASSWORD='postgres'


class DatabaseHelper:
    def __init__(self, connection_str):
        self.connection_str = connection_str
        self.on_create()

    def on_create(self):
        self.engine = create_engine(self.connection_str)
        
        self.base = declarative_base()
        logger.info('Database connection success')

    def Session(self):
        return sessionmaker(bind=self.engine)
    
    def Base(self):
        return self.base
    
    def Engine(self):
        return self.engine
    
DbHelper = DatabaseHelper(f"{DB_TYPE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
from utils.logger import Logger

logger = Logger(__name__)

import os

db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_type = os.getenv('DB_TYPE')

# load_dotenv()

class DatabaseHelper:
    def __init__(self, connection_str):
        self.connection_str = connection_str
        self.on_create()

    def _check_connection(self, engine):
        try:
            engine.execute('SELECT 1')
            return True
        except OperationalError as e:
            logger.error(f'Error connecting to the database: {e}')
            return False

    def on_create(self):
        self.engine = create_engine(self.connection_str)
        if not self._check_connection(self.engine):
            return
        
        self.base = declarative_base()
        logger.info('Database connection success')

    def Session(self):
        return sessionmaker(bind=self.engine)
    
    def Base(self):
        return self.base
    
    def Engine(self):
        return self.engine
    
DbHelper = DatabaseHelper(f"{db_type}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")
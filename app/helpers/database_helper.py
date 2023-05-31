from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DatabaseHelper:
    def __init__(self, connection_str):
        self.connection_str = connection_str
        self.on_create()

    def on_create(self):
        self.engine = create_engine(self.connection_str)
        self.base = declarative_base()

    def Session(self):
        return sessionmaker(bind=self.engine)
    
    def Base(self):
        return self.base
    
    def Engine(self):
        return self.engine
    
DbHelper = DatabaseHelper('sqlite:///database.db')
from ..helpers.database_helper import DbHelper
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = DbHelper.Base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create tables in the database
Base.metadata.create_all(DbHelper.Engine())
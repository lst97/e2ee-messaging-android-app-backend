from helpers.database_helper import DbHelper
from sqlalchemy import Column, Integer, String, LargeBinary

Base = DbHelper.Base()

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True, nullable=False)
    

# Create tables in the database
Base.metadata.create_all(DbHelper.Engine())
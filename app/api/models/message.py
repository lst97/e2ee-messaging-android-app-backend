from helpers.database_helper import DbHelper
from sqlalchemy import Column, Integer, String, LargeBinary

Base = DbHelper.Base()

# undelivered messages
class User(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    sender = Column(String, unique=True, nullable=False) # sender hash
    receiver = Column(String, unique=True, nullable=False) # receiver hash
    message = Column(String, nullable=False)


# Create tables in the database
Base.metadata.create_all(DbHelper.Engine())
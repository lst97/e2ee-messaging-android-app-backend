from api.helpers.database_helper import DbHelper
from sqlalchemy import Column, Integer, String, LargeBinary

Base = DbHelper.Base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True, nullable=False)
    hash = Column(String, unique=True, nullable=False)
    name = Column(String)
    picture = Column(LargeBinary)
    ip_address = Column(String, nullable=False)
    key_pair = Column(String, nullable=False)
    registered_id = Column(String, nullable=False)

# Create tables in the database
Base.metadata.create_all(DbHelper.Engine())
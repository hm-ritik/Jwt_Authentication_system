from app.core.database import Base 
from sqlalchemy import Column , Integer , String 

class User(Base):
    __tablename__="users"
    id=Column(Integer , primary_key=True , autoincrement=True)
    username=Column(String , unique=True , nullable=False)
    email=Column(String , unique=True , nullable=False)
    password=Column(String , nullable=False)
    
from sqlalchemy import Column , Integer , String 
from app.core.database import Base 


class user(Base):
    __tablename__='user'
    id=Column(Integer , primary_key=False)
    name=Column(String , unique=True ,nullable=False)
    email=Column(String , unique=True , nullable=False)
    password=Column(String , nullable=False)


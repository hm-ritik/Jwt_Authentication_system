from pydantic import BaseModel ,EmailStr, Field


class Signup(BaseModel):
    name=str=Field(...,min_length=3,max_length=15)
    email=EmailStr
    password=str

class Login(BaseModel): 
    name=str
    password=str 

class ResponseModel(BaseModel):
    id=int
    name:str
    email:EmailStr
    class config:
        orm_mode=True      
from pydantic import BaseModel


class RegisterUser(BaseModel):
    username:str
    email:str
    password:str

class Login(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    id:int
    username:str
    email:str

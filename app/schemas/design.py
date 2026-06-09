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
    role:str
    email:str

class Update(BaseModel): 
    username:str
    email:str      

class Token(BaseModel):
    access_token: str
    token_type: str
    model_config = {"from_attributes": True}    

 

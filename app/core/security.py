from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")

ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRY_MINUTES=30


pwd_context=CryptContext(schemes=["bcrypt"] , deprecated="auto")


def hash_password(password:str):
    password_hashed=pwd_context.hash(password)
    return password_hashed

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)

    to_encode.update(
        {"exp":expire}
    )

    encoded_token=jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)
    return encoded_token

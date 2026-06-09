from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.core.database import get_db
import os
from dotenv import load_dotenv
load_dotenv()
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends , HTTPException 
from app.models.user_table import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

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

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    payload = jwt.decode( token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")
    user = db.query(User).filter(User.username == username).first()
    return user 

def require_admin(current_user=Depends(get_current_user)):
    if current_user.role !='Admin':
        raise HTTPException(status_code=403 , detail="Admin Access Required")
    return current_user



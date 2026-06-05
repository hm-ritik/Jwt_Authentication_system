from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
from fastapi import Depends
from sqlalchemy.orm import Session
from jose import jwt

from app.core.database import get_db
from app.models.user_table import User
from app.core.security import (
    SECRET_KEY,
    ALGORITHM
)
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    payload = jwt.decode( token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")
    user = db.query(User).filter(User.username == username).first()
    return user
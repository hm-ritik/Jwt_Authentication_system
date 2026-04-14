from sqlalchemy.orm import Session 
from app.schemas.design import Signup , Login , ResponseModel
from app.models.users import user


def signup_user(db:Session , data=Signup):
    hashed_password = hash_password(data.password)
    user=Signup(
        name=data.name,
        email=data.email,
        password=hashed_password
    )
    db.add(user)
    db.refresh(user)
    db.commit()
    return user

def login_user(db:Session , email:str):
    db.query(user).filter(user.email==email).first()


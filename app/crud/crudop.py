from app.schemas.design import RegisterUser , UserResponse , Login
from sqlalchemy.orm import Session
from app.models.user_table import User
from app.core.security import verify_password , hash_password , create_access_token



def register(post:RegisterUser , db:Session):
    existing_user=db.query(User).filter(post.username==User.username).first()
    if existing_user:
        return None
    paswrd=hash_password(post.password)
    new_user=User(
        username=post.username,
        email=post.email,
        password=paswrd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def readuser(id:int , db:Session):
    find_user=db.query(User).filter(id==User.id).first()
    if not find_user:
        return None
    return find_user

def loginuser(data:Login , db: Session):
    userdata=db.query(User).filter(data.username==User.username).first()

    if not userdata:
        return None
    
    if not verify_password(
        data.password,
        userdata.password
    ):
     return None
    token=create_access_token({"sub": userdata.username})
    return token
    
    



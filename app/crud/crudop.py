from app.schemas.design import RegisterUser , UserResponse , Login
from sqlalchemy.orm import Session
from app.models.user_table import User
from app.core.security import verify_password , hash_password



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
    db.close()
    return new_user

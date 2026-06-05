from fastapi import APIRouter , HTTPException , Depends
from app.schemas.design import UserResponse , RegisterUser , Login
from app.core.database import get_db
from sqlalchemy.orm import Session 
from app.crud.crudop import register , readuser ,loginuser
from app.api.auth import get_current_user




router=APIRouter()

@router.post("/registeruser", response_model=UserResponse)
def registeruser(post:RegisterUser , db:Session=Depends(get_db)):
    user=register(post , db)
    if user is None :
        raise HTTPException(status_code=404 , detail="User Already Exists")
    return user

@router.get("/readuser/{id}",response_model=UserResponse)
def showuser(id:int , db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    user=readuser(id , db)
    if user is None:
        raise HTTPException(status_code=404 , detail="user do not exists")
    return user

@router.post("/login/")
def userlogin(post:Login , db:Session=Depends(get_db)):
    user=loginuser(post , db)

    if user is None:
        raise HTTPException(status_code=404 , detail="Invalid Username or Password")
    return user


 



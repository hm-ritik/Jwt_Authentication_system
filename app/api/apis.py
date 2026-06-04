from fastapi import APIRouter , HTTPException , Depends
from app.schemas.design import UserResponse , RegisterUser
from core.database import get_db
from sqlalchemy.orm import Session 
from app.crud.crudop import register



router=APIRouter()

@router.post("/registeruser", response_model=UserResponse)
def registeruser(post:RegisterUser , db:Session=Depends(get_db)):
    user=register(post , db)
    if user is None :
        raise HTTPException(status_code=401 , detail="User Already Exists")
    return user
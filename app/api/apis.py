from fastapi import APIRouter , HTTPException , Depends
from app.schemas.design import UserResponse , RegisterUser , Login , Update
from app.core.database import get_db
from sqlalchemy.orm import Session 
from app.crud.crudop import register , readuser ,loginuser, showusers,removeuser,updateinfo
from app.core.security import get_current_user , require_admin


router=APIRouter()

@router.post("/registeruser", response_model=UserResponse)
def registeruser(post:RegisterUser , db:Session=Depends(get_db)):
    user=register(post , db)
    if user is None :
        raise HTTPException(status_code=404 , detail="User Already Exists")
    return user

@router.get("/getalluser")
def getallusers(db:Session=Depends(get_db) , admin=Depends(require_admin)):
    return showusers(db)


@router.post("/login/")
def userlogin(post:Login , db:Session=Depends(get_db)):
    user=loginuser(post , db)

    if user is None:
        raise HTTPException(status_code=404 , detail="Invalid Username or Password")
    return user

@router.get("/readuser/{id}",response_model=UserResponse)
def showuser(id:int , db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    if current_user.id !=id and current_user.role!='Admin':
        raise HTTPException(status_code=401, detail="Access Denied")
    user=readuser(id , db)
    if user is None:
        raise HTTPException(status_code=404 , detail="user do not exists")
    return user

@router.delete("/removeuser")
def deleteuser(id:int , db:Session=Depends(get_db) , current_user=Depends(require_admin)):
    user=removeuser(id,db)

    if user is None:
        raise HTTPException(status_code=404 , detail="User Not Found")
    return {
       "Message":" User deleted Successfully"
   }

@router.put("/updateuser/{id}")
def updateuser(id:int , post:Update ,db:Session=Depends(get_db) , current_user=Depends(get_current_user)):
    if current_user.id !=id and current_user.role !='Admin':
        raise HTTPException(status_code=403, detail="Access Denied")
    user=updateinfo(id ,post, db)
    if user is None:
        raise HTTPException(status_code=404 , detail="User Not exists")
    return user







 



from fastapi import FastAPI 
from app.models.users import users
from app.core.database import base , engine




app=FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def health():
    return {
        "message": "Apis are working "
    }
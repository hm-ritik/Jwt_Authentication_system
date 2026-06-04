from fastapi import FastAPI 
from app.api import apis
from app.core.database import Base,engine


app=FastAPI()

app.include_router(apis.router)

@app.get("/")
def check():
    return{
        "Message":"Testing Apis are working"
    }
Base.metadata.create_all(bind=engine)
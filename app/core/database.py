from sqlalchemy.orm import sessionmaker , declarative_base
from sqlalchemy import create_engine
import os 
from dotenv import load_dotenv

load_dotenv()

database=os.getenv("DATABASE_URL")
#print(database)

engine=create_engine(database , connect_args={"check_same_thread": False})
Base=declarative_base()
SessionLocal=sessionmaker(bind=engine , autocommit=False , autoflush=False)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()    

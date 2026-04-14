from sqlalchemy.orm import Session , declarative_base
from sqlalchemy import create_engine
from dotenv import getenv


engine=create_engine(Data)
SessionLocal=Session()
Base=declarative_base()
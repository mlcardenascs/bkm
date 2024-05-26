from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('dbUser')
dbName = os.getenv('dbName')
pwd = os.getenv('dbPwd')
host = os.getenv('dbHost')
port = os.getenv('dbPort')

DB_URL = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(user, pwd, host, port, dbName)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://ktym57cel7olx1jj:bv8tkko2kdmnpiw6@ebh2y8tqym512wqs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/naahstp8zt2ps63g"

db_engine = create_engine(DATABASE_URL)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

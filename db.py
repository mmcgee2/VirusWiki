from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://pn2qeknluf2bh2xb:lkaqjwxjaazho23z@n4m3x5ti89xl6czh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/ll43lin6tfexl1ha"

db_engine = create_engine(DATABASE_URL, pool_pre_ping=True)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

# mysql://mmcgee:QAZwsx!23$@localhost/virus
# mysql://pn2qeknluf2bh2xb:lkaqjwxjaazho23z@n4m3x5ti89xl6czh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/ll43lin6tfexl1ha

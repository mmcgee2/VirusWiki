from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://n5az6cwzmic0a8gu:mmzlol2qy6k0dc1v@n4m3x5ti89xl6czh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dtc39cq7y0wbis8o"

db_engine = create_engine(DATABASE_URL)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

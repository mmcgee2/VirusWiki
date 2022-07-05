from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://mmcgee:QAZwsx!23$@localhost/author"

db_engine = create_engine(DATABASE_URL)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

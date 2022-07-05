from db import Base
from sqlalchemy import Column, TEXT, VARCHAR, Integer

# still noob but thinking one-one relationship so keeping in same table
class Virus(Base):
    __tablename__ = "sarscov2"

    id = Column(Integer, primary_key=True, index=True)
    variant = Column(VARCHAR(255), index=True)
    changes = Column(VARCHAR(255), unique=True, index=True)
    description = Column(TEXT, unique=True)

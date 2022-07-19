from enum import unique
from db import Base
from sqlalchemy import Column, TEXT, VARCHAR, Integer

# still noob but thinking one-one relationship so keeping in same table
class Virus(Base):
    __tablename__ = "sarscov2"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    variant = Column(VARCHAR(255), index=True)
    changes = Column(VARCHAR(255), index=True)
    description = Column(TEXT)
    description2 = Column(TEXT)


class Overview(Base):
    __tablename__ = "overview"

    id = Column(VARCHAR(255), primary_key=True, index=True, unique=True)
    works_cited = Column(TEXT)
    purpose = Column(TEXT)

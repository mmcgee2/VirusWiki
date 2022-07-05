from db import Base
from sqlalchemy import Column, TEXT, VARCHAR, ForeignKey, Integer

# still noob but thinking one-one relationship so keeping in same table
class Virus(Base):
    __tablename__ = "sarscov2"

    id = Column(Integer, primary_key=True, index=True)
    Variant = Column(VARCHAR, index=True)
    Changes = Column(VARCHAR, unique=True, index=True)
    Description = Column(TEXT, unique=True)

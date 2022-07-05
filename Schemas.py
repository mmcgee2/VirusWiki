from pydantic import BaseModel

# from .Model import User


class virus_base(BaseModel):
    Changes: str
    Description: str


class variant_create(virus_base):
    Variant: str


class virus(virus_base):
    id: int

    class Config:
        orm_mode = True

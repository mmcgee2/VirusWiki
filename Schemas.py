from pydantic import BaseModel

# from .Model import User


class user_base(BaseModel):
    Change: str
    Description: str


class variant_create(user_base):
    name: str


class virus(user_base):
    Variant: str
    ID: int

    class Config:
        orm_mode = True

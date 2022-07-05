from pydantic import BaseModel

# from .Model import User


class user_base(BaseModel):
    Changes: str
    Description: str


class variant_create(user_base):
    name: str


class virus(user_base):
    Variant: str
    id: int

    class Config:
        orm_mode = True

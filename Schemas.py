from pydantic import BaseModel

# from .Model import User


class virus_base(BaseModel):
    Changes: str
    Description: str


class variant_create(BaseModel):
    Variant: str


class virus(variant_create):
    id: int

    class Config:
        orm_mode = True

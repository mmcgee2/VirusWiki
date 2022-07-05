from pydantic import BaseModel

# from .Model import User


class variant_create(BaseModel):
    Variant: str


class virus_base(variant_create):
    Changes: str
    Description: str


class virus(variant_create):
    id: int

    class Config:
        orm_mode = True

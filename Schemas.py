from pydantic import BaseModel

# from .Model import User


class variant_create(BaseModel):
    variant: str


class virus_base(variant_create):
    changes: str
    description: str


class virus(variant_create):
    id: int

    class Config:
        orm_mode = True

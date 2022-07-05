from pydantic import BaseModel

# from .Model import User


class virus_base(BaseModel):
    changes: str
    description: str


class variant_create(virus_base):
    variant: str


class virus(virus_base):
    id: int

    class Config:
        orm_mode = True

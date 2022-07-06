from pydantic import BaseModel


class create_variant(BaseModel):
    id: int
    variant: str
    changes: str
    description: str

    class Config:
        orm_mode = True


class collection(create_variant):
    items: list[create_variant] = []

    class Config:
        orm_mode = True


"""
class virus_base(BaseModel):
    changes: str
    description: str


class variant_create(virus_base):
    variant: str


class virus(virus_base):
    id: int

    class Config:
        orm_mode = True
"""

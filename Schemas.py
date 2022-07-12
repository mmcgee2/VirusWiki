from pydantic import BaseModel


class create_variant(BaseModel):
    id: int
    variant: str
    changes: str
    description: str
    description2: str


class collection(create_variant):
    items: list[create_variant] = []

    class Config:
        orm_mode = True


class articles(BaseModel):
    id: int
    summary: str
    purpose: str

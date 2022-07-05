from pydantic import BaseModel


class virus_base(BaseModel):
    changes: str
    description: str


class variant_create(virus_base):
    variant: str


class virus(virus_base):
    id: int

    class Config:
        orm_mode = True

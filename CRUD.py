from requests import session
from sqlalchemy.orm import Session
import Model, Schemas


def get_id(db: Session, id: int):
    return db.query(Model.Virus).filter(Model.Virus.ID == id).first()


def get_variant(db: Session, name: str):
    return db.query(Model.Virus).filter(Model.Virus.Variant == name).first()


def get_changes(db: Session, changes: str):
    return db.query(Model.Virus).filter(Model.Virus.Changes == changes).first()


def get_description(db: Session, description: str):
    return db.query(Model.Virus).filter(Model.Virus.Description == description).first()


def get_variants(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Model.Virus).offset(skip).limit(limit).all()


def create_variant(db: Session, virus: Schemas.variant_create):
    variant_name = virus.name
    db_virus = Model.Virus(
        variant=virus.name, changes=virus.changes, description=virus.description
    )

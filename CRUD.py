from sqlalchemy.orm import Session
import Model, Schemas


def get_id(db: Session, id: int):
    return db.query(Model.Virus).filter(Model.Virus.id == id).first()


def get_variant(db: Session, Variant: str):
    return db.query(Model.Virus).filter(Model.Virus.Variant == Variant).first()


def get_changes(db: Session, Changes: str):
    return db.query(Model.Virus).filter(Model.Virus.Changes == Changes).first()


def get_description(db: Session, Description: str):
    return db.query(Model.Virus).filter(Model.Virus.Description == Description).first()


def get_variants(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Model.Virus).offset(skip).limit(limit).all()


def create_variant(db: Session, virus: Schemas.variant_create):
    db_virus = Model.Virus(
        Variant=virus.name, Changes=virus.Changes, Description=virus.Description
    )
    db.add(db_virus)
    db.commit()
    db.refresh(db_virus)
    return db_virus

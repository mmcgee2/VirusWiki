from sqlalchemy.orm import Session
import Model, Schemas


def get_id(db: Session, id: int):
    return db.query(Model.Virus).filter(Model.Virus.id == id).first()


def get_variant(db: Session, variant: str):
    return db.query(Model.Virus).filter(Model.Virus.variant == variant).first()


def get_changes(db: Session, changes: str):
    return db.query(Model.Virus).filter(Model.Virus.changes == changes).first()


def get_description(db: Session, description: str):
    return db.query(Model.Virus).filter(Model.Virus.description == description).first()


def get_variants(db: Session, skip: int = 1, limit: int = 10):
    return db.query(Model.Virus).offset(skip).limit(limit).all()


def create_variant(db: Session, virus: Schemas.create_variant):
    db_virus = Model.Virus(
        changes=virus.changes,
        description=virus.description,
        variant=virus.variant,
    )
    db.add(db_virus)
    db.commit()
    db.refresh(db_virus)
    return db_virus

from fastapi import Depends, FastAPI, HTTPException, Body
from sqlalchemy.orm import Session
import CRUD, Model, Schemas
from db import local_session, db_engine
from fastapi.middleware.cors import CORSMiddleware

Model.Base.metadata.create_all(bind=db_engine)

app = FastAPI()

origins = [
    "https://desolate-sea-33600.herokuapp.com:3306",
    "https://desolate-sea-33600.herokuapp.com/virus",
    "https://viruswiki.pages.dev/Covid",
    "http://viruswiki.pages.dev/",
    "https://localhost:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# dependency
def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()


@app.post("/virus/", response_model=Schemas.create_variant)
def create_variants(
    virus: Schemas.create_variant = Body(default=None, embed=True),
    db: Session = Depends(get_db),
):
    result = {"virus": virus}
    db_virus = (
        CRUD.get_variant(db, variant=virus.variant),
        CRUD.get_changes(db, changes=virus.changes),
        CRUD.get_description(db, description=virus.description),
        CRUD.get_description2(db, description2=virus.description2),
    )
    if not db_virus:
        raise HTTPException(status_code=400, detail="Variant already in use")
    return result, CRUD.create_variant(db=db, virus=virus)


@app.get("/virus/", response_model=list[Schemas.collection])
def read_variants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    variants = CRUD.get_variants(db, skip=skip, limit=limit)
    return variants


@app.get("/virus/{id}", response_model=Schemas.create_variant)
def read_variant(id: int, db: Session = Depends(get_db)):
    db_virus = CRUD.get_id(db, id=id)
    if db_virus is None:
        raise HTTPException(status_code=404, detail="Variant not found")
    return db_virus


@app.put("/virus/{id}", response_model=Schemas.create_variant)
def update_variant(
    id: int,
    virus: Schemas.create_variant = Body(default=None, embed=True),
    db: Session = Depends(get_db),
):
    db_virus = CRUD.get_id(db, id=id)
    if db_virus is None:
        raise HTTPException(status_code=404, detail="Variant not found")
    return db_virus, CRUD.update_variant(db=db, id=id, virus=virus)


@app.delete("/virus/{id}")
def delete_variant(id: int, db: Session = Depends(get_db)):
    db_virus = CRUD.get_id(db, id=id)
    if db_virus is None:
        raise HTTPException(status_code=404, detail="Variant not found")
    return CRUD.delete_variant(db=db, id=id)


@app.post("/overview/", response_model=Schemas.articles)
def review(review: Schemas.articles, db: Session = Depends(get_db)):
    db_review = (
        CRUD.get_works_cited(db, works_cited=review.works_cited),
        CRUD.get_purpose(db, purpose=review.purpose),
    )
    if not db_review:
        raise HTTPException(status_code=400, detail="Already posted")
    return CRUD.article(db=db, review=review)


@app.get("/overview/", response_model=list[Schemas.collections])
def read_overview(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    overview = CRUD.get_overview(db, skip=skip, limit=limit)
    return overview

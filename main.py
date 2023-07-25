from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from fastapi.openapi.docs import get_redoc_html

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CV-API",
    description="Eine API für den Lebenslauf",
    version="1.0.0",
    redoc_url=None,
    docs_url="/", 
)
persondaten_router = APIRouter(default=JSONResponse)
ausbildung_router = APIRouter(default=JSONResponse)
beruferfahrungen_router = APIRouter(default=JSONResponse)
programmiererfahrungen_router = APIRouter(default=JSONResponse)
projekte_router=APIRouter(default=JSONResponse)
sprachen_router = APIRouter(default=JSONResponse)
stipendien_router = APIRouter(default=JSONResponse)
hobbys_router = APIRouter(default=JSONResponse)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="CV-API-Dokumentation"
    )
# Post
@persondaten_router.post("/", response_model=schemas.Persondaten)
def add_persondaten(persondaten: schemas.Persondaten, db:Session=Depends(get_db)):
    if crud.persondaten_exists(db):
        raise HTTPException(status_code=409, detail="Persondaten bereits vorhanden")
    return crud.add_persondaten(db,persondaten)

@ausbildung_router.post("/", response_model=schemas.Ausbildung)
def add_ausbildung(ausbildung: schemas.Ausbildung, db:Session=Depends(get_db)):
    if crud.ausbildung_exists(db, ausbildung):
        raise HTTPException(status_code=409, detail="Ausbildung bereits vorhanden")
    return crud.add_ausbildung(db,ausbildung)

@beruferfahrungen_router.post("/", response_model=schemas.Beruferfahrungen)
def add_beruferfahrung(beruferfahrung: schemas.Beruferfahrungen, db:Session=Depends(get_db)):
    if crud.beruferfahrung_exists(db, beruferfahrung):
        raise HTTPException(status_code=409, detail="Beruferfahrung bereits vorhanden")
    return crud.add_beruferfahrung(db,beruferfahrung)

@programmiererfahrungen_router.post("/",response_model=schemas.Programmiererfahrungen)
def add_programmiererfahrung(programmiererfahrung:schemas.Programmiererfahrungen,db:Session=Depends(get_db)):
    if crud.programmiererfahrung_exists(db, programmiererfahrung):
        raise HTTPException(status_code=409, detail="Programmiererfahrung bereits vorhanden")
    return crud.add_programmiererfahrung(db,programmiererfahrung)

@projekte_router.post("/",response_model=schemas.Projekte)
def add_projekt(projekt:schemas.Projekte,db:Session=Depends(get_db)):
    if crud.projekt_exists(db, projekt):
        raise HTTPException(status_code=409, detail="Projekt bereits vorhanden")
    return crud.add_projekt(db,projekt)

@sprachen_router.post("/",response_model=schemas.Sprachen)
def add_sprache(sprache:schemas.Sprachen,db:Session=Depends(get_db)):
    if crud.sprache_exists(db, sprache):
        raise HTTPException(status_code=409, detail="Sprache bereits vorhanden")
    return crud.add_sprache(db,sprache)

@stipendien_router.post("/",response_model=schemas.Stipendien)
def add_stipendium(stipendium:schemas.Stipendien,db:Session=Depends(get_db)):
    if crud.stipendium_exists(db, stipendium):
        raise HTTPException(status_code=409, detail="Stipendium bereits vorhanden")
    return crud.add_stipendium(db,stipendium)

@hobbys_router.post("/",response_model=schemas.Hobbys)
def add_hobby(hobby:schemas.Hobbys,db:Session=Depends(get_db)):
    if crud.hobby_exists(db, hobby):
        raise HTTPException(status_code=409, detail="Hobby bereits vorhanden")
    return crud.add_hobby(db,hobby)

# Put 
@persondaten_router.put("/", response_model=schemas.Persondaten)
def update_persondaten(persondaten: schemas.Persondaten, db: Session = Depends(get_db)):
    return crud.update_persondaten(db, persondaten)

@ausbildung_router.put("/{ausbildung_id}", response_model=schemas.Ausbildung)
def update_ausbildung(ausbildung_id: int, ausbildung: schemas.Ausbildung, db: Session = Depends(get_db)):
    return crud.update_ausbildung(db, ausbildung_id, ausbildung)

@beruferfahrungen_router.put("/{beruferfahrung_id}", response_model=schemas.Beruferfahrungen)
def update_beruferfahrung(beruferfahrung_id: int, beruferfahrung: schemas.Beruferfahrungen, db: Session = Depends(get_db)):
    return crud.update_beruferfahrung(db, beruferfahrung_id, beruferfahrung)

@programmiererfahrungen_router.put("/{programmiererfahrung_id}", response_model=schemas.Programmiererfahrungen)
def update_programmiererfahrung(programmiererfahrung_id: int, programmiererfahrung: schemas.Programmiererfahrungen, db: Session = Depends(get_db)):
    return crud.update_programmiererfahrung(db, programmiererfahrung_id, programmiererfahrung)

@projekte_router.put("/{projekt_id}", response_model=schemas.Projekte)
def update_projekt(projekt_id: int, projekt: schemas.Projekte, db: Session = Depends(get_db)):
    return crud.update_projekt(db, projekt_id, projekt)

@sprachen_router.put("/{sprache_id}", response_model=schemas.Sprachen)
def update_sprache(sprache_id: int, sprache: schemas.Sprachen, db: Session = Depends(get_db)):
    return crud.update_sprache(db, sprache_id, sprache)

@stipendien_router.put("/{stipendium_id}", response_model=schemas.Stipendien)
def update_stipendium(stipendium_id: int, stipendium: schemas.Stipendien, db: Session = Depends(get_db)):
    return crud.update_stipendium(db, stipendium_id, stipendium)

@hobbys_router.put("/{hobby_id}", response_model=schemas.Hobbys)
def update_hobby(hobby_id: int, hobby: schemas.Hobbys, db: Session = Depends(get_db)):
    return crud.update_hobby(db, hobby_id, hobby)


# Get 
@persondaten_router.get("/", response_model=list[schemas.Persondaten])
def get_persondaten(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    persondaten = crud.get_perondaten(db,skip=skip,limit=limit)
    return persondaten

@ausbildung_router.get("/", response_model=list[schemas.Ausbildung])
def get_ausbildung(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ausbildung = crud.get_ausbildung(db,skip=skip,limit=limit)
    return ausbildung

@beruferfahrungen_router.get("/", response_model=list[schemas.Beruferfahrungen])
def get_beruferfahrungen(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    beruferfahrungen = crud.get_beruferfahrungen(db,skip=skip,limit=limit)
    return beruferfahrungen

@programmiererfahrungen_router.get("/",response_model=list[schemas.Programmiererfahrungen])
def get_programmiererfahrungen(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    programmiererfahrungen = crud.get_programmiererfahrungen(db,skip=skip,limit=limit)
    return programmiererfahrungen

@projekte_router.get("/",response_model=list[schemas.Projekte])
def get_projekte(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projekte = crud.get_projekte(db,skip=skip,limit=limit)
    return projekte

@sprachen_router.get("/",response_model=list[schemas.Sprachen])
def get_sprachen(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sprachen = crud.get_sprachen(db,skip=skip,limit=limit)
    return sprachen

@stipendien_router.get("/",response_model=list[schemas.Stipendien])
def get_stipendien(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stipendien = crud.get_stipendien(db,skip=skip,limit=limit)
    return stipendien

@hobbys_router.get("/",response_model=list[schemas.Hobbys])
def get_hobbys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hobbys = crud.get_hobbys(db,skip=skip,limit=limit)
    return hobbys

# Get Last
@ausbildung_router.get("/last", response_model=list[schemas.Ausbildung])
def get_last_ausbildung(db: Session = Depends(get_db)):
    ausbildung = crud.get_last_ausbildung(db)
    return ausbildung

@beruferfahrungen_router.get("/last", response_model=list[schemas.Beruferfahrungen])
def get_last_beruferfahrung(db: Session = Depends(get_db)):
    beruferfahrung = crud.get_last_beruferfahrung(db)
    return beruferfahrung

# Delete
@persondaten_router.delete("/")
def delete_persondaten(db: Session = Depends(get_db)):
    return crud.delete_persondaten(db)

@ausbildung_router.delete("/{ausbildung_id}")
def delete_ausbildung(ausbildung_id: int, db: Session = Depends(get_db)):
    return crud.delete_ausbildung(db, ausbildung_id)

@beruferfahrungen_router.delete("/{beruferfahrung_id}")
def delete_beruferfahrung(beruferfahrung_id: int, db: Session = Depends(get_db)):
    return crud.delete_beruferfahrung(db, beruferfahrung_id)

@programmiererfahrungen_router.delete("/{programmiererfahrung_id}")
def delete_programmiererfahrung(programmiererfahrung_id: int, db: Session = Depends(get_db)):
    return crud.delete_programmiererfahrung(db, programmiererfahrung_id)

@projekte_router.delete("/{projekt_id}")
def delete_projekt(projekt_id: int, db: Session = Depends(get_db)):
    return crud.delete_projekt(db, projekt_id)

@sprachen_router.delete("/{sprache_id}")
def delete_sprache(sprache_id: int, db: Session = Depends(get_db)):
    return crud.delete_sprache(db, sprache_id)

@stipendien_router.delete("/{stipendium_id}")
def delete_stipendium(stipendium_id: int, db: Session = Depends(get_db)):
    return crud.delete_stipendium(db, stipendium_id)

@hobbys_router.delete("/{hobby_id}")
def delete_hobby(hobby_id: int, db: Session = Depends(get_db)):
    return crud.delete_hobby(db, hobby_id)


app.include_router(persondaten_router, prefix="/persondaten", tags=["Persondaten"])
app.include_router(ausbildung_router, prefix="/ausbildung", tags=["Ausbildung"])
app.include_router(beruferfahrungen_router, prefix="/beruferfahrungen", tags=["Beruferfahrungen"])
app.include_router(programmiererfahrungen_router, prefix="/programmiererfahrungen", tags=["Programmiererfahrungen"])
app.include_router(projekte_router, prefix="/projekte", tags=["Projekte"])
app.include_router(sprachen_router, prefix="/sprachen", tags=["Sprachen"])
app.include_router(stipendien_router, prefix="/stipendien", tags=["Stipendien"])
app.include_router(hobbys_router, prefix="/hobbys", tags=["Hobbys"])


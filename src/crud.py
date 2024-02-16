from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from . import models, schemas

# get functions
def get_perondaten(db:Session, skip: int= 0, limit: int = 100):
    return db.query(models.Persondaten).offset(skip).limit(limit).all()
def get_ausbildung(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ausbildung).offset(skip).limit(limit).all()
def get_beruferfahrungen(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Beruferfahrungen).offset(skip).limit(limit).all()
def get_programmiererfahrungen(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Programmiererfahrungen).offset(skip).limit(limit).all()
def get_projekte(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Projekte).offset(skip).limit(limit).all()
def get_sprachen(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sprachen).offset(skip).limit(limit).all()
def get_stipendien(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Stipendien).offset(skip).limit(limit).all()
def get_hobbys(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hobbys).offset(skip).limit(limit).all()

# Get last
def get_last_ausbildung(db: Session):
    return [db.query(models.Ausbildung).order_by(models.Ausbildung.id.desc()).first()]
def get_last_beruferfahrung(db: Session):
    return [db.query(models.Beruferfahrungen).order_by(models.Beruferfahrungen.id.desc()).first()]

# Post 
def add_persondaten(db:Session, persondaten:schemas.Persondaten):
    db_persondaten = models.Persondaten(
        vorname = persondaten.vorname,
        nachname= persondaten.nachname,
        adresse=persondaten.adresse,
        telefonnummer=persondaten.telefonnummer,
        geburtsdatum=persondaten.geburtsdatum,
        geburtsort=persondaten.geburtsort
    )
    db.add(db_persondaten)
    db.commit()
    db.refresh(db_persondaten)
    return db_persondaten

def add_ausbildung(db:Session, ausbildung:schemas.Ausbildung):
    db_ausbildung = models.Ausbildung(
        name=ausbildung.name,
        ort=ausbildung.ort,
        abschluss=ausbildung.abschluss,
        anfang=ausbildung.anfang,
        ende=ausbildung.ende
    )
    db.add(db_ausbildung)
    db.commit()
    db.refresh(db_ausbildung)
    return db_ausbildung

def add_beruferfahrung(db: Session, beruferfahrungen: schemas.Beruferfahrungen):
    db_beruferfahrungen = models.Beruferfahrungen(
        name=beruferfahrungen.name,
        ort=beruferfahrungen.ort,
        titel=beruferfahrungen.titel,
        anfang=beruferfahrungen.anfang,
        ende=beruferfahrungen.ende,
        referenz=beruferfahrungen.referenz,
        verantwortungen=beruferfahrungen.verantwortungen
    )
    db.add(db_beruferfahrungen)
    db.commit()
    db.refresh(db_beruferfahrungen)
    return db_beruferfahrungen

def add_programmiererfahrung(db: Session, programmiererfahrungen: schemas.Programmiererfahrungen):
    db_programmiererfahrungen = models.Programmiererfahrungen(
        sprache=programmiererfahrungen.sprache,
        frameworks=programmiererfahrungen.frameworks
    )
    db.add(db_programmiererfahrungen)
    db.commit()
    db.refresh(db_programmiererfahrungen)
    return db_programmiererfahrungen


def add_projekt(db: Session, projekte: schemas.Projekte):
    db_projekte = models.Projekte(
        name=projekte.name,
        beschreibung=projekte.beschreibung
    )
    db.add(db_projekte)
    db.commit()
    db.refresh(db_projekte)
    return db_projekte


def add_sprache(db: Session, sprachen: schemas.Sprachen):
    db_sprachen = models.Sprachen(
        sprache=sprachen.sprache,
        level=sprachen.level
    )
    db.add(db_sprachen)
    db.commit()
    db.refresh(db_sprachen)
    return db_sprachen

def add_stipendium(db: Session, stipendien: schemas.Stipendien):
    db_stipendien = models.Stipendien(
        stiftung=stipendien.stiftung,
        anfang=stipendien.anfang,
        ende=stipendien.ende
    )
    db.add(db_stipendien)
    db.commit()
    db.refresh(db_stipendien)
    return db_stipendien

def add_hobby(db: Session, hobbys: schemas.Hobbys):
    db_hobbys = models.Hobbys(
        hobby=hobbys.hobby
    )
    db.add(db_hobbys)
    db.commit()
    db.refresh(db_hobbys)
    return db_hobbys

# Update
def update_persondaten(db: Session, persondaten: schemas.Persondaten):
    db_persondaten = db.query(models.Persondaten).filter(models.Persondaten.id == 1).first()
    if not db_persondaten:
        raise HTTPException(status_code=404, detail="Persondaten nicht gefunden")
        
    # Aktualisieren der Felder mit den neuen Werten
    if persondaten.vorname:
        db_persondaten.vorname = persondaten.vorname
    if persondaten.nachname:
        db_persondaten.nachname = persondaten.nachname
    if persondaten.adresse:
        db_persondaten.adresse = persondaten.adresse
    if persondaten.telefonnummer:
        db_persondaten.telefonnummer = persondaten.telefonnummer
    if persondaten.geburtsdatum:
        db_persondaten.geburtsdatum = persondaten.geburtsdatum
    if persondaten.geburtsort:
        db_persondaten.geburtsort = persondaten.geburtsort    
    db.commit()
    db.refresh(db_persondaten)
    return db_persondaten    

def update_ausbildung(db: Session, ausbildung_id: int, ausbildung: schemas.Ausbildung):
    db_ausbildung = db.query(models.Ausbildung).filter(models.Ausbildung.id == ausbildung_id).first()
    if not db_ausbildung:
        raise HTTPException(status_code=404, detail="Ausbildung nicht gefunden")
        
    # Aktualisieren der Felder mit den neuen Werten
    if ausbildung.name:
        db_ausbildung.name = ausbildung.name
    if ausbildung.ort:
        db_ausbildung.ort = ausbildung.ort
    if ausbildung.abschluss:
        db_ausbildung.abschluss = ausbildung.abschluss
    if ausbildung.anfang:
        db_ausbildung.anfang = ausbildung.anfang
    if ausbildung.ende:
        db_ausbildung.ende = ausbildung.ende
    
    db.commit()
    db.refresh(db_ausbildung)
    return db_ausbildung
def update_beruferfahrung(db: Session, beruferfahrung_id: int, beruferfahrung: schemas.Beruferfahrungen):
    db_beruferfahrung = db.query(models.Beruferfahrungen).filter(models.Beruferfahrungen.id == beruferfahrung_id).first()
    if not db_beruferfahrung:
        raise HTTPException(status_code=404, detail="Beruferfahrung nicht gefunden")
        
    # Aktualisieren der Felder mit den neuen Werten
    if beruferfahrung.name:
        db_beruferfahrung.name = beruferfahrung.name
    if beruferfahrung.ort:
        db_beruferfahrung.ort = beruferfahrung.ort
    if beruferfahrung.titel:
        db_beruferfahrung.titel = beruferfahrung.titel
    if beruferfahrung.anfang:
        db_beruferfahrung.anfang = beruferfahrung.anfang
    if beruferfahrung.ende:
        db_beruferfahrung.ende = beruferfahrung.ende
    if beruferfahrung.referenz:
        db_beruferfahrung.referenz = beruferfahrung.referenz
    if beruferfahrung.verantwortungen:
        db_beruferfahrung.verantwortungen = beruferfahrung.verantwortungen
        
    db.commit()
    db.refresh(db_beruferfahrung)
    return db_beruferfahrung

def update_programmiererfahrung(db: Session, programmiererfahrung_id: int, programmiererfahrung: schemas.Programmiererfahrungen):
    db_programmiererfahrung = db.query(models.Programmiererfahrungen).filter(models.Programmiererfahrungen.id == programmiererfahrung_id).first()
    if not db_programmiererfahrung:
        raise HTTPException(status_code=404, detail="Programmiererfahrung nicht gefunden")
        
    # Aktualisieren der Felder mit den neuen Werten
    if programmiererfahrung.sprache:
        db_programmiererfahrung.sprache = programmiererfahrung.sprache
    if programmiererfahrung.frameworks:
        db_programmiererfahrung.frameworks = programmiererfahrung.frameworks
        
    db.commit()
    db.refresh(db_programmiererfahrung)
    return db_programmiererfahrung


def update_projekt(db: Session, projekt_id: int, projekt: schemas.Projekte):
    db_projekt = db.query(models.Projekte).filter(models.Projekte.id == projekt_id).first()
    if not db_projekt:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")
        
    # Aktualisieren der Felder mit den neuen Werten
    if projekt.name:
        db_projekt.name = projekt.name
    if projekt.frameworks:
        db_projekt.beschreibung = projekt.beschreibung
        
    db.commit()
    db.refresh(db_projekt)
    return db_projekt

def update_sprache(db: Session, sprache_id: int, sprache: schemas.Sprachen):
    db_sprache = db.query(models.Programmiererfahrungen).filter(models.Sprachen.id == sprache_id).first()
    if not db_sprache:
        raise HTTPException(status_code=404, detail="Sprache nicht gefunden")
        
    # Aktualisieren der Felder mit den neuen Werten
    if sprache.sprache:
        db_sprache.sprache = sprache.sprache
    if sprache.level:
        db_sprache.level = sprache.level
        
    db.commit()
    db.refresh(db_sprache)
    return db_sprache

def update_stipendium(db: Session, stipendium_id: int, stipendium: schemas.Stipendien):
    db_stipendium = db.query(models.Programmiererfahrungen).filter(models.Stipendien.id == stipendium_id).first()
    if not db_stipendium:
        raise HTTPException(status_code=404, detail="Stipendium nicht gefunden")
        
    # Aktualisieren der Felder mit den neuen Werten
    if stipendium.stiftung:
        db_stipendium.stiftung = stipendium.stiftung
    if stipendium.anfang:
        db_stipendium.anfang = stipendium.anfang
    if stipendium.ende:
        db_stipendium.ende = stipendium.ende
                
    db.commit()
    db.refresh(db_stipendium)
    return db_stipendium

def update_hobby(db: Session, hobby_id: int, hobby: schemas.Hobbys):
    db_hobby = db.query(models.Hobbys).filter(models.Hobbys.id == hobby_id).first()
    if not db_hobby:
        raise HTTPException(status_code=404, detail="Programmiererfahrung nicht gefunden")
        
    # Aktualisieren der Felder mit den neuen Werten
    if hobby.hobby:
        db_hobby.hobby = hobby.hobby
    db.commit()
    db.refresh(db_hobby)
    return db_hobby

# Delete
def delete_persondaten(db: Session):
    persondaten = db.query(models.Persondaten).filter(
        models.Persondaten.id == 1).first()
    if not persondaten:
        raise HTTPException(
            status_code=404, detail="Persondaten nicht gefunden")

    db.delete(persondaten)
    db.commit()
    return {"message": "Persondaten gelöscht"}

def delete_ausbildung(db: Session, ausbildung_id: int):
    ausbildung = db.query(models.Ausbildung).filter(
        models.Ausbildung.id == ausbildung_id).first()
    if not ausbildung:
        raise HTTPException(
            status_code=404, detail="Ausbildung nicht gefunden")

    db.delete(ausbildung)
    db.commit()
    return {"message": "Ausbildung gelöscht"}

def delete_beruferfahrung(db: Session, beruferfahrung_id: int):
    beruferfahrung = db.query(models.Beruferfahrungen).filter(
        models.Beruferfahrungen.id == beruferfahrung_id).first()
    if not beruferfahrung:
        raise HTTPException(
            status_code=404, detail="Beruferfahrung nicht gefunden")

    db.delete(beruferfahrung)
    db.commit()
    return {"message": "Beruferfahrung gelöscht"}

def delete_programmiererfahrung(db: Session, programmiererfahrung_id: int):
    programmiererfahrung = db.query(models.Programmiererfahrungen).filter(models.Programmiererfahrungen.id == programmiererfahrung_id).first()
    if not programmiererfahrung:
        raise HTTPException(status_code=404, detail="Programmiererfahrung nicht gefunden")
    
    db.delete(programmiererfahrung)
    db.commit()
    return {"message": "Programmiererfahrung gelöscht"}

def delete_projekt(db: Session, projekt_id: int):
    projekt = db.query(models.Projekte).filter(models.Projekte.id == projekt_id).first()
    if not projekt:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")
    
    db.delete(projekt)
    db.commit()
    return {"message": "Projekt gelöscht"}

def delete_sprache(db: Session, sprache_id: int):
    sprache = db.query(models.Sprachen).filter(models.Sprachen.id == sprache_id).first()
    if not sprache:
        raise HTTPException(status_code=404, detail="Sprache nicht gefunden")
    
    db.delete(sprache)
    db.commit()
    return {"message": "Sprache gelöscht"}

def delete_stipendium(db: Session, stipendium_id: int):
    stipendium = db.query(models.Stipendien).filter(models.Stipendien.id == stipendium_id).first()
    if not stipendium:
        raise HTTPException(status_code=404, detail="Stipendium nicht gefunden")
    
    db.delete(stipendium)
    db.commit()
    return {"message": "Stipendium gelöscht"}

def delete_hobby(db: Session, hobby_id: int):
    hobby = db.query(models.Hobbys).filter(models.Hobbys.id == hobby_id).first()
    if not hobby:
        raise HTTPException(status_code=404, detail="Hobby nicht gefunden")
    
    db.delete(hobby)
    db.commit()
    return {"message": "Hobby gelöscht"}

# Fehler behandlung
def persondaten_exists(db: Session) -> bool:
    persondaten_count = db.query(func.count(models.Persondaten.id)).scalar()
    return persondaten_count > 0


def ausbildung_exists(db: Session, ausbildung: schemas.Ausbildung) -> bool:
    query = db.query(models.Ausbildung).filter(
        models.Ausbildung.name == ausbildung.name,
        models.Ausbildung.ort == ausbildung.ort
    )
    ausbildung_exists = db.query(query.exists()).scalar()
    return ausbildung_exists

def beruferfahrung_exists(db: Session, beruferfahrung: schemas.Beruferfahrungen) -> bool:
    query = db.query(models.Beruferfahrungen).filter(
        models.Beruferfahrungen.name == beruferfahrung.name,
        models.Beruferfahrungen.ort == beruferfahrung.ort
    )
    beruferfahrung_exists = db.query(query.exists()).scalar()
    return beruferfahrung_exists

def programmiererfahrung_exists(db: Session, programmiererfahrung: schemas.Programmiererfahrungen) -> bool:
    query = db.query(models.Programmiererfahrungen).filter(
        models.Programmiererfahrungen.sprache == programmiererfahrung.sprache,
    )
    programmiererfahrung_exists = db.query(query.exists()).scalar()
    return programmiererfahrung_exists

def projekt_exists(db: Session, projekt: schemas.Projekte) -> bool:
    query = db.query(models.Programmiererfahrungen).filter(
        models.Projekte.name == projekt.name
    )
    projekt_exists = db.query(query.exists()).scalar()
    return projekt_exists

def sprache_exists(db: Session, sprache: schemas.Sprachen) -> bool:
    query = db.query(models.Sprachen).filter(
        models.Sprachen.sprache == sprache.sprache
    )
    sprache_exists = db.query(query.exists()).scalar()
    return sprache_exists

def stipendium_exists(db: Session, stipendium: schemas.Stipendien) -> bool:
    query = db.query(models.Stipendien).filter(
        models.Stipendien.stiftung == stipendium.stiftung
    )
    stipendium_exists = db.query(query.exists()).scalar()
    return stipendium_exists

def hobby_exists(db: Session, hobby: schemas.Hobbys) -> bool:
    query = db.query(models.Hobbys).filter(
        models.Hobbys.hobby == hobby.hobby
    )
    hobby_exists = db.query(query.exists()).scalar()
    return hobby_exists


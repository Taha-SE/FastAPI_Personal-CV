from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base

class Persondaten(Base):
    __tablename__ = "persondaten"

    id = Column(Integer, primary_key=True, index= True)
    vorname = Column(String, index= True)
    nachname = Column(String, index= True)
    adresse = Column(String, index= True)
    telefonnummer = Column(String, index= True)
    geburtsdatum = Column(Date, index= True)
    geburtsort = Column(String, index= True)

class Ausbildung(Base):
    __tablename__ = "ausbildung"
    
    id = Column(Integer, primary_key=True, index= True)
    name = Column(String, index= True)
    ort = Column(String, index= True)
    abschluss=Column(String, index= True)
    anfang = Column(Date, index= True)
    ende= Column(Date, index= True, nullable= True)
    

class Beruferfahrungen(Base):
    __tablename__ = "beruferfahrungen"

    id = Column(Integer, primary_key=True, index= True)
    name = Column(String, index= True)
    ort = Column(String, index= True)
    titel = Column(String, index= True)
    anfang = Column(Date, index= True)
    ende= Column(Date, index= True, nullable= True)
    referenz = Column(String, index= True, nullable=True) 
    verantwortungen = Column(String, index = True, nullable= True)

class Programmiererfahrungen(Base):
    __tablename__ = "programmiererfahrungen"

    id = Column(Integer, primary_key=True, index= True)
    sprache = Column(String, index= True)
    frameworks  = Column(String, index=True,nullable=True)

class Projekte(Base):
    __tablename__ = "projekte"
    
    id = Column(Integer, primary_key=True, index= True)
    name= Column(String, index=True)
    beschreibung = Column(String, index=True)

class Sprachen(Base):
    __tablename__ = "sprachen"

    id = Column(Integer, primary_key=True, index= True)
    sprache= Column(String, index= True)
    level = Column(String, index=True)

class Stipendien(Base):
    __tablename__ = "stipendien"

    id = Column(Integer, primary_key=True, index= True)
    stiftung= Column(String, index= True)
    anfang = Column(Date, index= True)
    ende= Column(Date, index= True, nullable= True)
class Hobbys(Base):
    __tablename__ = "hobbys"

    id = Column(Integer, primary_key=True, index= True)
    hobby= Column(String, index= True)  

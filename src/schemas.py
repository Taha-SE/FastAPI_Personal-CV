from pydantic import BaseModel, validator
from typing import Optional
from datetime import date

#models for database
class PersondatenBase(BaseModel):
    vorname: str
    nachname: str
    adresse: str
    telefonnummer: str
    geburtsdatum: date
    geburtsort: str

class AusbildungBase(BaseModel):
    id: Optional[int]
    name: str
    ort: str
    abschluss: str
    anfang: date
    ende: Optional[date]

class BeruferfahrungenBase(BaseModel):
    id: Optional[int]
    name: str
    ort:str
    titel:str
    anfang:date
    ende:Optional[date]
    referenz:str
    verantwortungen:str

class ProgrammiererfahrungenBase(BaseModel):
    id: Optional[int]
    sprache:str
    frameworks:str
class ProjekteBase(BaseModel):
    id: Optional[int]
    name:str
    beschreibung:str
class SprachenBase(BaseModel):
    id: Optional[int]
    sprache:str
    level:str
class StipendienBase(BaseModel):
    id: Optional[int]
    stiftung:str
    anfang: date
    ende: Optional[date]

class HobbysBase(BaseModel):
    id: Optional[int]
    hobby:str

#models for reading/returning 
class Persondaten(PersondatenBase):
    class Config:
        schema_extra = {
           "example": {
                    "vorname": "Max",
                    "nachname": "Mueller",
                    "adresse": "Hauptstrasse 8, 14587 Berlin",
                    "telefonnummer": "012345678, +49-123-456-78",
                    "geburtsdatum": "Geburtsdatum JJ-MM-TT",
                    "geburtsort":"Berlin, Germany"
            }
        }
        orm_mode = True    

class Ausbildung(AusbildungBase):
    class Config:
        schema_extra = {
           "example": {
                    "name": "Name der Ausbildung",
                    "ort": "Stadt, Land",
                    "abschluss": "Abschluss",
                    "anfang": "Anfangsdatum JJ-MM-TT",
                    "ende": "Falls fortlaufend dann null"
            }
        }
        orm_mode = True

class Beruferfahrungen(BeruferfahrungenBase):

    class Config:  
        schema_extra = {
           "example": {
                    "name": "Name des Unternehmens",
                    "ort": "Stadt, Land",
                    "titel": "Titel der Position",
                    "anfang": "Anfangsdatum JJ-MM-TT",
                    "ende": "Falls fortlaufend dann null",
                    "referenz": "Name oder Email",
                    "verantwortungen": "Liste der Verantwortungen und Aufgaben"
            }
        }
        orm_mode = True 

class Programmiererfahrungen(ProgrammiererfahrungenBase):

    class Config:
        orm_mode = True
        schema_extra = {
           "example": {
                    "sprache": "Bsp. Python",
                    "frameworks": "Bsp. Flask, Django, Fastapi",
            }
        }
class Projekte(ProjekteBase):

    class Config:
        orm_mode = True
        schema_extra = {
           "example": {
                    "name": "Name des Porjekts",
                    "beschreibung": "Kurze Beschreibung des Projekts",
            }
        }
class Sprachen(SprachenBase):

    class Config:
        orm_mode = True
        schema_extra = {
           "example": {
                    "sprache": "Name der Sprache",
                    "level": "B1,B2 oder Fließend,Muttersprache",
            }
        }
class Stipendien(StipendienBase):

    class Config:
        orm_mode = True
        schema_extra = {
           "example": {
                    "stiftung": "Name der Stiftung",
                    "anfang": "Anfangsdatum JJ-MM-TT",
                    "ende": "Falls fortlaufend dann null"
            }
        }
class Hobbys(HobbysBase):

    class Config:
        orm_mode = True
        schema_extra = {
           "example": {
                    "hobby": "Name"
            }
        }


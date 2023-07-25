# Personal-CV with FastAPI
This Project is a API for saving your personal CV.

## Table of Contents
- [Requirements](#requirments)
- [Installation](#installation)
- [Endpoints](#endpoints)
- [Notes](#notes)

## Requirements
To run the application, you need to have the following installed:

-Python==3.9
-fastapi==0.100.0
-pydantic==1.10.7
-SQLAlchemy==1.3.18
-starlette==0.31.0

## Installation
1- Clone the repository:
~~~
git clone´https://github.com/Taha-SE/FastAPI_Personal-CV.git
~~~
2- Install the required dependencies:
~~~
pip install -r requirements.txt
~~~
3- Setup the database and run the application:
~~~
python -m uvicorn main:app --reload
~~~

## Endpoints
### Persondaten - /persondaten
- **GET**: Get all person data
- **POST**: Add a new person data entry
- **PUT**: Update an existing person data entry
- **DELETE**: Delete the person data entry

### Ausbildung - /ausbildung
- **GET**: Get all education entries
- **POST**: Add a new education entry
- **PUT**: Update an existing education entry
- **DELETE**: Delete an education entry

### Beruferfahrungen - /beruferfahrungen
- **GET**: Get all work experiences
- **POST**: Add a new work experience
- **PUT**: Update an existing work experience
- **DELETE**: Delete a work experience

### Programmiererfahrungen - /programmiererfahrungen
- **GET**: Get all programming experiences
- **POST**: Add a new programming experience
- **PUT**: Update an existing programming experience
- **DELETE**: Delete a programming experience

### Projekte - /projekte
- **GET**: Get all project entries
- **POST**: Add a new project entry
- **PUT**: Update an existing project entry
- **DELETE**: Delete a project entry

### Sprachen - /sprachen
- **GET**: Get all language entries
- **POST**: Add a new language entry
- **PUT**: Update an existing language entry
- **DELETE**: Delete a language entry

### Stipendien - /stipendien
- **GET**: Get all scholarship entries
- **POST**: Add a new scholarship entry
- **PUT**: Update an existing scholarship entry
- **DELETE**: Delete a scholarship entry

### Hobbys - /hobbys
- **GET**: Get all hobby entries
- **POST**: Add a new hobby entry
- **PUT**: Update an existing hobby entry
- **DELETE**: Delete a hobby entry


## Notes:
The variable "end" is optional and can be set as null. In this case it will shown as "forlaufend"

This is my first big project! So please feel free to comment and leave suggestions 
  


  

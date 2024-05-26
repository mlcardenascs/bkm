from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import models.models as models
import schemas.schemas as schemas
from database.db import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.params import Depends
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/')
def main():
    return RedirectResponse(url='/docs/')

@app.get('/grupos', tags=["Grupos"])
def getGrupos(db:Session=Depends(get_db)):
    try:
        grupos = db.query(models.Grupo).all()
        return grupos
    except:
        return {"Status":500}

@app.get('/grupos/{grupo}', tags=['Grupos'])
def getGrupo(grupo:str, db:Session=Depends(get_db)):
    try:
        grupo = db.query(models.Grupo).filter_by(grupo=grupo).first()
        return grupo
    except:
        return {"Status":500}

@app.post('/grupos', tags=['Grupos'])
def crearGrupo(entry:schemas.Grupo, db:Session=Depends(get_db)):
    try:
        grupo = models.Grupo(grupo=entry.grupo, aula=entry.aula, edificio=entry.edificio)
        db.add(grupo)
        db.commit()
        db.refresh(grupo)
        return grupo
    except:
        return {"Status":500} 

@app.put('/grupos', tags=['Grupos'])
def ectualizarGrupo(grp:str, entry:schemas.Grupo, db:Session=Depends(get_db)):
    try:
        grupo = db.query(models.Grupo).filter_by(grupo=grp).first()
        grupo.grupo = entry.grupo
        grupo.aula = entry.aula
        grupo.edificio = entry.edificio
        db.commit()
        db.refresh(grupo)
        return grupo
    except:
        return {"Status":500}
    
@app.delete('/grupos', tags=['Grupos'])
def eliminarGrupo(entry:str, db:Session=Depends(get_db)):
    try:
        grupo = db.query(models.Grupo).filter_by(grupo=entry).first()
        db.delete(grupo)
        db.commit()
        return {"Status":200}
    except:
        return {"Status":500}
    
@app.get('/profesor', tags=['Profesor'])
def getProfesores(db:Session=Depends(get_db)):
    try:
        profesor = db.query(models.Profesor).all()
        return profesor
    except:
        return {"Status":500}
    
@app.get('/profesor/{correo}', tags=['Profesor'])
def getProfesor(correo:str, db:Session=Depends(get_db)):
    try:
        profesor = db.query(models.Profesor).filter_by(correo=correo).first()
        return profesor
    except:
        return {"Status":500}
    
@app.post('/profesor', tags=['Profesor'])
def crearProfesor(entry:schemas.Maestro, db:Session=Depends(get_db)):
    try:
        profesor = models.Profesor(nombre=entry.nombre, apellido=entry.apellido, correo=entry.correo, carrera=entry.carrera)
        db.add(profesor)
        db.commit()
        db.refresh(profesor)
        return profesor
    except:
        return {"Status":500}
    
@app.put('/profesor/', tags=["Profesor"])
def actualizarProfesor(correo:str, entry:schemas.Maestro ,db:Session=Depends(get_db)):
    try:
        profesor = db.query(models.Profesor).filter_by(correo=correo).first()
        profesor.nombre = entry.nombre
        profesor.apellido = entry.apellido
        profesor.correo = entry.correo
        profesor.carrera = entry.carrera
        db.commit()
        db.refresh(profesor)
        return profesor
    except:
        return {"Status":500}
    
@app.delete('/profesor', tags=['Profesor'])
def eliminarProfesor(correo:str ,db:Session=Depends(get_db)):
    try:
        profesor = db.query(models.Profesor).filter_by(correo=correo).first()
        db.delete(profesor)
        db.commit()
        return {"Status":200}
    except:
        return {"Status":500}
        
@app.get('/materias', tags=['Materias'])
def getMaterias(db:Session=Depends(get_db)):
    try:
        materias = db.query(models.Materia).all()
        return materias
    except:
        return {"Status":500}
    
@app.get('/materias/{materia}', tags=['Materias'])
def getMateria(materia:str, db:Session=Depends(get_db)):
    try:
        materia = db.query(models.Materia).filter_by(materia=materia).first()
        return materia
    except:
        return {"Status":500}
    
@app.post('/materias', tags=['Materias'])
def crearMateria(entry:schemas.Materia, db:Session=Depends(get_db)):
    try:
        materia = models.Materia(materia=entry.materia, carrera=entry.carrera)
        db.add(materia)
        db.commit()
        db.refresh(materia)
        return materia
    except:
        return {"Status":500}
    
@app.put('/materias', tags=['Materias'])
def actualizarMateria(materia:str, entry:schemas.Materia, db:Session=Depends(get_db)):
    try:
        materia = db.query(models.Materia).filter_by(materia=materia).first()
        materia.materia = entry.materia
        materia.carrera = entry.carrera
        db.commit()
        db.refresh(materia)
        return materia
    except:
        return {"Status":500}
    
@app.delete('/materias', tags=['Materias'])
def eliminarMateria(materiaN:str, db:Session=Depends(get_db)):
    try:
        materia = db.query(models.Materia).filter_by(materia=materiaN).first()
        db.delete(materia)
        db.commit()
        return {"Status":200}
    except:
        return {"Status":500}        
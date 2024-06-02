from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import models.models as models
import schemas.schemas as schemas
from database.db import SessionLocal
from sqlalchemy.orm import Session
from fastapi.params import Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

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
    
@app.get('/horaios', tags=['Horarios'])
def getHoraios(db:Session=Depends(get_db)):
    try:
        horaios = db.query(models.Horario).all()
        return horaios
    except:
        return {"Status":500}
    
@app.get('/horario', tags=['Horarios'])
def getHorario(entry:str, db:Session=Depends(get_db)):
    try:
        horario = db.query(models.Horario).filter_by(grupo=entry).all()
        return horario
    except:
        return {"Status":500}
    
@app.post('/horario', tags=['Horarios'])
def crearHorario(entry:schemas.Horario, db:Session=Depends(get_db)):
    try:
        horario = models.Horario(grupo=entry.grupo, aula=entry.aula, hora=entry.hora, materia=entry.materia, profesor=entry.profesor, semana=entry.semana, dias=entry.dias)
        db.add(horario)
        db.commit()
        db.refresh(horario)
        return horario
    except:
        return {"Status":500}
        
@app.put('/horaio', tags=['Horarios'])
def actualizarHorario(grp:str,mtr:str, entry:schemas.Horario, db:Session=Depends(get_db)):
    try:
        horario = db.query(models.Horario).filter_by(grupo=grp, materia=mtr).first()
        horario.grupo = entry.grupo
        horario.aula = entry.aula
        horario.hora = entry.hora
        horario.materia = entry.materia
        horario.profesor = entry.profesor
        horario.semana = entry.semana
        horario.dias = entry.dias
        db.commit()
        db.refresh(horario)
        return horario
    except:
        return {"Status":500}
    
@app.delete('/horario', tags=['Horarios'])
def eliminarHorario(grp:str, db:Session=Depends(get_db)):
    try:
        sqlstm = text("delete from horario where grupo = '"+grp+"'")
        db.execute(sqlstm)
        db.commit()
        return {"Status":200}
    except:
        return {"Status":500}


@app.get('/usuarios', tags=['Usuarios'])
def getUsuarios(db:Session=Depends(get_db)):
    try:
        usuarios = db.query(models.Usuario).all()
        return usuarios
    except:
        return {"Status":500}
    
@app.get('/usuario', tags=['Usuarios'])
def getUsuario(entry:str, db:Session=Depends(get_db)):
    try:
        usuario = db.query(models.Usuario).filter_by(correo=entry).first()
        if usuario == None:
            return {"Status":500}
        return usuario
    except:
        return {"Status": 500}
    
@app.post('/usuario', tags=['Usuarios'])
def crearUsuario(entry:schemas.Usuario, db:Session=Depends(get_db)):
    try:
        usuario = models.Usuario(nombre=entry.nombre, apellido=entry.apellido, correo=entry.correo, pwd = entry.pwd, tipo_usuario=entry.tipo_usuario)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except:
        return {"Status":500}

@app.put('/usuario', tags=['Usuarios'])
def actualizarUsuario(entry:schemas.Usuario, mail:str, db:Session=Depends(get_db)):
    try:
        usuario = db.query(models.Usuario).filter_by(correo=mail).first()
        usuario.nombre = entry.nombre
        usuario.apellido = entry.apellido
        usuario.correo = entry.correo
        usuario.pwd = entry.pwd
        usuario.tipo_usuario = entry.tipo_usuario
        db.commit()
        db.refresh(usuario)
        return usuario
    except:
        return {"Status":500}
        
@app.delete('/usuario', tags=['Usuarios'])
def eleiminarUsuario(mail:str, db:Session=Depends(get_db)):
    try:
        usuario = db.query(models.Usuario).filter_by(correo=mail).first()
        db.delete(usuario)
        db.commit()
        return {"Status":200}
    except:
        return {"Status":500}
    
@app.get('/usuaio/login', tags=['Usuario'], response_model=schemas.UserLogin)
def login(mail:str, contra:str, db:Session=Depends(get_db)):
    try:
        usuario = db.query(models.Usuario).filter_by(correo=mail).first()
        if(usuario == None):
            return {"Status":404}
        elif usuario.pwd == contra:
            usrlg = schemas.UserLogin
            usrlg = usuario
            return usrlg
        return{"Status":404}
    except:
        return {"Status":500}
        
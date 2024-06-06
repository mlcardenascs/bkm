from pydantic import BaseModel
from typing import Optional

class Grupo(BaseModel):
    id:Optional[int] = None
    grupo:str
    aula:str
    edificio:str
    carrera:str
    
    class Config():
        from_attributes = True

class Maestro(BaseModel):
    id:Optional[int] = None
    nombre:str
    apellido:str
    correo:str
    carrera:str
    
    class Config():
        from_attributes = True
        
class Materia(BaseModel):
    id:Optional[int] = None
    materia:str
    carrera:str
    
    class Config():
        from_attributes = True

class Horario(BaseModel):
    id:Optional[int] = None
    grupo:str
    aula:str
    hora_inicio:str
    hora_fin:str
    materia:str
    profesor:str
    semana:str
    hora:str
    carrera:str
        
    class config():
        from_attributes = True

class Usuario(BaseModel):
    id:Optional[int] = None
    nombre:str
    apellido:str
    correo:str
    pwd:str
    tipo_usuario:str
    
    class config():
        from_attributes = True
        
class UserLogin(BaseModel):
    nombre:str
    apellido:str
    correo:str
    tipo_usuario:str
    
    class config():
        from_attributes = True
        
class AsistenciaAlumno(BaseModel):
    id:Optional[int] = None
    grupo:str
    hora:str
    materia:str
    profesor:str
    Lun:str
    Mar:str
    Mier:str
    Jue:str
    Vier:str
    semana:str
    carrera:str
    
    class config():
        from_attributes = True

class AsistenciaProfe(BaseModel):
    id:Optional[int] = None
    grupo:str
    hora:str
    materia:str
    profesor:str
    Lun:str
    Mar:str
    Mier:str
    Jue:str
    Vier:str
    semana:str
    carrera:str
    
    class config():
        from_attributes = True
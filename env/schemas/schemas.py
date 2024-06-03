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
    dias:str
        
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
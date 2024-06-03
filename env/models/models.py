from sqlalchemy import Column, Integer, String
from database.db import Base

class Grupo(Base):
    __tablename__ = 'grado'
    id = Column(Integer, primary_key=True, autoincrement=True)
    grupo = Column(String(25), nullable=False)
    aula = Column(String(10), nullable=False)
    edificio = Column(String(4), nullable=False)
    carrera = Column(String(45), nullable=False)

class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    correo = Column(String(50), nullable=False)
    carrera = Column(String(50), nullable=False)
    
class Materia(Base):
    __tablename__ = 'materia'
    id = Column(Integer, primary_key=True, autoincrement=True)
    materia = Column(String(50), nullable=False)
    carrera = Column(String(50), nullable=False)

class Horario(Base):
    __tablename__ = 'horario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    grupo = Column(String(20), nullable= False)
    aula = Column(String(10), nullable=False)
    hora_inicio = Column(String(10), nullable=False)
    hora_fin = Column(String(10), nullable=False)
    materia = Column(String(50), nullable=False)
    profesor = Column(String(50), nullable=False)
    semana = Column(String(50), nullable=False)
    hora = Column(String(45), nullable=False)
    carrera = Column(String(50), nullable=False)
    
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    apellido = Column(String(45), nullable=False)
    correo = Column(String(45), nullable=False)
    pwd = Column(String(45), nullable=False)
    tipo_usuario = Column(String(45), nullable=False)
    
class Asistencia(Base):
    __tablename__ = 'asistencias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    grupo = Column(String(45), nullable=False)
    hora = Column(String(45), nullable=False)
    materia = Column(String(45), nullable=False)
    profesor = Column(String(45), nullable=False)
    Lun = Column(String(15), nullable=False)
    Mar = Column(String(15), nullable=False)
    Mier = Column(String(15), nullable=False)
    Jue = Column(String(15), nullable=False)
    Vier = Column(String(15), nullable=False)
    semana = Column(String(45), nullable=False)
    carrera = Column(String(45), nullable=False)
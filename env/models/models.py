from sqlalchemy import Column, Integer, String
from database.db import Base

class Grupo(Base):
    __tablename__ = 'grado'
    id = Column(Integer, primary_key=True, autoincrement=True)
    grupo = Column(String(3), nullable=False)
    aula = Column(String(3), nullable=False)
    edificio = Column(String(4), nullable=False)

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
    hora = Column(String(10), nullable=False)
    materia = Column(String(50), nullable=False)
    profesor = Column(String(50), nullable=False)
    
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.orm import Session
from sqlalchemy import event

# Define tu modelo Department
class Template(Base):
    __tablename__ = "template"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre_plantilla = Column(String(30))
    unidad_medida = Column(String(5))
    ancho = Column(Integer)
    alto = Column(Integer)
    fondo = Column(String(30))
    foto_x = Column(Integer)
    foto_y = Column(Integer)
    tipo_codigo = Column(String(5), nullable=True)
    tipo_codigo_x = Column(Integer, nullable=True)
    tipo_codigo_y = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())  # Fecha de creación
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # Fecha de última actualización

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

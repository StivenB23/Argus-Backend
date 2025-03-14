from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.orm import Session
from sqlalchemy import event

# Define tu modelo Department
class Department(Base):
    __tablename__ = "facultad"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(30))
    nombre = Column(String(30))
    descripcion = Column(Text)
    correo_contacto = Column(String(30))
    created_at = Column(TIMESTAMP, server_default=func.now())  # Fecha de creación
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # Fecha de última actualización

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base

# Define tu modelo Department
class Degree(Base):
    __tablename__ = "programa"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    codigo = Column(String(255))
    descripcion = Column(Text)
    nivel = Column(String(30))
    duracion = Column(Integer)
    modalidad = Column(String(20))

    created_at = Column(TIMESTAMP, server_default=func.now())  # Fecha de creación
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # Fecha de última actualización
    

    # Relación con el modelo Rol
    rol_id = Column(Integer, ForeignKey("facultad.id"))
    rol = relationship("Department")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
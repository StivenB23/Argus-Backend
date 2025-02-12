from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base

# Define tu modelo Department
class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(30))
    nombre = Column(String(30))
    descripcion = Column(Text)
    correo_contacto = Column(String(30))

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
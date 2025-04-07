from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.orm import Session
from sqlalchemy import event


# Define tu modelo Department
class FieldTemplate(Base):
    __tablename__ = "campo_plantilla"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30))
    ubicacion_x = Column(String(5))
    ubicacion_y = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())  # Fecha de creación
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # Fecha de última actualización



    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

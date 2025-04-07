from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .associations import rol_instalacion
from .base import Base


# Define tu modelo Department
class Facility(Base):
    __tablename__ = "instalacion"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    tipo = Column(String(255))
    direccion = Column(String(30))

    roles = relationship("Role", secondary=rol_instalacion, back_populates="instalaciones")


    created_at = Column(TIMESTAMP, server_default=func.now())  # Fecha de creación
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # Fecha de última actualización


    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
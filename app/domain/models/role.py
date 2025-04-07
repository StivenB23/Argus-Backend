from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .associations import rol_instalacion
from .base import Base

# Define tu modelo User
class Role(Base):
    __tablename__ = "rol"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20))
    estado = Column(Boolean, unique=False, default=True)

    instalaciones = relationship("Facility", secondary=rol_instalacion, back_populates="roles")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
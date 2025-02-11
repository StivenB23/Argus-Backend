from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.adapters.database.mysql import Base

# Define tu modelo User
class Rol(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))

    posts = relationship("User", back_populates="rol")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
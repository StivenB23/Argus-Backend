from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .associations import role_facility_association
from .base import Base

class Facility(Base):
    __tablename__ = "facility"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    type = Column(String(255))
    address = Column(String(30))

    roles = relationship("Role", secondary=role_facility_association, back_populates="facilities")

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Facility(id={self.id}, name={self.name})"

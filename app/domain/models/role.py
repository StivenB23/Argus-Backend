from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .associations import role_facility_association
from .base import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    is_active = Column(Boolean, default=True)

    facilities = relationship("Facility", secondary=role_facility_association, back_populates="roles")

    def __repr__(self):
        return f"Role(id={self.id}, name={self.name}, active={self.is_active})"

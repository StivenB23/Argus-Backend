from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .base import Base


class Degree(Base):
    __tablename__ = "degree"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    code = Column(String(255))
    description = Column(Text)
    level = Column(String(30))
    duration = Column(Integer)
    modality = Column(String(20))

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    department_id = Column(Integer, ForeignKey("department.id"))
    department = relationship("Department")

    def __repr__(self):
        return f"Degree(id={self.id}, name={self.name}, code={self.code})"

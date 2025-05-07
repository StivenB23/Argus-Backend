from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from .base import Base


class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(30))
    name = Column(String(50))
    description = Column(Text)
    contact_email = Column(String(40))

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Department(id={self.id}, name={self.name}, email={self.contact_email})"

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .identity_card import IdentityCard
from .base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    document_type = Column(String(10))
    document_number = Column(String(20))
    first_name = Column(String(255))
    last_name = Column(String(255))
    photo = Column(String(255))
    status = Column(String(30), default="active")
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

    #Relaciones
    role_id = Column(Integer, ForeignKey("role.id"))
    role = relationship("Role")

    identity_card = relationship("IdentityCard", back_populates="user", uselist=False, cascade="all, delete")
    #timestamps
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"User(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})"

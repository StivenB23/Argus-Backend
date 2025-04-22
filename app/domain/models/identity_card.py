from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class IdentityCard(Base):
    __tablename__ = "identity_card"

    id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    uuid = Column(String(36), nullable=False, unique=True)
    issue_date = Column(Date, nullable=True)
    status = Column(String(36), nullable=False, default="activo")

    user = relationship("User", back_populates="identity_card")

    template_id = Column(Integer, ForeignKey("card_template.id"))
    template = relationship("Template")


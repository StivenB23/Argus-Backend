from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class AccessLog(Base):
    __tablename__ = "access_log"

    id = Column(Integer, primary_key=True, index=True)
    access_method = Column(String(50))  # Ej: "web", "mobile", "scanner"
    uuid_card = Column(String(30))
    location = Column(String(100), nullable=True)
    status = Column(String(20), default="success")  # ✅ "success", "failed", "unauthorized"
    reason = Column(String(255), nullable=True)  # Opcional: mensaje de error si falló
    timestamp = Column(TIMESTAMP, server_default=func.now())

    identity_card_id = Column(Integer, ForeignKey("identity_card.id"), nullable=True)  # Puede ser null si no se encontró
    identity_card = relationship("IdentityCard", backref="access_logs")

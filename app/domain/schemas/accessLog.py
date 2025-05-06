from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AccessLogCreate(BaseModel):
    identity_card_id: Optional[int]  # Puede ser None si el acceso no está ligado a una cédula
    access_method: Optional[str]     # Ej: "web", "mobile", "scanner"
    location: Optional[str]
    uuid: str
    status: str                      # Ej: "success", "failed", "unauthorized"
    reason: Optional[str]            # Detalle en caso de error

class AccessLogResponse(AccessLogCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

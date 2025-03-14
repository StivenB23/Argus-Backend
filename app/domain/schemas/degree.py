from pydantic import BaseModel
from typing import Optional

class DegreeBase(BaseModel):
    nombre: str
    codigo: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int
    modalidad: str

class DegreeCreate(DegreeBase):
    pass

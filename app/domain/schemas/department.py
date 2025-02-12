from pydantic import BaseModel
from typing import Optional

class DepartmentBase(BaseModel):
    nombre: str
    codigo: str
    descripcion: Optional[str] = None
    correo_contacto: str


class DepartmentCreate(DepartmentBase):
    pass

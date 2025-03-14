from pydantic import BaseModel
from typing import Optional

class TemplateBase(BaseModel):
    nombre_plantilla: str
    unidad_medida: str
    ancho: int
    alto: int
    foto_x:int
    foto_y:int
    fondo:str
    tipo_codigo: Optional[str] = None
    tipo_codigo_y: Optional[int] = None
    tipo_codigo_x: Optional[int] = None


class TemplateCreate(TemplateBase):
    pass

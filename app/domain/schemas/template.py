from pydantic import BaseModel
from typing import Optional

class TemplateBase(BaseModel):
    template_name: str
    unit: str
    width: float
    height: float
    photo_width: float
    photo_height: float
    photo_x: float
    photo_y: float
    background: str
    labels:str
    code_type: Optional[str] = None
    code_type_y: Optional[int] = None
    code_type_x: Optional[int] = None

class TemplateCreateDTO(TemplateBase):
    pass


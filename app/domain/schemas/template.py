from pydantic import BaseModel
from typing import Optional

class TemplateBase(BaseModel):
    template_name: str
    unit: str
    width: int
    height: int
    photo_width: float
    photo_height: int
    photo_x: int
    photo_y: int
    background: str
    code_type: Optional[str] = None
    code_type_y: Optional[int] = None
    code_type_x: Optional[int] = None

class TemplateCreateDTO(TemplateBase):
    pass


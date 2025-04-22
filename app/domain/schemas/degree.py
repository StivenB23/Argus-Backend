from pydantic import BaseModel
from typing import Optional

class DegreeBase(BaseModel):
    name: str
    code: str
    description: Optional[str] = None
    level: str
    duration: int
    modality: str

class DegreeCreate(DegreeBase):
    pass

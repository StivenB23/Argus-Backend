from pydantic import BaseModel
from typing import Optional

class DepartmentBase(BaseModel):
    name: str
    code: str
    description: Optional[str] = None
    contact_email: str

class DepartmentCreate(DepartmentBase):
    pass

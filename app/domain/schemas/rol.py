from typing import Optional
from app.domain.schemas.facility import FacilityResponse
from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str
    is_active: Optional[bool]

class RoleCreate(RoleBase):
    status: bool = True

class RoleFacilityResponse(RoleBase):
    id:int
    facilities: list[FacilityResponse]

    class Config:
        orm_mode = True

class RoleUpdate(BaseModel):
    name: str
    facilities: list[int]  # IDs de instalaciones
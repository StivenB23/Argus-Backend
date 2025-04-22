from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    status: bool = True

from pydantic import BaseModel
# from schemas.rol import RolResponse

class RolBase(BaseModel):
    nombre: str

class RolCreate(RolBase):
    estado: bool = True

# class RolResponse(RolBase):
#     id: int
#     rol: RolResponse

#     class Config:
#         orm_mode = True

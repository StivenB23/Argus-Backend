from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional
# from schemas.rol import RolResponse

# Esquema base
class UserBase(BaseModel):
    nombre: Annotated[str, Field(..., description="El nombre del usuario", min_length=2, max_length=255)]
    correo: EmailStr

# Esquema para registrar un usuario
class UserCreate(UserBase):
    tipo_documento: Annotated[str, Field(..., description="Tipo de documento (CC, TI, etc.)", min_length=2, max_length=10)]
    num_documento: Annotated[str, Field(..., description="Número de documento", min_length=5, max_length=20)]
    apellido: Annotated[str, Field(..., description="Apellido del usuario", min_length=2, max_length=255)]
    clave: Annotated[str, Field(..., description="Contraseña del usuario", min_length=8, max_length=255)]
    rol_id: int

# Esquema para actualizar un usuario (opcionalidad de los campos)
class UserUpdate(BaseModel):
    nombre: Optional[str] = Field(None, description="Nuevo nombre del usuario", min_length=2, max_length=255)
    apellido: Optional[str] = Field(None, description="Nuevo apellido del usuario", min_length=2, max_length=255)
    email: Optional[EmailStr] = Field(None, description="Nuevo email del usuario")
    clave: Optional[str] = Field(None, description="Nueva contraseña", min_length=8, max_length=255)
    rol_id: Optional[int] = Field(None, description="Nuevo rol del usuario")

class UserResponse(UserBase):
     id: int
     apellido: str
     rol: str

# Esquema para respuesta de usuario
# class UserResponse(UserBase):
#     id: int
#     apellido: str
#     tipo_documento: str
#     num_documento: str
#     rol: RolResponse

#     class Config:
#         from_attributes = True

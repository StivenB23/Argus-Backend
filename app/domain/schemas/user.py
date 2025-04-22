from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional

from app.domain.schemas.identityCard import IdentityCardWithTemplateResponse
from app.domain.schemas.template import TemplateBase

class UserBase(BaseModel):
    first_name: Annotated[str, Field(..., description="User's first name", min_length=2, max_length=255)]
    email: EmailStr

class UserCreate(UserBase):
    document_type: Annotated[str, Field(..., description="Document type (CC, TI, etc.)", min_length=2, max_length=10)]
    document_number: Annotated[str, Field(..., description="Document number", min_length=5, max_length=20)]
    last_name: Annotated[str, Field(..., description="User's last name", min_length=2, max_length=255)]
    password: Annotated[str, Field(..., description="User's password", min_length=8, max_length=255)]
    photo: str
    role_id: int
    template_id: Optional[int] = None

class UserCreated(BaseModel):
    id:int
    role:int
    document_number:str

class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, description="New first name", min_length=2, max_length=255)
    last_name: Optional[str] = Field(None, description="New last name", min_length=2, max_length=255)
    email: Optional[EmailStr] = Field(None, description="New email")
    password: Optional[str] = Field(None, description="New password", min_length=8, max_length=255)
    role_id: Optional[int] = Field(None, description="New role ID")

class UserResponse(UserBase):
    id: int
    last_name: str
    role: str

class UserResponseIdentity(UserBase):
    id: int
    last_name: str
    document_type: str
    document_number: str
    role: str
    photo: str
    identity_card: IdentityCardWithTemplateResponse

class UsersResponse(BaseModel):
    id: int
    document_type: Optional[str] = None
    document_number: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str
    status: Optional[str] = "Activo"
    role: str

    class Config:
        from_attributes = True

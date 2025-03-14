from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID, uuid4

class User(BaseModel):
    _id: UUID = uuid4()
    name: str
    email: EmailStr
    age: Optional[int] = None

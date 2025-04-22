from pydantic import BaseModel
from typing import Optional
from datetime import date

from app.domain.schemas.template import TemplateBase


class IdentityCard(BaseModel):
    uuid:str
    status:str = "activo"



class IdentityCardCreateDTO(IdentityCard):
    user_id:int
    template_id:int

class IdentityCardWithTemplateResponse(IdentityCard):
    issue_date: date
    template: TemplateBase

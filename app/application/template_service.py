from sqlalchemy.orm import Session

from app.domain.models.template import Template
from app.domain.schemas.template import TemplateCreate


async def create_template(db:Session, template: TemplateCreate):
    template_s = Template()
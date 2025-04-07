from sqlalchemy.orm import Session

from app.domain.models.template import Template
from app.domain.schemas.template import TemplateCreateDTO


async def create_template_service(db:Session, template: TemplateCreateDTO):
    print("hiii")
    template_new = Template(**template.dict())
    print("template_new")
    db.add(template_new)
    db.commit()
    db.refresh(template_new)
    return template_new
from sqlalchemy.orm import Session

from app.domain.models.template import Template
from app.domain.schemas.template import TemplateCreateDTO

async def get_templates_service(db:Session):
    templates = db.query(Template).all()
    return templates

async def create_template_service(db:Session, template: TemplateCreateDTO):
    template_new = Template(**template.dict())
    db.add(template_new)
    db.commit()
    db.refresh(template_new)
    return template_new
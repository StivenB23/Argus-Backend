from sqlalchemy.orm import Session

from app.domain.models.identity_card import IdentityCard
from app.domain.schemas.identityCard import IdentityCardCreateDTO
from datetime import datetime

async def create_identify_card_service(db, create_identity_card:IdentityCardCreateDTO):
    date = datetime.now().date()
    new_identity_card = IdentityCard(
        id=create_identity_card.user_id,
        uuid=create_identity_card.uuid,
        issue_date= date,
        template_id=create_identity_card.template_id
    )
    db.add(new_identity_card)
    db.commit()
    db.refresh(new_identity_card)
    return new_identity_card

async def get_identity_card_by_uuid_service(db:Session, uuid:str):
    identity_card = db.query(IdentityCard).filter_by(uuid=uuid).first()
    return identity_card

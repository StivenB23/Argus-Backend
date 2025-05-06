from sqlalchemy.orm import Session
from app.domain.models.AccesLog import AccessLog
from app.domain.schemas.accessLog import AccessLogCreate


async def create_access_log(db: Session, log_data: AccessLogCreate):
    log_entry = AccessLog(
        identity_card_id=log_data.identity_card_id,
        access_method=log_data.access_method,
        uuid_card= log_data.uuid,
        location=log_data.location,
        status=log_data.status,
        reason=log_data.reason
    )
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return log_entry

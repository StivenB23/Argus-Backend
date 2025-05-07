from sqlalchemy.orm import Session

from app.domain.models.instalacion import Facility
from app.domain.schemas.facility import FacilityResponse


async def get_facilities_service(db:Session):
    facilities = db.query(Facility).all()
    facilitiesMapper = [
        FacilityResponse(
            id=facility.id,
            name=facility.name,
            address=facility.address,
            type=facility.type
        )
        for facility in facilities
    ]
    return facilitiesMapper
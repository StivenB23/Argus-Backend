from typing import Optional

from pydantic import BaseModel, ConfigDict


class FacilityBase(BaseModel):
    name: str
    type: Optional[str]
    address: Optional[str]

class FacilityResponse(FacilityBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
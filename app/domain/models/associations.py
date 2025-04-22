from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

# Association table between Role and Facility
role_facility_association = Table(
    "role_facility",  # Renamed from "rol_instalacion" to "role_facility"
    Base.metadata,
    Column("role_id", Integer, ForeignKey("role.id"), primary_key=True),
    Column("facility_id", Integer, ForeignKey("facility.id"), primary_key=True)
)

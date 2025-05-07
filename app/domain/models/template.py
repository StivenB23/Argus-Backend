from sqlalchemy import Column, Integer, String, Text, Float, TIMESTAMP, func
from .base import Base


class Template(Base):
    __tablename__ = "card_template"

    id = Column(Integer, primary_key=True, index=True)
    template_name = Column(String(30))
    unit = Column(String(5))
    width = Column(Float)
    height = Column(Float)
    background = Column(Text)
    labels = Column(String(255))

    photo_width = Column(Float)
    photo_height = Column(Float)
    photo_x = Column(Float)
    photo_y = Column(Float)

    code_type = Column(String(5), nullable=True)
    code_type_y = Column(Float, nullable=True)
    code_type_x = Column(Float, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Template(id={self.id}, name={self.template_name})"

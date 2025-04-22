from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from .base import Base


class Template(Base):
    __tablename__ = "card_template"

    id = Column(Integer, primary_key=True, index=True)
    template_name = Column(String(30))
    unit = Column(String(5))
    width = Column(Integer)
    height = Column(Integer)
    background = Column(Text)

    photo_width = Column(Integer)
    photo_height = Column(Integer)
    photo_x = Column(Integer)
    photo_y = Column(Integer)

    code_type = Column(String(5), nullable=True)
    code_type_y = Column(Integer, nullable=True)
    code_type_x = Column(Integer, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Template(id={self.id}, name={self.template_name})"

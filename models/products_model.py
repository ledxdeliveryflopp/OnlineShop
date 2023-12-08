import uuid
from sqlalchemy import Column, String, Numeric, UUID, ForeignKey, Integer
from sqlalchemy.orm import relationship
from database.database import Base
from models.tags_model import Tag


class Product(Base):
    __tablename__ = "products"

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), unique=True, index=True)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    tags_id = Column(Integer, ForeignKey(Tag.id))

    tags = relationship(Tag)
    # vendor = Column

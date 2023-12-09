from typing import List
from sqlalchemy import Column, String, Numeric, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import ARRAY, INTEGER
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), unique=True, index=True)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    tags_id = Column(Integer, ForeignKey("tags.id"))

    tags = relationship("Tag", back_populates="products")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), unique=True, index=True)

    products = relationship("Product", back_populates="tags")

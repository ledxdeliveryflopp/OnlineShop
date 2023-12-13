from typing import List
from sqlalchemy import Column, String, Numeric, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped
from database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), unique=True, index=True)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)

    tags_id = Column(Integer, ForeignKey("tags.id"))
    tags: Mapped[List["Tag"]] = relationship(back_populates="products")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), unique=True, index=True)

    products: Mapped[List["Product"]] = relationship(back_populates="tags")

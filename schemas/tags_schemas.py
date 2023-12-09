from typing import List
from pydantic import BaseModel


class ProductSchemas(BaseModel):
    """Схема товара"""

    id: int
    title: str

    class Config:
        orm_mode = True


class TagBaseSchemas(BaseModel):
    """Схема тега"""

    id: int
    title: str

    class Config:
        orm_mode = True


class TagSchemas(BaseModel):
    """Схема тега"""

    title: str
    products: List[ProductSchemas] = []

    class Config:
        orm_mode = True


class TagCreateSchemas(BaseModel):
    title: str

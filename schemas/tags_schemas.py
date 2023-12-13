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

    title: str

    class Config:
        orm_mode = True


class TagResponseSchemas(BaseModel):
    """Схема тега для ответа"""

    id: int
    title: str
    products: List[ProductSchemas] = []

    class Config:
        orm_mode = True


class TagCreateSchemas(TagBaseSchemas):
    """Схема тега для создания"""

    pass


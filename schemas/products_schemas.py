from uuid import UUID
from pydantic import BaseModel
from schemas.tags_schemas import TagSchemas


class ProductAdminSchemas(BaseModel):
    """Схема товара для админа"""
    # id: UUID
    id: int
    title: str
    description: str
    price: int

    class Config:
        orm_mode = True


class ProductBaseSchemas(BaseModel):
    """Базавая схема товара"""

    title: str
    description: str
    price: int

    class Config:
        orm_mode = True


class ProductSchemas(BaseModel):
    """Схема товара"""

    title: str
    description: str
    price: int
    tags: TagSchemas

    class Config:
        orm_mode = True


class ProductCreateSchemas(ProductBaseSchemas):
    """Схема товара для создания"""
    pass

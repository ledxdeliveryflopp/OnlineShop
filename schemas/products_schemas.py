from pydantic import BaseModel


class TagSchemas(BaseModel):
    """Схема тега"""

    title: str

    class Config:
        orm_mode = True


class ProductResponseSchemas(BaseModel):
    """Схема товара"""

    title: str
    description: str
    price: int
    tags: TagSchemas

    class Config:
        orm_mode = True


class ProductBaseSchemas(BaseModel):
    """Базавая схема товара"""

    title: str
    description: str
    price: int
    tags_id: int

    class Config:
        orm_mode = True


class ProductCreateSchemas(ProductBaseSchemas):
    """Схема товара для создания"""

    pass

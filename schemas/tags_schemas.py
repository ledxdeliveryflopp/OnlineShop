from uuid import UUID
from pydantic import BaseModel


class TagAdminSchemas(BaseModel):
    """Схема тега для админа"""
    # id: UUID
    id: int
    title: str

    class Config:
        orm_mode = True


class TagSchemas(BaseModel):
    """Схема тега"""

    title: str

    class Config:
        orm_mode = True


class TagCreateSchemas(TagSchemas):
    """Схема тега для создания"""
    pass

from sqlalchemy.orm import Session
from models.products_model import Tag
from schemas.tags_schemas import TagCreateSchemas


def get_tag(db: Session, limit: int = 100):
    return db.query(Tag).limit(limit).all()


def get_tag_by_title(db: Session, title: str):
    return db.query(Tag).filter(Tag.title == title).first()


def get_tag_by_id(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()


def create_Tag(db: Session, tag: TagCreateSchemas):
    db_tag = Tag(**tag.model_dump())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import engine, SessionLocal
from models import tags_model
from schemas.tags_schemas import TagAdminSchemas, TagSchemas, TagCreateSchemas
from crud.tags_crud import get_tag_by_title, get_tag, create_Tag

tags_model.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/tags",
    tags=["tags"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/list/",  response_model=list[TagSchemas])
def get_tags(limit: int = 100, db: Session = Depends(get_db)):
    tags = get_tag(db, limit=limit)
    return tags


@router.get("/list/admin/",  response_model=list[TagAdminSchemas])
def get_tags_admin(limit: int = 100, db: Session = Depends(get_db)):
    tags = get_tag(db, limit=limit)
    return tags


@router.post("/create/", response_model=TagSchemas)
def add_tags(tag: TagCreateSchemas, db: Session = Depends(get_db)):
    tags = get_tag_by_title(db, title=tag.title)
    if tags:
        raise HTTPException(status_code=400, detail="Такой тег есть")
    return create_Tag(db=db, tag=tag)


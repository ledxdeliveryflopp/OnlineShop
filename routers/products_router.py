from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database.database import engine, SessionLocal
from models import products_model
from schemas.products_schemas import ProductSchemas, ProductAdminSchemas, ProductCreateSchemas
from crud.products_crud import get_product, create_product, get_product_by_title
from crud.tags_crud import get_tag_by_id

products_model.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/products",
    tags=["products"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/list/",  response_model=list[ProductSchemas])
def get_products(limit: int | None = None, db: Session = Depends(get_db)):
    products = get_product(db, limit=limit)
    return products


@router.get("/list/admin/",  response_model=list[ProductAdminSchemas])
def get_products_admin(limit: int | None = None, db: Session = Depends(get_db)):
    products = get_product(db, limit=limit)
    return products


@router.post("/create/", response_model=ProductSchemas)
def add_products(tag_id: Annotated[int, Query(alias="tag id", description="id тега")],
                 product: ProductCreateSchemas, db: Session = Depends(get_db)):
    products = get_product_by_title(db, title=product.title)
    tags = get_tag_by_id(db, tag_id=tag_id)
    if products:
        raise HTTPException(status_code=400, detail="Такой товар есть")
    if not tags:
        raise HTTPException(status_code=404, detail="Такого тега нет")
    return create_product(db=db, product=product, tag_id=tag_id)



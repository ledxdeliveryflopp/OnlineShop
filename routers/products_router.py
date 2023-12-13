from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import engine, SessionLocal
from models import products_model
from schemas.products_schemas import ProductResponseSchemas, ProductCreateSchemas
from crud.products_crud import get_product, create_product, get_product_by_title
from crud.tags_crud import get_tag_by_id

products_model.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/list/",  response_model=list[ProductResponseSchemas])
def get_products(limit: int | None = None, db: Session = Depends(get_db)):
    products = get_product(db, limit=limit)
    if not products:
        raise  HTTPException(status_code=404, detail="Товаров нет")
    return products


@router.post("/create/", response_model=ProductResponseSchemas)
def add_products(product: ProductCreateSchemas, db: Session = Depends(get_db)):
    products = get_product_by_title(db, title=product.title)
    tags = get_tag_by_id(db, tag_id=product.tags_id)
    if products:
        raise HTTPException(status_code=400, detail="Такой товар есть")
    if not tags:
        raise HTTPException(status_code=404, detail="Такого тега нет")
    return create_product(db=db, product=product)



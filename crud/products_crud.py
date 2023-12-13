from sqlalchemy.orm import Session
from models.products_model import Product
from schemas.products_schemas import ProductCreateSchemas


def get_product(db: Session, limit: int = 100):
    return db.query(Product).limit(limit).all()


def get_product_by_title(db: Session, title: str):
    return db.query(Product).filter(Product.title == title).first()


def create_product(db: Session, product: ProductCreateSchemas):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

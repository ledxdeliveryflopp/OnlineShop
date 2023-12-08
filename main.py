from fastapi import FastAPI
from routers import products_router, tags_router
from database.database import engine
from models.products_model import Product

shop = FastAPI(title="Shop", description="Pet project", version="1.0")

shop.include_router(products_router.router)
shop.include_router(tags_router.router)


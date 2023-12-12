from fastapi import FastAPI
from routers import products_router, tags_router
from database.database import engine
from models.products_model import Product, Tag
from starlette_admin.contrib.sqla import Admin, ModelView

shop = FastAPI(title="Shop", description="Pet project", version="1.0")

shop.include_router(products_router.router)
shop.include_router(tags_router.router)

admin = Admin(engine, title="Example: SQLAlchemy")

admin.add_view(ModelView(Product))
admin.add_view(ModelView(Tag))

admin.mount_to(shop)

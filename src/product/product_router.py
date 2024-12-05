from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import select
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .product_models import Products
from .product_shema import ProductCreate, ProductPydantic
from ..db import get_session


app = APIRouter(prefix="/products", tags=["Products"])

templates = Jinja2Templates(directory="src/templates")

#создание счёта
# @app.post("/", response_class=HTMLResponse)
# def create_product(request: Request, product_create: ProductCreate, session: Session = Depends(get_session)):
#     product = Products(name=product_create.name, price=product_create.price, description=product_create.description)
#     session.add(product)
#     session.commit()
#     session.refresh(product)
#     return product

# получение сведений о всех счетах пользователя
@app.get("/", response_class=HTMLResponse)
def list_products(request: Request, session: Session = Depends(get_session)):
    products = session.scalars(Products).all()
    context = {
        "request": request,
        "titel": "Продукты",
        "products": products
    }
    return templates.TemplateResponse("index.html", context=context)
    # for i in all_products:
    #     product_pydantic = ProductPydantic.from_orm(i)
    #     print(product_pydantic.model_dump())

# получение сведений о продукте по его id
# @app.get("/{product_id}", response_model=float, response_class=HTMLResponse)
# def get_balance(request: Request, product_id: int, session: Session = Depends(get_session)):
#     product = session.scalar(select(Products).filter(Products.id == product_id))
#     context = {
#         "request": request,
#         "titel": "Продукты"
#     }
#     return templates.TemplateResponse("index.html", context=context)
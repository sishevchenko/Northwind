from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers import Controller
from src.db import get_async_session
from src.products.models import Products
from src.products.schemas import ProductsCreate, ProductsUpdate

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/get_all")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Products, session=session)


@router.get("/get/{pk}")
async def get_one(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Products, pk_attribute=Products.product_id, pk=pk, session=session)


@router.post("/create", response_model=ProductsCreate)
async def create(new_stmt: ProductsCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Products, pk_attribute=Products.product_id,
                                   value=new_stmt, session=session)


@router.post("/update", response_model=ProductsUpdate)
async def update(new_stmt: ProductsUpdate, session: AsyncSession = Depends(get_async_session)):
    return Controller.update(table_name=Products, pk_attribute=Products.product_id, value=new_stmt,
                             session=session)


@router.delete("/delete")
async def delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Products, pk_attribute=Products.product_id, pk=pk, session=session)


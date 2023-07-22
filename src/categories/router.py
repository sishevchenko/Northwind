from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.categories.models import Categories
from src.categories.schemas import CategoriesCreate, CategoriesUpdate
from src.controllers import Controller
from src.db import get_async_session

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/get_all")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Categories, session=session)


@router.get("/get/{pk}")
async def get_one(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Categories, pk_attribute=Categories.category_id, pk=pk, session=session)


@router.post("/create")
async def create(new_stmt: CategoriesCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Categories, pk_attribute=Categories.category_id.key,
                                   value=new_stmt, session=session)


@router.post("/update")
async def update(new_stmt: CategoriesUpdate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.update(table_name=Categories, pk_attribute=Categories.category_id, value=new_stmt,
                                   session=session)


@router.delete("/delete")
async def delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Categories, pk_attribute=Categories.category_id, pk=pk, session=session)

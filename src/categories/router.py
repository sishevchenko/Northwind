from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.categories.models import Categories
from src.categories.schemas import CategoriesCreate
from src.controllers import Controller
from src.db import get_async_session

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/")
async def get_all_categories(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Categories, session=session)


@router.get("/{pk}")
async def get_category(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Categories, pk_attribute=Categories.category_id, pk=pk, session=session)


@router.post("/")
async def categories_create(new_categories: CategoriesCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Categories, pk_attribute=Categories.category_id,
                                   value=new_categories, session=session)


@router.delete("/")
async def categories_delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Categories, pk_attribute=Categories.category_id, pk=pk, session=session)

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.products.models import Products

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
async def get_all_products(session: AsyncSession = Depends(get_async_session)):
    query = select(Products)
    res = await session.execute(query)
    return res.scalars().all()

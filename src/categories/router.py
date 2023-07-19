from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.categories.models import Categories
from src.db import get_async_session

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/")
async def get_all_categories(session: AsyncSession = Depends(get_async_session)):
    query = select(Categories)
    res = await session.execute(query)
    return res.scalars().all()

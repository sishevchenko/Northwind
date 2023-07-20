from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.shippers.models import Shippers

router = APIRouter(
    prefix="/shippers",
    tags=["Shippers"]
)


@router.get("/")
async def get_all_shippers(session: AsyncSession = Depends(get_async_session)):
    query = select(Shippers)
    res = await session.execute(query)
    return res.scalars().all()

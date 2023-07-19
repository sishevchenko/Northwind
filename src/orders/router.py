from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.orders.models import Orders

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


async def get_all_orders(session: AsyncSession = Depends(get_async_session)):
    query = select(Orders)
    res = await session.execute(query)
    return res.scalars().all()

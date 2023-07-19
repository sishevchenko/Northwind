from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.customers.models import Customers
from src.db import get_async_session

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("/")
async def get_all_customers(session: AsyncSession = Depends(get_async_session)):
    query = select(Customers)
    res = await session.execute(query)
    return res.scalars().all()

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.suppliers.models import Suppliers

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)


@router.get("/")
async def get_all_suppliers(session: AsyncSession = Depends(get_async_session)):
    query = select(Suppliers)
    res = await session.execute(query)
    return res.scalars().all()

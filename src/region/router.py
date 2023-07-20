from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.region.models import Region

router = APIRouter(
    prefix="/region",
    tags=["Region"]
)


@router.get("/")
async def get_all_region(session: AsyncSession = Depends(get_async_session)):
    query = select(Region)
    res = await session.execute(query)
    return res.scalars().all()

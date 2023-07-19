from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.employees.models import Employees

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/")
async def get_all_employees(session: AsyncSession = Depends(get_async_session)):
    query = select(Employees)
    employees = await session.execute(query)
    return employees.scalars().all()

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers import Controller
from src.db import get_async_session
from src.region.models import Region
from src.region.schemas import RegionCreate, RegionUpdate

router = APIRouter(
    prefix="/region",
    tags=["Region"]
)


@router.get("/get_all")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Region, session=session)


@router.get("/get/{pk}")
async def get_one(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Region, pk_attribute=Region.region_id, pk=pk, session=session)


@router.post("/create")
async def create(new_stmt: RegionCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Region, pk_attribute=Region.region_id.key,
                                   value=new_stmt, session=session)


@router.post("/update")
async def update(new_stmt: RegionUpdate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.update(table_name=Region, pk_attribute=Region.region_id, value=new_stmt,
                                   session=session)


@router.delete("/delete")
async def delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Region, pk_attribute=Region.region_id, pk=pk, session=session)

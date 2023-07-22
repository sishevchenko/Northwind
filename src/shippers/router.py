from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers import Controller
from src.db import get_async_session
from src.shippers.models import Shippers
from src.shippers.schemas import ShippersCreate, ShippersUpdate

router = APIRouter(
    prefix="/shippers",
    tags=["Shippers"]
)


@router.get("/get_all")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Shippers, session=session)


@router.get("/get/{pk}")
async def get_one(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Shippers, pk_attribute=Shippers.shipper_id, pk=pk, session=session)


@router.post("/create")
async def create(new_stmt: ShippersCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Shippers, pk_attribute=Shippers.shipper_id.key,
                                   value=new_stmt, session=session)


@router.post("/update")
async def update(new_stmt: ShippersUpdate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.update(table_name=Shippers, pk_attribute=Shippers.shipper_id, value=new_stmt,
                                   session=session)


@router.delete("/delete")
async def delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Shippers, pk_attribute=Shippers.shipper_id, pk=pk, session=session)

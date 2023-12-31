from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers import Controller
from src.db import get_async_session
from src.order_details.models import OrderDetails
from src.order_details.schemas import OrderDetailsCreate, OrderDetailsUpdate

router = APIRouter(
    prefix="/order_details",
    tags=["Order Details"]
)


@router.get("/get_all")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=OrderDetails, session=session)


@router.get("/get/{pk}")
async def get_one(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=OrderDetails, pk_attribute=OrderDetails.order_id, pk=pk, session=session)


@router.post("/create")
async def create(new_stmt: OrderDetailsCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=OrderDetails, value=new_stmt, session=session)


@router.post("/update")
async def update(new_stmt: OrderDetailsUpdate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.update(table_name=OrderDetails, pk_attribute=OrderDetails.order_id, value=new_stmt,
                                   session=session)


@router.delete("/delete")
async def delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=OrderDetails, pk_attribute=OrderDetails.order_id, pk=pk, session=session)

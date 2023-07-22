from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers import Controller
from src.db import get_async_session
from src.orders.models import Orders
from src.orders.schemas import OrdersCreate, OrdersUpdate

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/get_all")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Orders, session=session)


@router.get("/get/{pk}")
async def get_one(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Orders, pk_attribute=Orders.order_id, pk=pk, session=session)


@router.post("/create")
async def create(new_stmt: OrdersCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Orders, pk_attribute=Orders.order_id.key,
                                   value=new_stmt, session=session)


@router.post("/update")
async def update(new_stmt: OrdersUpdate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.update(table_name=Orders, pk_attribute=Orders.order_id, value=new_stmt,
                                   session=session)


@router.delete("/delete")
async def delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Orders, pk_attribute=Orders.order_id, pk=pk, session=session)

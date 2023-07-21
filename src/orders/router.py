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
async def get_all_categories(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Orders, session=session)


@router.get("/get/{pk}")
async def get_category(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Orders, pk_attribute=Orders.order_id, pk=pk, session=session)


@router.post("/create", response_model=OrdersCreate)
async def categories_create(new_stmt: OrdersCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Orders, pk_attribute=Orders.order_id,
                                   value=new_stmt, session=session)


@router.post("/update", response_model=OrdersUpdate)
async def categories_update(new_stmt: OrdersUpdate, session: AsyncSession = Depends(get_async_session)):
    return Controller.update(table_name=Orders, pk_attribute=Orders.order_id, value=new_stmt,
                             session=session)


@router.delete("/delete")
async def categories_delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Orders, pk_attribute=Orders.order_id, pk=pk, session=session)

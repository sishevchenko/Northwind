from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.customers.models import Customers
from src.db import get_async_session
from src.controllers import Controller
from src.customers.schemas import CustomersCreate, CustomersUpdate

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("/get_all")
async def get_all_categories(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Customers, session=session)


@router.get("/get/{pk}")
async def get_category(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Customers, pk_attribute=Customers.customer_id, pk=pk, session=session)


@router.post("/create", response_model=CustomersCreate)
async def categories_create(new_stmt: CustomersCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Customers, pk_attribute=Customers.customer_id.key,
                                   value=new_stmt, session=session)


@router.post("/update", response_model=CustomersUpdate)
async def categories_update(new_stmt: CustomersUpdate, session: AsyncSession = Depends(get_async_session)):
    return Controller.update(table_name=Customers, pk_attribute=Customers.customer_id, value=new_stmt,
                             session=session)


@router.delete("/delete")
async def categories_delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Customers, pk_attribute=Customers.customer_id, pk=pk, session=session)

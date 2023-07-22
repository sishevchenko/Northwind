from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers import Controller
from src.db import get_async_session
from src.suppliers.models import Suppliers
from src.suppliers.schemas import SuppliersCreate, SuppliersUpdate

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)


@router.get("/get_all")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Suppliers, session=session)


@router.get("/get/{pk}")
async def get_one(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Suppliers, pk_attribute=Suppliers.supplier_id, pk=pk, session=session)


@router.post("/create")
async def create(new_stmt: SuppliersCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Suppliers, pk_attribute_key=Suppliers.supplier_id.key,
                                   value=new_stmt, session=session)


@router.post("/update")
async def update(new_stmt: SuppliersUpdate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.update(table_name=Suppliers, pk_attribute=Suppliers.supplier_id, value=new_stmt,
                                   session=session)


@router.delete("/delete")
async def delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Suppliers, pk_attribute=Suppliers.supplier_id, pk=pk, session=session)

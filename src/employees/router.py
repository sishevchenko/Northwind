from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers import Controller
from src.db import get_async_session
from src.employees.models import Employees
from src.employees.schemas import EmployeesCreate, EmployeesUpdate

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/get_all")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_all(table_name=Employees, session=session)


@router.get("/get/{pk}")
async def get_one(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.get_one(table_name=Employees, pk_attribute=Employees.employee_id, pk=pk, session=session)


@router.post("/create")
async def create(new_stmt: EmployeesCreate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.create(table_name=Employees, pk_attribute=Employees.employee_id.key,
                                   value=new_stmt, session=session)


@router.post("/update")
async def update(new_stmt: EmployeesUpdate, session: AsyncSession = Depends(get_async_session)):
    return await Controller.update(table_name=Employees, pk_attribute=Employees.employee_id, value=new_stmt,
                             session=session)


@router.delete("/delete")
async def delete(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await Controller.delete(table_name=Employees, pk_attribute=Employees.employee_id, pk=pk, session=session)

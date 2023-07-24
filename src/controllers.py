from fastapi import HTTPException
from sqlalchemy import func, select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta, Mapped
from pydantic import BaseModel


class Controller:
    """
    CRUD operations controllers
    methods:
    get_one, get_all, create, update, delete
    """

    @staticmethod
    async def get_one(table_name: DeclarativeMeta, pk_attribute: Mapped, pk: int | str, session: AsyncSession):
        """Returns the element of the table whose pk is equal to the given one"""
        try:
            query = select(table_name).where(pk_attribute == pk)
            obj = await session.execute(query)
            return obj.scalars().all()
        except Exception as ex:
            raise HTTPException(status_code=200, detail={
                "status": "error",
                "data": None,
                "details": ex
            })

    @staticmethod
    async def get_all(table_name: DeclarativeMeta, session: AsyncSession):
        """Returns all fields of objects of the passed table"""
        try:
            query = select(table_name)
            obj = await session.execute(query)
            return obj.scalars().all()
        except Exception as ex:
            raise HTTPException(status_code=200, detail={
                "status": "error",
                "data": None,
                "details": ex
            })

    @staticmethod
    async def create(table_name: DeclarativeMeta, value: BaseModel, session: AsyncSession,
                     pk_attribute_key: str | None = None) -> dict:
        """Creates a new record in the table.
        When passing the pk_attribute_key parameter, it autogenerate a new pk"""
        try:
            new_obj = value.model_dump()
            if isinstance(pk_attribute_key, str):
                last_id = select(func.count()).select_from(table_name)
                count = await session.execute(last_id)
                new_obj[pk_attribute_key] = count.scalar() + 1
            stmt = insert(table_name).values(**new_obj).returning(table_name)
            obj = await session.execute(stmt)
            await session.commit()
            return dict(status_code=201, obj=obj.scalar())
        except Exception as ex:
            raise HTTPException(status_code=200, detail={
                "status": "error",
                "data": None,
                "details": ex
            })

    @staticmethod
    async def update(table_name: DeclarativeMeta, pk_attribute: Mapped, value: BaseModel,
                     session: AsyncSession) -> dict:
        """Performs an update of the entry specified in pk_attribute"""
        try:
            new_obj = value.model_dump()
            stmt = update(table_name).where(pk_attribute == new_obj[pk_attribute.key]).values(**new_obj).returning(
                table_name)
            obj = await session.execute(stmt)
            await session.commit()
            return dict(status_code=201, obj=obj.scalar())
        except Exception as ex:
            raise HTTPException(status_code=200, detail={
                "status": "error",
                "data": None,
                "details": ex
            })

    @staticmethod
    async def delete(table_name: DeclarativeMeta, pk_attribute: Mapped, pk: int,
                     session: AsyncSession) -> dict:
        """Removes the entry specified by pk"""
        try:
            stmt = delete(table_name).where(pk_attribute == pk).returning(table_name)
            obj = await session.execute(stmt)
            await session.commit()
            return dict(status_code=201, obj=obj.scalar())
        except Exception as ex:
            raise HTTPException(status_code=200, detail={
                "status": "error",
                "data": None,
                "details": ex
            })

from fastapi import HTTPException
from sqlalchemy import func, select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, DeclarativeMeta, Mapped
from pydantic import BaseModel


class Controller:
    """"""

    @staticmethod
    async def get_one(table_name: DeclarativeMeta, pk_attribute: Mapped, pk: int, session: Session | AsyncSession):
        """"""
        try:
            query = select(table_name).where(pk_attribute == pk)
            res = await session.execute(query)
            return res.scalars().all()
        except Exception as ex:
            raise HTTPException(status_code=200, detail={
                "status": "error",
                "data": None,
                "details": ex
            })

    @staticmethod
    async def get_all(table_name: DeclarativeMeta, session: Session | AsyncSession):
        """"""
        try:
            query = select(table_name)
            res = await session.execute(query)
            return res.scalars().all()
        except Exception as ex:
            raise HTTPException(status_code=200, detail={
                "status": "error",
                "data": None,
                "details": ex
            })

    @staticmethod
    async def create(table_name: DeclarativeMeta, value: BaseModel, session: Session | AsyncSession,
                     pk_attribute_key: str | None = None) -> dict:
        """"""
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
                     session: Session | AsyncSession) -> dict:
        """"""
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
                     session: Session | AsyncSession) -> dict:
        """"""
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

from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta


class Shippers(BaseMeta):
    __tablename__ = "shippers"

    shipper_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, nullable=False)
    company_name: Mapped[str] = mapped_column(String(length=40), nullable=False)
    phone: Mapped[str] = mapped_column(String(length=24), nullable=True)

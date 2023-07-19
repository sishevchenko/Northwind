from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta


class Customers(BaseMeta):
    __tablename__ = "customers"

    customer_id: Mapped[str] = mapped_column(String(length=5), primary_key=True, nullable=False)
    company_name: Mapped[str] = mapped_column(String(length=40), nullable=False)
    contact_name: Mapped[str] = mapped_column(String(length=30), nullable=True)
    contact_title: Mapped[str] = mapped_column(String(length=30), nullable=True)
    address: Mapped[str] = mapped_column(String(length=60), nullable=True)
    city: Mapped[str] = mapped_column(String(length=15), nullable=True)
    region: Mapped[str] = mapped_column(String(length=15), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(length=10), nullable=True)
    country: Mapped[str] = mapped_column(String(length=15), nullable=True)
    phone: Mapped[str] = mapped_column(String(length=24), nullable=True)
    fax: Mapped[str] = mapped_column(String(length=24), nullable=True)

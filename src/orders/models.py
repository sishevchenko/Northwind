from datetime import date

from sqlalchemy import SmallInteger, String, DATE, REAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta
from src.customers.models import Customers
from src.employees.models import Employees
from src.products.models import Products


class Orders(BaseMeta):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, nullable=False)
    customer_id: Mapped[str] = mapped_column(ForeignKey(Customers.customer_id, ondelete="CASCADE"), nullable=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey(Employees.employee_id, ondelete="CASCADE"), nullable=True)
    order_date: Mapped[date] = mapped_column(DATE, nullable=True)
    required_date: Mapped[date] = mapped_column(DATE, nullable=True)
    shipped_date: Mapped[date] = mapped_column(DATE, nullable=True)
    ship_via: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    freight: Mapped[float] = mapped_column(REAL, nullable=True)
    ship_name: Mapped[str] = mapped_column(String(length=40), nullable=True)
    ship_address: Mapped[str] = mapped_column(String(length=60), nullable=True)
    ship_city: Mapped[str] = mapped_column(String(length=15), nullable=True)
    ship_region: Mapped[str] = mapped_column(String(length=15), nullable=True)
    ship_postal_code: Mapped[str] = mapped_column(String(length=10), nullable=True)
    ship_country: Mapped[str] = mapped_column(String(length=15), nullable=True)


class OrderDetails(BaseMeta):
    __tablename__ = "order_details"

    order_id: Mapped[int] = mapped_column(ForeignKey(Orders.order_id, ondelete="CASCADE"), primary_key=True,
                                          nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey(Products.product_id, ondelete="CASCADE"), primary_key=True,
                                            nullable=False)
    unit_price: Mapped[float] = mapped_column(REAL, nullable=False)
    quantity: Mapped[float] = mapped_column(SmallInteger, nullable=False)
    discount: Mapped[float] = mapped_column(REAL, nullable=False)

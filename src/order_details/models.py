from sqlalchemy import SmallInteger, REAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta
from src.orders.models import Orders
from src.products.models import Products


class OrderDetails(BaseMeta):
    __tablename__ = "order_details"

    order_id: Mapped[int] = mapped_column(ForeignKey(Orders.order_id, ondelete="CASCADE"), primary_key=True,
                                          nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey(Products.product_id, ondelete="CASCADE"), primary_key=True,
                                            nullable=False)
    unit_price: Mapped[float] = mapped_column(REAL, nullable=False)
    quantity: Mapped[float] = mapped_column(SmallInteger, nullable=False)
    discount: Mapped[float] = mapped_column(REAL, nullable=False)

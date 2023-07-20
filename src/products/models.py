from sqlalchemy import SmallInteger, ForeignKey, String, REAL, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.categories.models import Categories
from src.db import BaseMeta
from src.suppliers.models import Suppliers


class Products(BaseMeta):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, nullable=False)
    product_name: Mapped[str] = mapped_column(String(length=40), nullable=False)
    supplier_id: Mapped[int] = mapped_column(ForeignKey(Suppliers.supplier_id, ondelete="CASCADE"), nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey(Categories.category_id, ondelete="CASCADE"), nullable=True)
    quantity_per_unit: Mapped[str] = mapped_column(String(length=20), nullable=True)
    unit_price: Mapped[float] = mapped_column(REAL, nullable=True)
    units_in_stock: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    units_on_order: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    reorder_level: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    discontinued: Mapped[int] = mapped_column(Integer, nullable=False)

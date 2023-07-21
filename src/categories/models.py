from sqlalchemy import SmallInteger, String, TEXT, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta


class Categories(BaseMeta):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, nullable=False)
    category_name: Mapped[str] = mapped_column(String(length=15), nullable=False)
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
    picture: Mapped[bytes] = mapped_column(LargeBinary, nullable=True)

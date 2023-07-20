from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta


class Region(BaseMeta):
    __tablename__ = "region"

    region_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, nullable=False)
    region_description: Mapped[str] = mapped_column(String, nullable=False)

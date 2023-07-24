import uuid

from sqlalchemy import UUID, String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta


class UserType(BaseMeta):
    pass


class User(BaseMeta):
    __tablename__ = "users"

    user_id: Mapped[uuid] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), nullable=False)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    phone_number: Mapped[int] = mapped_column(Integer)
    is_activ: Mapped[bool] = mapped_column(Boolean, default=True)

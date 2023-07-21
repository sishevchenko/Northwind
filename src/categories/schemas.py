from pydantic import BaseModel
from typing_extensions import Any


class CategoriesCreate(BaseModel):
    category_name: str
    description: str | None
    picture: bytes | None

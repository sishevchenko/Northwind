from typing import Optional

from pydantic import BaseModel


class CategoriesCreate(BaseModel):
    category_name: str
    description: Optional[str] = None
    picture: Optional[bytes] = None


class CategoriesUpdate(BaseModel):
    id: int
    category_name: Optional[str]
    description: Optional[str]
    picture: Optional[bytes]

from pydantic import BaseModel


class CategoriesCreate(BaseModel):
    category_name: str
    description: str | None
    picture: bytes | None


class CategoriesUpdate(BaseModel):
    id: int
    category_name: str
    description: str | None
    picture: bytes | None

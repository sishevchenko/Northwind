from pydantic import BaseModel


class CategoriesCreate(BaseModel):
    category_name: str
    description: str | None
    picture: bytes | None

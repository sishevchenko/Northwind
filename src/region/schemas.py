from typing import Optional

from pydantic import BaseModel


class RegionCreate(BaseModel):
    region_id: int
    region_description: str


class RegionUpdate(BaseModel):
    region_id: int
    region_description: Optional[str]

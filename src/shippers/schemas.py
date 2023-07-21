from typing import Optional

from pydantic import BaseModel


class ShippersCreate(BaseModel):
    company_name: str
    phone: Optional[str | None] = None


class ShippersUpdate(BaseModel):
    shipper_id: int
    company_name: Optional[str | None]
    phone: Optional[str | None]

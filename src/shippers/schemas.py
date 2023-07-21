from typing import Optional

from pydantic import BaseModel


class ShippersCreate(BaseModel):
    company_name: str
    phone: Optional[str] = None


class ShippersUpdate(BaseModel):
    shipper_id: int
    company_name: Optional[str]
    phone: Optional[str]

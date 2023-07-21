from typing import Optional

from pydantic import BaseModel


class SuppliersCreate(BaseModel):
    company_name: str
    contact_name: Optional[str | None] = None
    contact_title: Optional[str | None] = None
    address: Optional[str | None] = None
    city: Optional[str | None] = None
    region: Optional[str | None] = None
    postal_code: Optional[str | None] = None
    country: Optional[str | None] = None
    phone: Optional[str | None] = None
    fax: Optional[str | None] = None
    homepage: Optional[str | None] = None


class SuppliersUpdate(BaseModel):
    supplier_id: int
    company_name: str
    contact_name: Optional[str | None]
    contact_title: Optional[str | None]
    address: Optional[str | None]
    city: Optional[str | None]
    region: Optional[str | None]
    postal_code: Optional[str | None]
    country: Optional[str | None]
    phone: Optional[str | None]
    fax: Optional[str | None]
    homepage: Optional[str | None]

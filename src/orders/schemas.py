from datetime import date
from typing import Optional

from pydantic import BaseModel


class OrdersCreate(BaseModel):
    customer_id: str
    employee_id: int
    order_date: date = date.today()
    required_date: date = date.today()
    shipped_date: date = date.today()
    ship_via: Optional[int | None] = None
    freight: Optional[float | None] = None
    ship_name: Optional[str | None] = None
    ship_address: Optional[str | None] = None
    ship_city: Optional[str | None] = None
    ship_region: Optional[str | None] = None
    ship_postal_code: Optional[str | None] = None
    ship_country: Optional[str | None] = None


class OrdersUpdate(BaseModel):
    order_id: int
    customer_id: str
    employee_id: int
    order_date: date = date.today()
    required_date: date = date.today()
    shipped_date: date = date.today()
    ship_via: Optional[int | None]
    freight: Optional[float | None]
    ship_name: Optional[str | None]
    ship_address: Optional[str | None]
    ship_city: Optional[str | None]
    ship_region: Optional[str | None]
    ship_postal_code: Optional[str | None]
    ship_country: Optional[str | None]

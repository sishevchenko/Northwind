from typing import Optional

from pydantic import BaseModel


class OrderDetailsCreate(BaseModel):
    order_id: int
    product_id: int
    unit_price: float
    quantity: float
    discount: float


class OrderDetailsUpdate(BaseModel):
    order_id: int
    product_id: int
    unit_price: Optional[float]
    quantity: Optional[float]
    discount: Optional[float]

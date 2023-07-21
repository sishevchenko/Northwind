from typing import Optional

from pydantic import BaseModel, field_validator, ValidationError


class ProductsCreate(BaseModel):
    product_name: str
    supplier_id: int
    category_id: int
    quantity_per_unit: str
    unit_price: float
    units_in_stock: int
    units_on_order: int
    reorder_level: int
    discontinued: int

    @field_validator("category_id")
    def is_valid_category_id(cls, value):
        if value >= 0:
            return value
        raise ValidationError(f"id field {value} < 0")

    @field_validator("supplier_id")
    def is_valid_supplier_id(cls, value):
        if value >= 0:
            return value
        raise ValidationError(f"id field {value} < 0")


class ProductsUpdate(BaseModel):
    product_id: int
    product_name: Optional[str]
    supplier_id: Optional[int]
    category_id: Optional[int]
    quantity_per_unit: Optional[str]
    unit_price: Optional[float]
    units_in_stock: Optional[int]
    units_on_order: Optional[int]
    reorder_level: Optional[int]
    discontinued: Optional[int]

    @field_validator("product_id")
    def is_valid_product_id(cls, value):
        if value >= 0:
            return value
        raise ValidationError(f"id field {value} < 0")

    @field_validator("category_id")
    def is_valid_category_id(cls, value):
        if value >= 0:
            return value
        raise ValidationError(f"id field {value} < 0")

    @field_validator("supplier_id")
    def is_valid_supplier_id(cls, value):
        if value >= 0:
            return value
        raise ValidationError(f"id field {value} < 0")

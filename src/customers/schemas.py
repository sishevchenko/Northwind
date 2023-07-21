from typing import Optional

from pydantic import BaseModel, ValidationError, field_validator


class CustomersCreate(BaseModel):
    customer_id: str
    company_name: str
    contact_name: Optional[str] = None
    contact_title: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None

    @field_validator("phone")
    def is_valid_phone(cls, value: str):
        if value.startswith("+") and value[1:].isdigit() or value.isdigit():
            return value
        raise ValidationError(f"wrong phone number format: '{value}'")

    @field_validator("fax")
    def is_valid_fax(cls, value: str):
        if value.startswith("+") and value[1:].isdigit() or value.isdigit():
            return value
        raise ValidationError(f"wrong phone number format: '{value}'")


class CustomersUpdate(BaseModel):
    customer_id: str
    company_name: Optional[str]
    contact_name: Optional[str]
    contact_title: Optional[str]
    address: Optional[str]
    city: Optional[str]
    region: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    phone: Optional[str]
    fax: Optional[str]

    @field_validator("phone")
    def is_valid_phone(cls, value: str):
        if value.startswith("+") and value[1:].isdigit() or value.isdigit():
            return value
        raise ValidationError(f"wrong phone number format: '{value}'")

    @field_validator("fax")
    def is_valid_fax(cls, value: str):
        if value.startswith("+") and value[1:].isdigit() or value.isdigit():
            return value
        raise ValidationError(f"wrong phone number format: '{value}'")

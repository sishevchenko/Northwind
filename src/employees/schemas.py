from datetime import date
from typing import Optional

from pydantic import BaseModel


class EmployeesCreate(BaseModel):
    last_name: str
    first_name: str
    title: Optional[str | None] = None
    title_of_courtesy: Optional[str | None] = None
    birth_date: Optional[date | None] = None
    hire_date: Optional[date | None] = None
    address: Optional[str | None] = None
    city: Optional[str | None] = None
    region: Optional[str | None] = None
    postal_code: Optional[str | None] = None
    country: Optional[str | None] = None
    home_phone: Optional[str | None] = None
    extension: Optional[str | None] = None
    photo: Optional[bytes | None] = None
    notes: Optional[str | None] = None
    reports_to: Optional[int | None] = None
    photo_path: Optional[str | None] = None


class EmployeesUpdate(BaseModel):
    employee_id: int
    last_name: str
    first_name: str
    title: Optional[str | None]
    title_of_courtesy: Optional[str | None]
    birth_date: Optional[date | None]
    hire_date: Optional[date | None]
    address: Optional[str | None]
    city: Optional[str | None]
    region: Optional[str | None]
    postal_code: Optional[str | None]
    country: Optional[str | None]
    home_phone: Optional[str | None]
    extension: Optional[str | None]
    photo: Optional[bytes | None]
    notes: Optional[str | None]
    reports_to: Optional[int | None]
    photo_path: Optional[str | None]

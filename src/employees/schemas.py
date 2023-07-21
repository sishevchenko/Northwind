from datetime import date
from typing import Optional

from pydantic import BaseModel


class EmployeesCreate(BaseModel):
    last_name: str
    first_name: str
    title: Optional[str] = None
    title_of_courtesy: Optional[str] = None
    birth_date: Optional[date] = None
    hire_date: Optional[date] = None
    address: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    home_phone: Optional[str] = None
    extension: Optional[str] = None
    photo: Optional[bytes] = None
    notes: Optional[str] = None
    reports_to: Optional[int] = None
    photo_path: Optional[str] = None


class EmployeesUpdate(BaseModel):
    employee_id: int
    last_name: str
    first_name: str
    title: Optional[str]
    title_of_courtesy: Optional[str]
    birth_date: Optional[date]
    hire_date: Optional[date]
    address: Optional[str]
    city: Optional[str]
    region: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    home_phone: Optional[str]
    extension: Optional[str]
    photo: Optional[bytes]
    notes: Optional[str]
    reports_to: Optional[int]
    photo_path: Optional[str]

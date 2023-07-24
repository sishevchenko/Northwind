import uuid
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator


class UseRead(BaseModel):
    user_id: uuid
    name: str
    surname: str
    email: EmailStr
    phone_number: int
    is_activ: bool


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone_number: int

    @field_validator("phone_number")
    def is_valid_phone_number(cls, value: int):
        if len(str(value)) == 10:
            return value
        raise HTTPException(status_code=422,
                            detail="validation error: length phone_number don't equal 10")


class UserUpdate(BaseModel):
    user_id: uuid
    name: Optional[str]
    surname: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[int]

    @field_validator("phone_number")
    def is_valid_phone_number(cls, value: int):
        if len(str(value)) == 10:
            return value
        raise HTTPException(status_code=422,
                            detail="validation error: length phone_number don't equal 10")

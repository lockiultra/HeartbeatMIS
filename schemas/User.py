from pydantic import BaseModel, EmailStr, field_validator
from datetime import date
from validators import validate_phone_number, validate_birthday


class UserBase(BaseModel):
    first_name: str
    second_name: str
    third_name: str | None = None
    birthday: date
    phone_number: str
    email: EmailStr

    @field_validator('phone_number')
    @classmethod
    def __validate_phone_number(cls, value: str) -> str:
        return validate_phone_number(value)
    
    # @field_validator('birthday')
    # @classmethod
    # def __validate_birthday(cls, value: str) -> str:
    #     return validate_birthday(value)
    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    first_name: str | None = None
    second_name: str | None = None
    third_name: str | None = None
    birthday: date | None = None
    phone_number: str | None = None
    email: EmailStr | None = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True 

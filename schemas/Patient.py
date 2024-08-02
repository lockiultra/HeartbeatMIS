from schemas.User import User, UserBase, UserCreate, UserUpdate
from pydantic import field_validator, ValidationError


class PatientBase(UserBase):
    insurance: str
    passport: str

    @field_validator('insurance')
    @classmethod
    def validate_insurance(cls, value: str) -> str:
        if len(value) != 16 or not sum([val.isdigit() for val in value]):
            raise ValidationError('Неправильный номер страхования')
        return value
    
    @field_validator('passport')
    @classmethod
    def validate_passport(cls, value: str) -> str:
        if len(value) != 10 or not sum([val.isdigit() for val in value]):
            raise ValidationError('Неправильные паспортные данные')
        return value

class PatientCreate(UserCreate, PatientBase):
    pass

class PatientUpdate(UserUpdate, PatientBase):
    insurance: str | None = None
    passport: str | None = None

class Patient(User, PatientBase):
    pass
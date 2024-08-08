from pydantic import ValidationError
import re
from datetime import date, datetime


def validate_phone_number(number: str) -> str:
    if not re.match(r"^\+\d{1,15}$", number):
        raise ValidationError("Incorrect phone number")
    return number


def validate_birthday(birthday: date) -> date:
    if birthday and birthday > datetime.now().time():
        raise ValidationError("Incorrect birthday")
    return birthday

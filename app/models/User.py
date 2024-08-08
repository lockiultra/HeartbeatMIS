from sqlalchemy.orm import Mapped, mapped_column
from datetime import date


class User:
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    second_name: Mapped[str]
    third_name: Mapped[str | None]
    birthday: Mapped[date]
    phone_number: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
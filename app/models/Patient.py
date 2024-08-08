from app.models.Base import Base
from app.models.User import User
from sqlalchemy.orm import Mapped


class Patient(Base, User):
    __tablename__ = "patients"

    insurance: Mapped[str]
    passport: Mapped[str]

from app.models.Base import Base
from app.models.User import User
from sqlalchemy.orm import Mapped


class Doctor(Base, User):
    __tablename__ = "doctors"

    expirience: Mapped[int]
    speciality: Mapped[str]

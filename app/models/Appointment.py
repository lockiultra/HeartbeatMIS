# from models.Base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
import app.models as models


class Appoinment(models.Base):
    __tablename__ = 'appointments'

    id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey('doctors.id'))
    patient_id: Mapped[int] = mapped_column(ForeignKey('patients.id'))
    datetime: datetime

    doctor_owner: Mapped[models.Doctor] = relationship(models.Doctor, back_populates=models.Doctor.appointments)
    patient_owner: Mapped[models.Patient] = relationship(models.Patient, back_populates=models.Patient.appointments)
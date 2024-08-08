from fastapi import APIRouter, Depends, Body
import app.models as models
import app.schemas as schemas
from app.db import get_db
from sqlalchemy.orm import Session


doctors_router = APIRouter()


@doctors_router.get("/", response_model=list[schemas.Doctor])
def get_all_doctors(db: Session = Depends(get_db)):
    doctors = db.query(models.Doctor).all()
    return doctors


@doctors_router.post("/", response_model=schemas.Doctor)
def add_new_doctor(
    doctor: schemas.DoctorCreate = Body(), db: Session = Depends(get_db)
):
    new_doctor = models.Doctor()
    for key, value in doctor.model_dump().items():
        setattr(new_doctor, key, value)
    db.add(new_doctor)
    db.commit()
    return new_doctor


@doctors_router.put("/{doctor_id}", response_model=schemas.Doctor)
def update_doctor(
    doctor_id: int, doctor: schemas.DoctorUpdate = Body(), db: Session = Depends(get_db)
):
    doctor_to_update = (
        db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    )
    for key, value in doctor.model_dump().items():
        setattr(doctor_to_update, key, value)
    db.commit()
    db.refresh()
    return doctor_to_update

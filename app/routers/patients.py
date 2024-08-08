from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.db import get_db
import app.models as models
import app.schemas as schemas


patients_router = APIRouter()


@patients_router.get("/", response_model=list[schemas.Patient])
def get_all_pacients(db: Session = Depends(get_db)):
    response = db.query(models.Patient).all()
    return response


@patients_router.get("/{patient_id}", response_model=schemas.Patient)
def get_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    return patient


@patients_router.post("/", response_model=schemas.Patient)
def add_new_patient(
    patient: schemas.PatientCreate = Body(), db: Session = Depends(get_db)
):
    new_patient = models.Patient()
    for key, value in patient.model_dump().items():
        setattr(new_patient, key, value)
    db.add(new_patient)
    db.commit()
    return new_patient


@patients_router.put("/{patient_id}", response_model=schemas.Patient)
def update_patient(
    patient_id: int,
    patient: schemas.PatientUpdate = Body(),
    db: Session = Depends(get_db),
):
    patient_to_update = (
        db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    )
    for key, value in patient.model_dump().items():
        setattr(patient_to_update, key, value)
    db.commit()
    db.refresh(patient_to_update)
    return patient_to_update

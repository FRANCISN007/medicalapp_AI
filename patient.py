from fastapi import APIRouter, HTTPException
from Schemas.patient import  Patient, patients


patient_router = APIRouter()


@patient_router.get("/patients")
async def get_patients():
    return patients

@patient_router.post("/create_patient")
async def post_create_patient(patient: Patient):
  patients.append(patient)
  return {"message":"Doctor account created successfully", "data":patient}



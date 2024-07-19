from fastapi import APIRouter, HTTPException, Response
from Schemas.doctor import doctors, Doctor


doctor_router = APIRouter()

@doctor_router.get("/doctors")
async def get_doctors():
    return doctors


#Endpoint to create more Doctors
@doctor_router.post("/create_doctor")
async def post_create_doctor(doctor: Doctor):
  doctors.append(doctor)
  return {"message":"Doctor account created successfully", "data":doctor}

@doctor_router.get("/doctors/{doctor_id}")
async def get_doctor(doctor_id: int):
    doctor = next((d for d in doctors if d.id == doctor_id), None)
    if doctor:
        return doctor
    else:
        return {"message": "Doctor not found"}, 404


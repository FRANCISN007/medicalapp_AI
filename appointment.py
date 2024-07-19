from fastapi import FastAPI, Body
from fastapi import APIRouter, HTTPException, Response
from Schemas.doctor import doctors, Doctor
from Schemas.appointment import appointments, Appointment


appointment_router = APIRouter()

@appointment_router.get("/appointments")
async def get_appointments():
    """
    List all Patient in Database
    """
    return appointments



@appointment_router.post("/book_appointment")
async def book_appointment(appointment: Appointment):
    """
    Book an appointment with a specified doctor.
    """
    doctor = next((d for d in doctors if d.name == appointment.doctor_name), None)
    if doctor and doctor.available:
        appointments.append(appointment)
        return {"message": "Appointment booked successfully"}
    else:
        return {"message": "Doctor is not available"}, 400
    
@appointment_router.get("/appointments/{patient_name}")
async def get_appointment(patient_name: str):
    """
    Sort Appointment with Patient Name.
    """
    appointment = next((a for a in appointments if a.patient_name == patient_name), None)
    if appointment:
        return appointment
    else:
        return {"message": "Appointment not found"}, 404
    

@appointment_router.delete("/appointments/{patient_name}")
async def cancel_appointment(patient_name: str):
    """
    Cancell Appointment with Patient Name
    """
    appointment = next((a for a in appointments if a.patient_name == patient_name), None)
    if appointment:
        appointments.remove(appointment)
        return {"message": "Appointment canceled successfully"}
    else:
        return {"message": "Appointment not found"}, 404

# Endpoint to update an appointment status
@appointment_router.put("/appointments/{patient_name}/status")
async def update_appointment_status(patient_name: str, status: str = Body(...)):
    """
    Update Appointment using Pateint Name
    """
    appointment = next((a for a in appointments if a.patient_name == patient_name), None)
    if appointment:
        appointment.status = status
        return {"message": "Appointment status updated successfully"}
    else:
        return {"message": "Appointment not found"}, 404   

from fastapi import FastAPI
from Routers.patient import patient_router
from Routers.doctor import doctor_router
from Routers.appointment import appointment_router


from typing import List, Optional


app = FastAPI()

app.include_router(patient_router, prefix ="/Patient", tags =["Patients"])
app.include_router(doctor_router, prefix ="/Doctor", tags = ["Doctors"])
app.include_router(appointment_router, prefix="/Appointment", tags= ["Appointment"])

@app.get('/home')
def index():
    return "WELCOME TO MY MEDICAL APPOINTMENT APPLICATION"





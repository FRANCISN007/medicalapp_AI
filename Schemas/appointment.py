from pydantic import BaseModel
from typing import Union
from typing import List, Optional


class Appointment(BaseModel):
    patient_name: str
    doctor_id: int
    doctor_name:str
    appointment_date: str
    status: str = "pending"

appointments: List[Appointment] = []

from pydantic import BaseModel
from typing import List, Optional

class Patient(BaseModel):
    name: str
    age: int
    sex: str
    weight_Kg: str
    height_Meter: str
    phone: str

patients: List[Patient] = []
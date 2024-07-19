from pydantic import BaseModel
from typing import Union
from typing import List, Optional

class Doctor(BaseModel):
    id: int
    name: str
    available: bool

doctors: List[Doctor] = [
    Doctor(id=1, name="Dr. Smith", available=True),
    Doctor(id=2, name="Dr. Johnson", available=False)  
]

from pydantic import BaseModel
#class lesson used in data validation in the file fastpitrial
class Lesson(BaseModel):
    id: int
    name: str
    Lecturer: str
    fees: float
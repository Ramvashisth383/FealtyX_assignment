# app/models.py

from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str

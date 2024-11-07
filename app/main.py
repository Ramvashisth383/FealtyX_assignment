# app/main.py

from fastapi import FastAPI, HTTPException
from app.models import Student
from app.crud import create_student, get_students, get_student_by_id, update_student, delete_student
from typing import List

app = FastAPI()

# In-memory student storage
students_db = {}

# Create a new student
@app.post("/students")
def create_new_student(student: Student):
    return create_student(student)

# Get all students
@app.get("/students", response_model=List[Student])
def read_students():
    return get_students()

# Get student by ID
@app.get("/students/{id}", response_model=Student)
def read_student(id: int):
    return get_student_by_id(id)

# Update a student by ID
@app.put("/students/{id}", response_model=Student)
def update_student_by_id(id: int, student: Student):
    return update_student(id, student)

# Delete a student by ID
@app.delete("/students/{id}")
def delete_student_by_id(id: int):
    return delete_student(id)

# app/main.py

from app.ollama_integration import generate_student_summary

@app.get("/students/{id}/summary")
def get_student_summary(id: int):
    student = get_student_by_id(id)
    summary = generate_student_summary(student)
    return summary

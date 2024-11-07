# app/crud.py

from app.models import Student
from fastapi import HTTPException

# In-memory database for students
students_db = {}

def create_student(student: Student):
    if student.id in students_db:
        raise HTTPException(status_code=400, detail="Student with this ID already exists")
    students_db[student.id] = student
    return student

def get_students():
    return list(students_db.values())

def get_student_by_id(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

def update_student(student_id: int, updated_student: Student):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    students_db[student_id] = updated_student
    return updated_student

def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": "Student deleted successfully"}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.m_students import Student
from schemas.s_students import StudentCreate, StudentResponse
from database import SessionLocal
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/api/students/", response_model=StudentResponse, tags=["Students"])
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@router.get("/api/students", response_model=List[StudentResponse], tags=["Students"])
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@router.get("/api/students/", response_model=List[StudentResponse], tags=["Students"])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.put("/api/students/{student_id}", response_model=StudentResponse, tags=["Students"])
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in student.dict().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/api/students/{student_id}", tags=["Students"])
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"msg": "Student deleted successfully"}

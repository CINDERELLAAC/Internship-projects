from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.m_instructors import Instructor
from schemas.s_instructors import InstructorCreate, InstructorResponse
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

@router.post("/api/instructors/", response_model=InstructorResponse, tags=["Instructors"])
def add_instructor(instructor: InstructorCreate, db: Session = Depends(get_db)):
    new_instructor = Instructor(**instructor.dict())
    db.add(new_instructor)
    db.commit()
    db.refresh(new_instructor)
    return new_instructor


@router.get("/api/instructors", response_model=List[InstructorResponse], tags=["Instructors"])
def get_all_instructors(db: Session = Depends(get_db)):
    instructors = db.query(Instructor).all()
    return instructors

@router.get("/api/instructors/", response_model=List[InstructorResponse], tags=["Instructors"])
def get_instructors(db: Session = Depends(get_db)):
    return db.query(Instructor).all()

@router.put("/api/instructors/{instructor_id}", response_model=InstructorResponse, tags=["Instructors"])
def update_instructor(instructor_id: int, instructor: InstructorCreate, db: Session = Depends(get_db)):
    db_instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    for key, value in instructor.dict().items():
        setattr(db_instructor, key, value)
    db.commit()
    db.refresh(db_instructor)
    return db_instructor

@router.delete("/api/instructors/{instructor_id}", tags=["Instructors"])
def delete_instructor(instructor_id: int, db: Session = Depends(get_db)):
    db_instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    db.delete(db_instructor)
    db.commit()
    return {"msg": "Instructor deleted successfully"}

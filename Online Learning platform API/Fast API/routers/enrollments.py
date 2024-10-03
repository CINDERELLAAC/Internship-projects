from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.m_enrollments import Enrollment
from schemas.s_enrollments import EnrollmentCreate, EnrollmentResponse
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

@router.post("/api/enrollments/", response_model=EnrollmentResponse, tags=["Enrollments"])
def add_enrollment(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    new_enrollment = Enrollment(**enrollment.dict())
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment


@router.get("/api/enrollments", response_model=List[EnrollmentResponse], tags=["Enrollments"])
def get_all_enrollments(db: Session = Depends(get_db)):
    enrollments = db.query(Enrollment).all()
    return enrollments

@router.get("/api/enrollments/", response_model=List[EnrollmentResponse], tags=["Enrollments"])
def get_enrollments(db: Session = Depends(get_db)):
    return db.query(Enrollment).all()

@router.put("/api/enrollments/{enrollment_id}", response_model=EnrollmentResponse, tags=["Enrollments"])
def update_enrollment(enrollment_id: int, enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    db_enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if db_enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    for key, value in enrollment.dict().items():
        setattr(db_enrollment, key, value)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

@router.delete("/api/enrollments/{enrollment_id}", tags=["Enrollments"])
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    db_enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if db_enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    db.delete(db_enrollment)
    db.commit()
    return {"msg": "Enrollment deleted successfully"}

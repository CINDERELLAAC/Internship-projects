from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.m_courses import Course
from schemas.s_courses import CourseCreate, CourseResponse, CourseBase
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/api/courses/", response_model=CourseResponse,tags=["Courses"])
def add_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


@router.get("/api/courses", response_model=list[CourseBase], tags=["Courses"])
def get_all_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses

@router.get("/api/courses/",tags=["Courses"])
def get_courses(db: Session = Depends(get_db), category: str = None, instructor_id: int = None, difficulty_level: str = None):
    query = db.query(Course)
    if category:
        query = query.filter(Course.category == category)
    if instructor_id:
        query = query.filter(Course.instructor_id == instructor_id)
    if difficulty_level:
        query = query.filter(Course.difficulty_level == difficulty_level)
    return query.all()

@router.put("/api/courses/{course_id}",tags=["Courses"])
            # , response_model=CourseResponse
def update_course(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in course.dict().items():
        setattr(db_course, key, value)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.delete("/api/courses/{course_id}",tags=["Courses"])
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(db_course)
    db.commit()
    return {"msg": "Course deleted successfully"}

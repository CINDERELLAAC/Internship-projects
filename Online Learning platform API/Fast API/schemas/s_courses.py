from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str
    description: str
    category: str
    difficulty_level: str
    instructor_id: int

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True

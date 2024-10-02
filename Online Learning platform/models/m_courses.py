from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String)
    category = Column(String, index=True)
    difficulty_level = Column(String, index=True)
    instructor_id = Column(Integer, ForeignKey('instructors.id'))

    instructor = relationship("Instructor", back_populates="courses")

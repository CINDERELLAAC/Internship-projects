from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Instructor(Base):
    __tablename__ = 'instructors'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    courses = relationship("Course", back_populates="instructor")

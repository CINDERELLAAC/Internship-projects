from fastapi import FastAPI
from routers import courses, instructors, students, enrollments

app = FastAPI()

app.include_router(courses.router)
app.include_router(instructors.router)
app.include_router(students.router)
app.include_router(enrollments.router)

# Additional setup code can go here

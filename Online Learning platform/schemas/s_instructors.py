from pydantic import BaseModel

class InstructorBase(BaseModel):
    name: str
    email: str

class InstructorCreate(InstructorBase):
    pass

class InstructorResponse(InstructorBase):
    id: int

    class Config:
        orm_mode = True

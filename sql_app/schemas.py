import datetime
from pydantic import BaseModel, Field



class UserCreate(BaseModel):
    username: str = Field(max_length=15)


class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True

class LectureCreate(BaseModel):
    lecture_name: str = Field(max_length=15)
    lecture_tech: str
    lecture_info: str
    user_id: int
    #date_update: datetime.datetime

class Lecture(LectureCreate):
    lecture_id: int
    #date_update: datetime.datetime

    class Config:
        orm_mode = True
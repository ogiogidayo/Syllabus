import datetime
from pydantic import BaseModel, Field



class UserCreate(BaseModel):
    username: str = Field(max_length=15)


class User(UserCreate):
    user_id: int
    username: str = Field(max_length=15)

    class Config:
        orm_mode = True

class LectureCreate(BaseModel):
    lecture_name: str = Field(max_length=15)
    lecture_tech: str
    lecture_info: str
    #date_update: datetime.datetime

class Lecture(LectureCreate):
    user_id: int
    lecture_id: int
    lecture_name: str = Field(max_length=15)
    lecture_tech: str
    lecture_info: str
    #date_update: datetime.datetime

    class Config:
        orm_mode = True
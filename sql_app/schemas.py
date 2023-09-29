import datetime
from pydantic import BaseModel, Field

class User(BaseModel):
    user_id: int
    username: str = Field(max_length=15)

    class Config:
        orm_mode = True

class Lecture(BaseModel):
    user_id: int
    lecture_id: int
    lecture_name: str = Field(max_length=15)
    lecture_tech: str
    lecture_info: str
    date_update: datetime.datetime.today()

    class Config:
        orm_mode = True
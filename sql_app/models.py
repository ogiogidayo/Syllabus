from sqlalchemy import Column, ForeignKey, Integer, DateTime, String
from .database import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

class Lecture(Base):
    __tablename__ = 'lectures'
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)
    lecture_id = Column(Integer, primary_key=True, index=True)
    lecture_name = Column(String, unique=True, index=True)
    lecture_tech = Column(String, unique=True, index=True)
    lecture_info = Column(String, unique=False, index=True)
    #date_update = Column(DateTime)
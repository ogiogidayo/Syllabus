from sqlalchemy.orm import  Session
from . import models, schemas

#User一覧取得
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

#シラバス一覧取得
def get_lectures(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lecture).offset(skip).limit(limit).all()

#ユーザー登録
def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#シラバス登録
def create_lecture(db: Session, lecture: schemas.Lecture):
    db_lecture = models.Lecture(
        user_id = lecture.user_id,
        lecture_name = lecture.lecture_name,
        lecture_tech=lecture.lecture_tech,
        lecture_info=lecture.lecture_info
    )
    db.add(db_lecture)
    db.commit()
    db.refresh(db_lecture)
    return db_lecture
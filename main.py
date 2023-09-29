from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sql_app import crud, models, schemas
from sql_app.database import engine, SessionLocal
from typing import List

#データベースの作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Read
@app.get("/users", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/read_lecture", response_model=List[schemas.Lecture])
async def read_lectures(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    lectures = crud.get_lectures(db, skip=skip, limit=limit)
    return lectures


@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db,user=user)

@app.post("/create_lecture", response_model=schemas.Lecture)
async def create_lecture(lecture: schemas.LectureCreate, db: Session = Depends(get_db)):
    return crud.create_lecture(db=db,lecture=lecture)
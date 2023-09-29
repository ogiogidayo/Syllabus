from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sql_app import crud, models, schemas
from sql_app.database import engine, SessionLocal
from typing import List

app = FastAPI()


@app.get("/uses")
async def read_users(skip: int = 0, limit = 100):
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

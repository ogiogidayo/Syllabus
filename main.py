from fastapi import FastAPI
from typing import List

app = FastAPI()


@app.get("/uses")
async def read_users(skip: int = 0, limit = 100):
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

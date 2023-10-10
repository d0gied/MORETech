from fastapi import Depends, FastAPI
# from .internal import admin
from .routers import queue

from .db.models.coupons import Base 
from .db.session import get_engine 


app = FastAPI()

app.include_router(queue.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.on_event("startup")
async def start():
    Base.metadata.create_all(get_engine())
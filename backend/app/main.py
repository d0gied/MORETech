from fastapi import Depends, FastAPI

# from .internal import admin
from .routers import queue

app = FastAPI()


app.include_router(queue.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}
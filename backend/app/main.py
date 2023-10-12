from fastapi import Depends, FastAPI

# from .internal import admin
from .routers import queue

from .db.models import Base
from .db.session import get_engine


app = FastAPI()

app.include_router(queue.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.on_event("startup")
async def start():
    Base.metadata.create_all(get_engine())

@app.post("/departments/{department_id}/services/")
def create_service_for_department(department_id: int, service: models.ServiceCreate, db: Session = Depends(database.get_db)):
    return crud.create_service_for_department(db=db, service=service, department_id=department_id)
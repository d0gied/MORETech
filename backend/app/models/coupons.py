import databases
from sqlalchemy import *
from datetime import datetime
from pydantic import BaseModel

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased

class Coupon(Base):
    __tablename__ = 'coupon'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    time = Column(DateTime, default=datetime.now())
    window = Column(String, nullable=False)
    active = Column(Boolean, default=True)

# Создать базу данных в памяти
engine = create_engine('sqlite:///:memory:', echo=True)

# Создать таблицы на основе моделей
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/coupons/")
def get_coupons(department_id: int, amount: int = 10, page: int = 0, db: SessionLocal = Depends(SessionLocal)):
    offset = page * amount
    coupons = (
        db.query(Coupon.name, Coupon.time)
        .filter(Coupon.department_id == department_id)
        .limit(amount)
        .offset(offset)
        .all()
    )
    
    total_coupons = db.query(func.count(Coupon.id)).filter(Coupon.department_id == department_id).scalar()
    total_pages = (total_coupons + amount - 1) // amount

    return {
        "department_id": department_id,
        "page": page,
        "total_pages": total_pages,
        "amount": len(coupons),
        "coupons": [{"name": name, "time": time} for name, time in coupons]
    }
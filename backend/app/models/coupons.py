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

    @classmethod
    def delete(cls, db: Session, department_id: int, coupon: str, window: Optional[str] = None):
        query = db.query(cls).filter_by(department_id=department_id, name=coupon)
        
        if window:
            query = query.filter_by(window=window)
            
        query.delete()
        db.commit()
    

# Создать базу данных в памяти
engine = create_engine('sqlite:///:memory:', echo=True)

# Создать таблицы на основе моделей
Base.metadata.create_all(engine)

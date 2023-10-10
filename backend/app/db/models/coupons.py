from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True)
    coupon = Column(String, nullable=False)
    time = Column(DateTime, default=datetime.now())
    window = Column(String, nullable=True)
    active = Column(Boolean, default=True)
    depatment_id = Column(Integer, nullable=False)



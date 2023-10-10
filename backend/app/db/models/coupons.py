from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True)
    coupon = Column(String, nullable=False)
    time = Column(DateTime, default=datetime.now())
    window = Column(String, nullable=True)
    active = Column(Boolean, default=True)
    department_id = Column(Integer, nullable=False)
    
    def as_dict(self):
        return {"id" : self.id, "coupon" : self.coupon, "time" : self.time,
                "window": self.window, "active" : self.active, "department_id" : self.department_id}

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .base import get_base

Base = get_base()

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    near_metro = Column(String, nullable=False)
    services = ...
    clients = ...
    
    def as_dict(self):
        return {"id" : self.id, "coupon" : self.coupon, "time" : self.time,
                "window": self.window, "active" : self.active, "department_id" : self.department_id}

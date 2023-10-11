from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .base import get_base

Base = get_base()

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    near_metro = Column(String, nullable=True)
    city = Column(String, nullable=False)

    def as_dict(self):
        return {
            "id" : self.id,
            "adress": self.address,
            "near_metro": self.near_metro,
            "city": self.city
        }

from datetime import datetime

from sqlalchemy import Column, Integer, String
from .base import get_base
from services import Service
from sqlalchemy.orm import relationship

Base = get_base()

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    metro = Column(String, nullable=True)
    city = Column(String, nullable=False)

    services = relationship("Department_Service")

    def as_dict(self):
        return {
            "id" : self.id,
            "adress": self.address,
            "metro": self.metro,
            "city": self.city,
            "services": list(map(Service.as_dict, self.services))
        }

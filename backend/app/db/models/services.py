from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .base import get_base

Base = get_base()


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    client_type = Column(String, nullable=False)
    service_time = Column(String, nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "client_type": self.client_type,
            "service_time": self.service_time,
        }

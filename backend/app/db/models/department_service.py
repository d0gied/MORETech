from sqlalchemy import Column, Integer, ForeignKey
from .base import get_base 

Base = get_base()

class Department_Service(Base):
    __tablename__ = 'department_services'

    id = Column(Integer, primary_key=True)
    department_id =  Column(Integer(), ForeignKey("departments.id"))
    service_id = Column(Integer(), ForeignKey("services.id"))

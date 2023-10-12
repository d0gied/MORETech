from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.session import get_session
from ..db.models.departments import Department

router = APIRouter(prefix="/departments", tags=["department"])

@router.put("/")
async def put_department(
    address: str, 
    city: str,
    name: str=None,
    metro: str = None, 
    db_session: Session = Depends(get_session),
):
    department = department(
        name = name,
        address = address, 
        metro = metro,
        city = city
    )
    db_session.add(department)
    db_session.commit()

@router.get("/{department_id}", responses={404: {"description": "Not found"}})
async def get_department(department_id: int, db_session: Session = Depends(get_session)):
    department: department = db_session.query(department).get(department_id)  # returns department or None
    if department is None:
        return HTTPException(404, "department not found")
    return department.as_dict()

router.patch("/{department_id}")  # update data in coupon
async def path_department(
    department_id: int, 
    address: str, 
    city: str,
    name: str=None,
    metro: str = None, 
    db_session: Session = Depends(get_session),
):
    department: department = db_session.query(department).get(department_id)  # returns department or None
    if department is None:
        return HTTPException(404, "department not found")
    if name is not None:
        if name == "":
            return HTTPException(400, "Wrong parametrs")
        department.name = name;
    if metro is not None:
        department.metro = metro 
    if  address is not None:
        department.address = address
    if city is not None:
        department.city = city
    
    db_session.add(department)
    db_session.commit()
    return department.as_dict()

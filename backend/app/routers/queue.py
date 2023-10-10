from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.session import get_session
from ..db.models.coupons import Coupon

router = APIRouter(prefix="/queue", tags=["queue"])

@router.get(
    "/department/{department_id}", responses={404: {"description": "Not found"}}
)
async def get_queue(department_id: int, amount: int = 10, page: int = 0):
    total_amount = len(coupons)
    coupons = coupons[page * amount : page * amount + amount]
    if not coupons:
        return HTTPException(status_code=404, detail="Wrong parameters")

    return {
        "department": department_id,
        "amount": len(coupons),
        "page": page,
        "total_pages": total_amount // amount + (total_amount % amount > 0),  # ceil
    }


@router.put("/department/{department_id}")
async def put_in_queue(
    department_id: int,
    coupon: str,
    time: datetime = None,
    active: bool = True,
    window: str = None,
    db_session: Session = Depends(get_session)
):
    if time is None:
        time = datetime.now()
    coupon = Coupon(
        time = time,
        department_id = department_id,
        coupon = coupon,
        active = active,
        window = window
    )
    db_session.add(coupon)
    db_session.commit()
    return coupon.as_dict()

@router.get("/coupon/{coupon_id}")
async def get_coupon(coupon_id: int):
    ...
    return {"id": 12, "name": "И001", "time": datetime.now(), "active": False}


@router.patch("/coupon/{coupon_id}")  # update data in coupon
async def put_in_queue(
    coupon_id: int, window: str = None, time: datetime = None, active: bool = None
):
    ...
    return {"id": 12, "name": "И001", "time": datetime.now(), "active": False}
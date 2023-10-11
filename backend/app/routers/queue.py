from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.session import get_session
from ..db.models.coupons import Coupon

router = APIRouter(prefix="/queue", tags=["queue"])


@router.get(
    "/department/{department_id}"
)
async def get_queue(
    department_id: int,
    offset: int = 0,
    limit: int = 10,
    db_session: Session = Depends(get_session),
):
    coupons = (
        db_session.query(Coupon)
        .where(Coupon.active == True)
        .where(Coupon.department_id == department_id)
        .order_by(Coupon.time)
        .offset(offset)
        .limit(limit)
    ).all()

    response = {
        'department_id': department_id,
        'offset': offset,
        'limit': limit,
        'amount': len(coupons),
        'coupons': list(map(Coupon.as_dict, coupons))
    }
    return response


@router.put("/department/{department_id}")
async def put_in_queue(
    department_id: int,
    coupon: str,
    time: datetime = None,
    active: bool = True,
    window: str = None,
    db_session: Session = Depends(get_session),
):
    if time is None:
        time = datetime.now()
    coupon = Coupon(
        time=time,
        department_id=department_id,
        coupon=coupon,
        active=active,
        window=window,
    )
    db_session.add(coupon)
    db_session.commit()
    return coupon.as_dict()


@router.get("/coupon/{coupon_id}", responses={404: {"description": "Not found"}})
async def get_coupon(coupon_id: int, db_session: Session = Depends(get_session)):
    coupon: Coupon = db_session.query(Coupon).get(coupon_id)  # returns Coupon or None
    if coupon is None:
        return HTTPException(404, "Coupon not found")
    return coupon.as_dict()


@router.patch("/coupon/{coupon_id}")  # update data in coupon
async def put_in_queue(
    coupon_id: int, window: str = None, time: datetime = None, active: bool = None
):
    ...
    return {"id": 12, "name": "И001", "time": datetime.now(), "active": False}

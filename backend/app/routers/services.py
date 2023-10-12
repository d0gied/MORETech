from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.session import get_session
from ..db.models.services import Service

router = APIRouter(prefix="/services", tags=["service"])


@router.put("/")
async def put_service(
    name: str,
    client_type: str,
    service_time: str,
    db_session: Session = Depends(get_session),
):
    service = Service(name=name, client_type=client_type, service_time=service_time)
    db_session.add(service)
    db_session.commit()


@router.get("/{service_id}", responses={404: {"description": "Not found"}})
async def get_service(service_id: int, db_session: Session = Depends(get_session)):
    service: Service = db_session.query(Service).get(
        service_id
    )  # returns Service or None
    if service is None:
        return HTTPException(404, "Service not found")
    return service.as_dict()


@router.patch("/{service_id}")  # update data in coupon
async def patch_service(
    service_id: int,
    name: str = None,
    client_type: str = None,
    service_time: str = None,
    db_session: Session = Depends(get_session),
):
    service: Service = db_session.query(Service).get(
        service_id
    )  # returns Service or None
    if service is None:
        return HTTPException(404, "Service not found")
    if name is not None:
        if name == "":
            return HTTPException(400, "Wrong parametrs")
        service.name = name
    if service_time is not None:
        service.service_time = service_time
    if client_type is not None:
        service.client_type = client_type

    db_session.add(service)
    db_session.commit()
    return service.as_dict()

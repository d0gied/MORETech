from fastapi import APIRouter, Depends, HTTPException
from ..map_api.yandex import Map

router = APIRouter(prefix="/map", tags=["map"])


@router.get("/yandex/route/time")
async def route_time(A: str, B: str):
    return {"time": "20m"}

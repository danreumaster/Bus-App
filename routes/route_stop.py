from models.route_stop import *
from schemas.route_stop import *
from database import AsyncSession,get_db
from fastapi import APIRouter,Depends

router=APIRouter(prefix="/routestop",tags=["Route Stop"])

@router.post("")
async def create_routestop(route_stop:RouteStopInDB,db:AsyncSession=Depends(get_db)):
    new_route_stop=RouteStop(
        route_id=route_stop.route_id,
        stop_id=route_stop.stop_id,
        stop_order=route_stop.stop_order,
        distance_from_start=route_stop.distance_from_start
    )
    db.add(new_route_stop)
    await db.commit()
    await db.refresh(new_route_stop)
    return new_route_stop
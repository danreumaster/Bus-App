from models.route import *
from models.route_stop import *
from models.stop import *
from fastapi import FastAPI,APIRouter,Depends
from database import AsyncSession,get_db
from schemas.route import RouteInDB
from sqlalchemy import select
from sqlalchemy.orm import selectinload


router=APIRouter(prefix="/route",tags=["Route Stop"])
@router.post("")
async def create_route(route:RouteInDB,db:AsyncSession=Depends(get_db)):
    new_route=Route(name=route.name)
    db.add(new_route)
    await db.commit()
    await db.refresh(new_route)
    return new_route

@router.get("/details")
async def get_route_stops_details(id:int,db:AsyncSession=Depends(get_db)):
    stmt=select(Route).options(selectinload(Route.stops).options(selectinload(RouteStop.stop)))
    data = await db.execute(stmt)
    return data.scalar_one_or_none()

from database import AsyncSession
from models.route import *
from models.stop import *
from models.route_stop import *
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from schemas.route import RouteOut

async def get_route_details(id : int, db : AsyncSession)->RouteOut:
    stmt=select(Route).where(Route.id==id)
    data = await db.execute(stmt)
    data = data.scalar()
    return data

async def get_route_stop_details(id:int,db:AsyncSession):
    stmt= select(Route).where(Route.id == id).options(selectinload(Route.stops).options(selectinload(RouteStop.stop)))
    data = await db.execute(stmt)
    data =  data.scalar_one_or_none()
    return data

async def get_bus_routes_of_city(city:str,db:AsyncSession):
    stmt=select(Route).where(Route.name.like("%"+city+"%"))
    route=await db.execute(stmt)
    return route.scalars().all()
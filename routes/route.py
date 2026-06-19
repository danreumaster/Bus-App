from models.route import *
from models.route_stop import *
from models.stop import *
from fastapi import FastAPI,APIRouter,Depends
from database import AsyncSession,get_db
from schemas.route import RouteInDB,RouteOut
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

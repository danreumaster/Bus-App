from models.vehicle import *
from schemas.vehicle import VehicleInDB
from fastapi import FastAPI,APIRouter,Depends
from database import AsyncSession,get_db
from schemas.route import RouteInDB


router=APIRouter(prefix="/vehicle",tags=["Vehicle"])

@router.post("")
async def create_vehicle(vehicle:VehicleInDB,db:AsyncSession=Depends(get_db) ):
    new_vehicle=Vehicle(name=vehicle.name,owner_id=vehicle.owner_id)
    db.add(new_vehicle)
    await db.commit()
    await db.refresh(new_vehicle)
    return new_vehicle

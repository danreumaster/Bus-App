from models.schedule import *
from fastapi import FastAPI,APIRouter,Depends
from database import AsyncSession,get_db
from schemas.schedule import ScheduleInDB

router=APIRouter(prefix="/schedule",tags=["Schedule"])

@router.post("")
async def create_schedule(schedule:ScheduleInDB,db:AsyncSession=Depends(get_db)):
    new_schedule=Schedule(shift_id=schedule.shift_id,route_id=schedule.route_id,vehicle_id=schedule.vehicle_id)
    db.add(new_schedule)
    await db.commit()
    await db.refresh(new_schedule)
    return new_schedule

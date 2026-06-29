from models.schedule import *
from fastapi import FastAPI,APIRouter,Depends
from database import AsyncSession,get_db
from schemas.schedule import ScheduleInDB
from services.shift_service import get_shift_of_user
from services.schedule_service import get_schedule_of_shift

router=APIRouter(prefix="/schedule",tags=["Schedule"])

@router.post("")
async def create_schedule(schedule:ScheduleInDB,db:AsyncSession=Depends(get_db)):
    new_schedule=Schedule(
        shift_id=schedule.shift_id,
        route_id=schedule.route_id,
        vehicle_id=schedule.vehicle_id,
        start_time=schedule.start_time,
        end_time=schedule.end_time,
        reverse=schedule.reverse
    )
    db.add(new_schedule)
    await db.commit()
    await db.refresh(new_schedule)
    return new_schedule



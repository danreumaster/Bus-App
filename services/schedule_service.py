from database import AsyncSession
from models.schedule import *
from models.route import *
from models.route_stop import *
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from schemas.schedule import ScheduleRouteOut,ScheduleInDB
from typing import List

async def get_schedule_of_shift(shift_id:int,db:AsyncSession):
    stmt=select(Schedule).where(Schedule.shift_id==shift_id, Schedule.active==True)
    data =await db.execute(stmt)
    data=data.scalar_one_or_none()
    #data=[ScheduleRouteOut.model_validate(schedule) for schedule in data]
    
    return data

async def get_schedule(schedule_id:int,db:AsyncSession):
    query = select(Schedule).where(Schedule.id==schedule_id)
    data = await db.execute(query)
    data = data.scalar_one_or_none()
    return data
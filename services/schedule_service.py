from database import AsyncSession
from models.schedule import *
from models.route import *
from models.route_stop import *
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from schemas.schedule import ScheduleRouteOut
from typing import List

async def get_schedule_of_shift(shift_id:int,db:AsyncSession)->ScheduleRouteOut:#List[ScheduleRouteOut]:
    stmt=select(Schedule).where(Schedule.shift_id==shift_id).options(selectinload(Schedule.route).options(selectinload(Route.stops).options(selectinload(RouteStop.stop))))
    data =await db.execute(stmt)
    data=data.scalar_one_or_none()
    #data=[ScheduleRouteOut.model_validate(schedule) for schedule in data]
    data=ScheduleRouteOut.model_validate(data)
    return data

from database import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models.vehicle import *

async def get_vehicle_details(id:int,db:AsyncSession):
    stmt=select(Vehicle).where(Vehicle.id==id)
    data = await db.execute(stmt)
    data = data.scalar_one_or_none()
    return data
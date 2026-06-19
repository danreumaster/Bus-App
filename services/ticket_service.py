from database import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models.ticket import *

async def get_tickets_of_today(db:AsyncSession):
    pass
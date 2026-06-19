from database import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models.shift import *
from models.shift_user import *
from schemas.shift import ShiftOut
from fastapi import HTTPException,status
async def get_shift_user_details(id : int,db : AsyncSession)->ShiftOut:
    stmt=select(Shift).where(Shift.id==id).options(selectinload(Shift.shift_users).options(selectinload(ShiftUser.user)))
    data = await db.execute(stmt)
    data = data.scalar_one_or_none()
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no shift found")
    data = ShiftOut.model_validate(data)
    return data

# Return shift_id,for a given user_id
async def get_shift_of_user(user_id : int,db:AsyncSession):
    stmt=select(ShiftUser.shift_id).where(ShiftUser.user_id==user_id)
    data=await db.execute(stmt)
    data=data.scalar_one_or_none()
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no shift for this user")
    return data
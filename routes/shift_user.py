from models.shift_user import *
from schemas.shift_user import *
from database import AsyncSession,get_db
from fastapi import APIRouter,Depends

router=APIRouter(prefix="/shift/user",tags=["Shift User"])

@router.post("")
async def create_shift_user(shift_user:ShiftUserInDB,db:AsyncSession=Depends(get_db)):
    new_shift_user=ShiftUser(shift_id=shift_user.shift_id,user_id=shift_user.user_id)
    db.add(new_shift_user)
    await db.commit()
    await db.refresh(new_shift_user)


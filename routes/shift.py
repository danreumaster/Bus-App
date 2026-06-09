from models.shift import *
from schemas.shift import ShiftInDB
from database import AsyncSession,get_db
from fastapi import APIRouter,Depends

router=APIRouter(prefix="/shift",tags=["Shift"])

@router.post("")
async def create_shift(shift:ShiftInDB,db:AsyncSession=Depends(get_db)):
    new_shift=Shift(name=shift.name)
    db.add(new_shift)
    await db.commit()
    await db.refresh(new_shift)
    return new_shift
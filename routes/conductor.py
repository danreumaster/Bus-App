from models.route_stop import *
from schemas.route_stop import *
from database import AsyncSession,get_db
from fastapi import APIRouter,Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import *
from schemas import *
from services.auth_service import *
from services.shift_service import get_shift_of_user,get_shift_user_details
from services.schedule_service import get_schedule_of_shift


router=APIRouter(prefix="/conductor",tags=["Conductor"])

@router.get("/dashboard")
async def get_conductor_dashboard(current_user:Annotated[UserInDB,Depends(get_current_user)],db:AsyncSession=Depends(get_db)):
    user_id=await get_user_id(current_user.name,db)
    shift_id = await get_shift_of_user(user_id,db)
    print(shift_id)
    shift_user = await get_shift_user_details(shift_id,db)
    print(shift_user)
    schedules=await get_schedule_of_shift(shift_id,db)
    return {
        "shift":shift_user,
        "schedules":schedules
    }
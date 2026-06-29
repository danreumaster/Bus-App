from models.route_stop import *
from models.schedule import *
from schemas.route_stop import *
from database import AsyncSession,get_db
from fastapi import APIRouter,Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import *
from schemas import *
from services.auth_service import *
from services.shift_service import get_shift_of_user,get_shift_user_details,create_user_shift
from services.schedule_service import get_schedule_of_shift
from services.route_stop_service import get_bus_routes_of_city,get_route_stop_details
from services.vehicle_service import get_vehicle_details

router=APIRouter(prefix="/conductor",tags=["Conductor"])

@router.get("/dashboard")
async def get_conductor_dashboard(city:str,current_user:Annotated[UserInDB,Depends(required_role("staff"))],db:AsyncSession=Depends(get_db)):
    shift_id = await get_shift_of_user(current_user.id,db)

    if shift_id is None:
        shift_user = await  create_user_shift(current_user.id,db)
    
    routes=await get_bus_routes_of_city(city,db)
    return routes

@router.get("/dashboard/route")
async def get_route_dashboard(
    route_id:int,
    current_user:Annotated[UserInDB,Depends(required_role("staff"))],
    db:AsyncSession=Depends(get_db)
    ):
    details = await get_route_stop_details(route_id,db)
    return details

@router.get("/dashboard/schedule/start")
async def start_schedule(
        route_id:int,
        vehicle_id:int,
        reverse:bool,
        current_user:Annotated[UserOut,Depends(required_role("staff"))],
        db:AsyncSession=Depends(get_db)
    ):
    vehicle = await get_vehicle_details(vehicle_id,db)
    if vehicle is None:
        return {"message":"no vehicle such vehicle found"}
    shift_id = await get_shift_of_user(current_user.id,db)

    new_schedule = Schedule(
        route_id=route_id,
        vehicle_id=vehicle_id,
        shift_id=shift_id,
        start_time=datetime.now(),
        reverse=reverse,
        active=True
    )
    db.add(new_schedule)
    await db.commit()
    await db.refresh(new_schedule)
    return {"message":"schedule started","schedule_id":new_schedule.id}

@router.get("/dashboard/schedule/end")
async def end_schedule(
        current_user:Annotated[UserOut,Depends(required_role("staff"))],
        db:AsyncSession=Depends(get_db)
    ):
    
    shift_id = await get_shift_of_user(current_user.id,db)
    schedule = await get_schedule_of_shift(shift_id,db)
    if schedule is None:
        return {"message":"no active schedule found"}
    schedule.active = False
    schedule.end_time = datetime.now()
    db.add(schedule)
    await db.commit()
    await db.refresh(schedule)
    return {"message":"schedule ended","schedule_id":schedule.id}
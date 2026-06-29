from typing_extensions import Annotated

from fastapi import APIRouter, Depends,HTTPException,status
from database import get_db,AsyncSession
from models.ticket import Ticket
from schemas.ticket import *
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from schemas.user import UserOut
from services.schedule_service import *
from services.route_stop_service import *
from services.auth_service import get_user_id,required_role
from services.shift_service import get_shift_of_user


router=APIRouter(prefix="/ticket",tags=["Ticket"])
@router.post("")
async def ticket(ticket : TicketInDB ,current_user:Annotated[UserOut,Depends(required_role("staff"))],db:AsyncSession=Depends(get_db)):
    #------------------------------------------------------------#same as in conductor
    shift_id = await get_shift_of_user(current_user.id,db)
    schedule = await get_schedule_of_shift(shift_id,db)
    #------------------------------------------------------------#
    
    """
    user_id= await get_user_id(ticket.user_id,db)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="invalid user")
    """
    if schedule is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="invalid schedule")
    
    route_details = await get_route_stop_details(schedule.route_id,db)
    
    if (route_details is None) :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="invalid route")
    
    allowed_stop_ids={stops.stop_id for stops in route_details.stops}
    #for i in allowed_stop_ids:
     #   print(i.__dict__)
    if ticket.start_stop_id not in allowed_stop_ids:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="invalid start stop")
    
    if ticket.end_stop_id not in allowed_stop_ids:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="invalid end stop")
    
    d1=0
    d2=0
    for stops in route_details.stops:
        if stops.stop_id==ticket.start_stop_id:
            d1=stops.distance_from_start
        if stops.stop_id==ticket.end_stop_id:
            d2=stops.distance_from_start
    distance=abs(d2-d1)
    fare=distance*2.5
    
    new_ticket=Ticket(
        user_id=ticket.user_id,
        schedule_id=schedule.id,
        start_stop_id=ticket.start_stop_id,
        end_stop_id=ticket.end_stop_id,
        distance=distance,
        fare=fare,
        mode_of_transaction=ticket.mode_of_transaction
    )
    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)
    return new_ticket
  
    
from fastapi import APIRouter, Depends
from database import get_db,AsyncSession
from models.ticket import Ticket
from schemas.ticket import *
from sqlalchemy import select
from sqlalchemy.orm import selectinload


router=APIRouter(prefix="/ticket",tags=["Ticket"])
@router.post("")
async def ticket(ticket : TicketInDB ,db:AsyncSession=Depends(get_db)):
    
    new_ticket=Ticket(
        schedule_id=ticket.schedule_id,
        start_stop_id=ticket.start_stop_id,
        end_stop_id=ticket.end_stop_id,
        distance=ticket.distance
    )
    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)
    return new_ticket
  
    
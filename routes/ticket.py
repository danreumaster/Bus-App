from fastapi import APIRouter, Depends
from database import get_db,AsyncSession
from models.ticket import Ticket
from schemas.ticket import *

router=APIRouter(prefix="/ticket",tags=["Ticket"])
@router.post("")
async def ticket(ticket : TicketInDB,db:AsyncSession=Depends(get_db)):
    
    new_ticket=Ticket(schedule_id=ticket.schedule_id)
    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)
    return new_ticket
  
    
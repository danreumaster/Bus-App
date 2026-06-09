from pydantic import BaseModel

class TicketInDB(BaseModel):
    schedule_id : int
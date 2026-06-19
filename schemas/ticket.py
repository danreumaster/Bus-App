from pydantic import BaseModel

class TicketInDB(BaseModel):
    schedule_id : int
    start_stop_id : int
    end_stop_id : int
    distance : int
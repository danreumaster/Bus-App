from pydantic import BaseModel
from models.ticket import ModeEnum
class TicketInDB(BaseModel):
    user_id :int
    start_stop_id : int
    end_stop_id : int
    mode_of_transaction : ModeEnum

class TicketOut(BaseModel):
    pass
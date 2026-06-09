from pydantic import BaseModel

class ShiftUserInDB(BaseModel):
    shift_id : int
    user_id : int
from pydantic import BaseModel,model_validator,ConfigDict
from schemas.shift_user import ShiftUserOut
from typing import Optional,List
class ShiftInDB(BaseModel):
    name : str

class ShiftOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    shift_users : Optional[List[ShiftUserOut]]=None
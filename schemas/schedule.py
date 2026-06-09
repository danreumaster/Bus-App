from pydantic import BaseModel

class ScheduleInDB(BaseModel):
    shift_id : int
    route_id : int
    vehicle_id : int
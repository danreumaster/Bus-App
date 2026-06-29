from typing import Optional
from pydantic import BaseModel,ConfigDict
from schemas.route import RouteOut
from datetime import datetime
class ScheduleInDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    shift_id : int
    route_id : int
    vehicle_id : int
    start_time : datetime
    end_time : Optional[datetime]
    reverse : bool
    active : bool

class ScheduleRouteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    route : RouteOut
    

    
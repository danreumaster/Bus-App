from pydantic import BaseModel,ConfigDict
from schemas.route import RouteOut
class ScheduleInDB(BaseModel):
    shift_id : int
    route_id : int
    vehicle_id : int

class ScheduleRouteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    route : RouteOut
    

    
from pydantic import BaseModel

class RouteStopInDB(BaseModel):
    route_id : int
    stop_id : int
    stop_order : int
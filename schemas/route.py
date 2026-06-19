from pydantic import BaseModel,ConfigDict
from typing import List,Optional
from schemas.route_stop import RouteStopOut
class RouteInDB(BaseModel):
    name:str

class RouteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name : str
    stops : Optional[List[RouteStopOut]]=None

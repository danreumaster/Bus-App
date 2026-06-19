from pydantic import BaseModel,ConfigDict,model_validator
from typing import List
class RouteStopInDB(BaseModel):
    route_id : int
    stop_id : int
    stop_order : int
    distance_from_start : int

class RouteStopOut(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    
    name : str
    stop_order : int
    distance_from_start : int
    @model_validator(mode="before")
    @classmethod
    def model_validate(cls,obj,**kwargs):
        if hasattr(obj,"stop") and obj.stop is not None:
            return {
                "name":obj.stop.name,
                "stop_order":obj.stop_order,
                "distance_from_start":obj.distance_from_start
            }
                
            
        elif isinstance(obj,dict):
            stop_data=obj.get("stop")
            if isinstance(stop_data, dict):
                name_val = stop_data.get("name", "Unknown Stop")
            elif stop_data is not None and hasattr(stop_data, "name"):
                name_val = stop_data.name
            else:
                name_val = "Unknown Stop" # Fallback if stop is missing or None
            return cls(
                name=name_val,
                stop_order=obj.get("stop_order"),
                distance_from_start=obj.get("distance_from_start")

            )
        return super().model_validate(obj,**kwargs)
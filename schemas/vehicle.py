from pydantic import BaseModel

class VehicleInDB(BaseModel):
    name : str
    owner_id : int
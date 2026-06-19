from pydantic import BaseModel,model_validator,ConfigDict
from typing import Optional,Any
class ShiftUserInDB(BaseModel):
    shift_id : int
    user_id : int
class ShiftUserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    job: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def flatten_user_details(cls, data: Any) -> Any:
        if hasattr(data, "user") and data.user is not None:
            return {
                "name": getattr(data.user, "name", "Unknown"),
                "job": getattr(data, "job", None)
            }
            
        
        if isinstance(data, dict):
            user_data = data.get("user") or {}
            
            if hasattr(user_data, "name"):
                name_val = getattr(user_data, "name", "Unknown")
            else:
                name_val = user_data.get("name", "Unknown")
                
            return {
                "name": name_val,
                "job": data.get("job")
            }
            
        # Scenario C: Safety fallback to prevent returning None
        return data

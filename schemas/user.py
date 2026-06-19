from pydantic import BaseModel,ConfigDict
from models.user import RoleEnum


class UserOut(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    name : str
    role : RoleEnum|None
    

class UserInDB(UserOut):
    password : str



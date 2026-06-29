from pydantic import BaseModel,ConfigDict
from models.user import RoleEnum

class UserIn(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    name : str
    password : str
    role : RoleEnum|None
class UserOut(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id : int
    name : str
    role : RoleEnum|None
    

class UserInDB(UserOut):
    password : str



from pydantic import BaseModel
from models.user import RoleEnum


class UserOut(BaseModel):
    name : str
    role : RoleEnum
    

class UserInDB(UserOut):
    passwod : str



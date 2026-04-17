from pydantic import BaseModel
from enums import *

class UserIn(BaseModel):
    name:str
    email:str
    password:str
    role:RoleEnum
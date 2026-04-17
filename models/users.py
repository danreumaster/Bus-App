from db import Base
from sqlalchemy import INTEGER,Column,String,Enum
from enums import *
class User(Base):
    __tablename__="users"
    id=Column(INTEGER,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    role=Column(String,Enum(RoleEnum))
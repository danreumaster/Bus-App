from database import Base
from sqlalchemy import Column,String,Integer,DateTime,Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

class RoleEnum(str,enum.Enum):
    admin="admin"
    operator="operator"
    staff="staff"
    passenger="passenger"

class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    role = Column(String,Enum(RoleEnum))
    password =Column(String)

    vehicles = relationship("Vehicle",back_populates="user")
    shift_user = relationship("ShiftUser",back_populates="user")
    
from database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    
    shift_users = relationship("ShiftUser",back_populates="shift")
    schedules = relationship("Schedule",back_populates="shift")
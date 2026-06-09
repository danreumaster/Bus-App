from database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Vehicle(Base):
    __tablename__="vehicles"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))

    user = relationship("User",back_populates="vehicles")
    schedules = relationship("Schedule",back_populates="vehicle")
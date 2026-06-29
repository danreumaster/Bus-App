from datetime import timezone

from database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey,Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer,primary_key=True,index=True)
    start_time = Column(DateTime(timezone=True),nullable=True)
    end_time = Column(DateTime(timezone=True),nullable=True)
    route_id= Column(Integer,ForeignKey("routes.id",ondelete="CASCADE"))
    shift_id = Column(Integer,ForeignKey("shifts.id",ondelete="CASCADE"))
    vehicle_id = Column(Integer,ForeignKey("vehicles.id",ondelete="CASCADE"))
    reverse = Column(Boolean,default=False)
    active = Column(Boolean,default=True)

    route = relationship("Route",back_populates="schedules")
    shift = relationship("Shift",back_populates="schedules")
    vehicle = relationship("Vehicle",back_populates="schedules")
    tickets =relationship("Ticket",back_populates="schedule")
    
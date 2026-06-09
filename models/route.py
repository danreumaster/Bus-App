from database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
class Route(Base):
    __tablename__="routes"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)

    stops=relationship("RouteStop",back_populates="route",order_by="RouteStop.stop_order",cascade="all, delete-orphan")
    schedules=relationship("Schedule",back_populates="route")
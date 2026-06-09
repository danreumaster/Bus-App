from database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class RouteStop(Base):
    __tablename__ = "routestop"
    
    id = Column(Integer,primary_key=True,index=True)
    route_id = Column(Integer,ForeignKey("routes.id",ondelete="CASCADE"))
    stop_id = Column(Integer,ForeignKey("stops.id",ondelete="CASCADE"))
    stop_order = Column(Integer)

    route=relationship("Route",back_populates="stops")
    stop=relationship("Stop",back_populates="routes")




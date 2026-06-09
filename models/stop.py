from database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Stop(Base):
    __tablename__ = "stops"

    id = Column(Integer,primary_key=True,index=True)
    name=Column(String)

    routes=relationship("RouteStop",back_populates="stop")
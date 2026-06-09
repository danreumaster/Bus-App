from database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Ticket(Base):
    __tablename__="tickets"

    id = Column(Integer,primary_key=True,index=True)
    created_at = Column(DateTime(timezone=True),nullable=False,server_default=func.now())
    schedule_id = Column(Integer,ForeignKey("schedules.id",ondelete="CASCADE"))

    schedule = relationship("Schedule",back_populates="tickets")
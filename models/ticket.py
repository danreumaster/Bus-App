from database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey,Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

class ModeEnum(str,enum.Enum):
    cash="cash"
    wallet="wallet"
    upi="upi"
class Ticket(Base):
    __tablename__="tickets"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id",ondelete="SET NULL"),nullable=True)
    created_at = Column(DateTime(timezone=True),nullable=False,server_default=func.now())
    schedule_id = Column(Integer,ForeignKey("schedules.id",ondelete="CASCADE"))
    start_stop_id = Column(Integer,ForeignKey("stops.id",ondelete="CASCADE"))
    end_stop_id = Column(Integer,ForeignKey("stops.id",ondelete="CASCADE"))
    distance = Column(Integer)
    fare = Column(Integer)
    mode_of_transaction = Column(String,Enum(ModeEnum))

    schedule = relationship("Schedule",back_populates="tickets")
    start_stop = relationship("Stop",foreign_keys=[start_stop_id])
    end_stop = relationship("Stop",foreign_keys=[end_stop_id])
    
from database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class ShiftUser(Base):
    __tablename__ = "shift_users"

    id = Column(Integer,primary_key=True,index=True)
    shift_id = Column(Integer,ForeignKey("shifts.id",ondelete="CASCADE"))
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    job = Column(String)

    shift = relationship("Shift",back_populates="shift_users")
    user = relationship("User",back_populates="shift_user")
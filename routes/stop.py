from models.stop import *
from schemas.stop import *
from database import AsyncSession,get_db
from fastapi import APIRouter,Depends

router=APIRouter(prefix="/stop",tags=["Route Stop"])

@router.post("/")
async def create_stop(stop:StopInDB,db:AsyncSession=Depends(get_db)):
    new_stop=Stop(name=stop.name)
    db.add(new_stop)
    await db.commit()
    await db.refresh(new_stop)
    return new_stop
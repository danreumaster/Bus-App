from fastapi import APIRouter, Depends
from database import get_db,AsyncSession
from models.user import User
from schemas.user import *

router = APIRouter(prefix = "/auth",tags=["Auth"])
@router.post("/register")
async def register(user : UserInDB ,db:AsyncSession=Depends(get_db)):
    new_user = User(name=user.name,role=user.role,password=user.passwod)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
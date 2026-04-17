from fastapi import FastAPI,APIRouter,Depends,HTTPException
from db import get_db
from sqlalchemy.orm import Session
from models.users import *
from schemas.users import *

router=APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/register")
def register(user : UserIn,db:Session=Depends(get_db)):
    old_user=db.query(User).filter(User.email==user.email).first()
    if old_user:
        raise HTTPException(status_code=400,detail="Email already exists")
    user=User(name=user.name,email=user.email,password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message":"user created","details":user}

@router.get("/login")
def login(user : UserIn,db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.email==user.email).first()
    if not db_user:
        raise HTTPException(status_code=400,detail="Invalid email or password")
    if db_user.password!=user.password:
        raise HTTPException(status_code=400,detail="Invalid email or password")
    return {"message":"Login successful","details":db_user}
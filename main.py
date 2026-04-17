from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from routes.auth import router as auth_router
app=FastAPI()
app.include_router(auth_router)

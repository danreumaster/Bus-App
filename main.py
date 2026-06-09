from fastapi import FastAPI,Depends,APIRouter
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from routes.ticket import router as ticket_router
from routes.auth import router as auth_router
from routes.route import router as route_router
from routes.stop import router as stop_router
from routes.route_stop import router as route_stop_router
from routes.vehicle import router as vehicle_router
from routes.shift import router as shift_router
from routes.shift_user import router as shift_user_router
from routes.schedule import router as schedule_router
app= FastAPI()

app.include_router(auth_router)
app.include_router(route_router)
app.include_router(stop_router)
app.include_router(route_stop_router)
app.include_router(vehicle_router)
app.include_router(shift_router)
app.include_router(shift_user_router)
app.include_router(schedule_router)
app.include_router(ticket_router)
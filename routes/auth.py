from fastapi import APIRouter, Depends
from database import get_db,AsyncSession
from models.user import User
from schemas.user import *
from services.auth_service import *
from schemas.user import *

router = APIRouter(prefix = "/auth",tags=["Auth"])
@router.post("/register")
async def register_user(form_data:UserIn,db:AsyncSession=Depends(get_db)):
    user = await get_user(form_data.name,db)
    if not (user is None):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="user alerady exists")
    hashed_password=hash_password(form_data.password)
    new_user=User(name=form_data.name,password=hashed_password,role=form_data.role)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    jwt_token=create_access_token({"sub":form_data.name})
    return jwt_token
@router.post("/login")
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:AsyncSession=Depends(get_db)):
    user=await get_user(form_data.username,db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid details")
    if not verify_password(form_data.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid details")

    jwt_token=create_access_token({"sub":user.name})
    return jwt_token
@router.get("/me")
async def get_user_details(current_user:Annotated[UserOut,Depends(get_current_user)]):
    return current_user
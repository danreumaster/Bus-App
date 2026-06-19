from fastapi import HTTPException,Depends,status
from jose import jwt,JWTError
from passlib.context import CryptContext
from typing import Union,Annotated
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from database import AsyncSession,get_db
from sqlalchemy import select
from models.user import User
from schemas.user import *
from datetime import datetime,timedelta,timezone

SECRET="go_daniel_billionaire_2005"
ALGORITHM="HS256"

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="auth/login")

import bcrypt

# Replace your old pwd_context with these two pure Python functions
def hash_password(password: str) -> str:
    # Encodes string to bytes, salts, hashes, and decodes back to string for DB storage
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), 
            hashed_password.encode("utf-8")
        )
    except Exception:
        return False
    


async def get_user(name:str,db:AsyncSession)->Union[UserInDB,None]:
    query=select(User).where(User.name==name)
    user=await db.execute(query)
    user=user.scalar_one_or_none()
    if user:
        return UserInDB.model_validate(user)


async def authenticate_user(name:str,password:str,db:AsyncSession):
    credential_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="incorrect username/password")
    user=await get_user(name,db)
    if user is None:
        raise credential_exception
    if not verify_password(password,user.password):
        raise credential_exception
    return user

def create_access_token(data:dict,exp:Union[timedelta,None]=None):
    to_encode=data.copy()
    if exp:
        exp=datetime.now(timezone.utc)+exp
    else:
        exp=datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode['exp']=exp

    jwt_encoded=jwt.encode(to_encode,SECRET,algorithm=ALGORITHM)
    return {
        "access_token":jwt_encoded,"token_type":"bearer"
    }

async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)],db:AsyncSession=Depends(get_db))->UserInDB:

    credential_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        payload=jwt.decode(token,SECRET,ALGORITHM)

        name=payload.get('sub')
        if name is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    user=await get_user(name,db)
    if user is None:
        raise credential_exception
    return UserInDB.model_validate(user)

async def get_user_id(name:str,db:AsyncSession)->int:
    stmt=select(User.id).where(User.name==name)
    user_id=await db.execute(stmt)
    user_id=user_id.scalar_one_or_none()
    return user_id
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import(
    async_sessionmaker,
    create_async_engine,
    AsyncSession
)
from sqlalchemy.orm import declarative_base
import os

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_async_engine(DATABASE_URL,echo=False,pool_pre_ping=True)#echo set to true if u want to see db operations on log

AsyncSessionLocal=async_sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)

Base=declarative_base()
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

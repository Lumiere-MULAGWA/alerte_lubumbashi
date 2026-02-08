import asyncio
from app.core.database import engine, Base
from app.models import users, alert, report

async def init_db():
    async with engine.begin() as conn:
        # Drop all tables (en dev seulement!)
        # await conn.run_sync(Base.metadata.drop_all)
        
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
    
    print("Database initialized successfully")

if __name__ == "__main__":
    asyncio.run(init_db())
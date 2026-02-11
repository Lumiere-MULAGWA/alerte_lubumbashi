import asyncio
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.crud.crud_user import crud_user
from app.schemas.user import UserCreate
from app.models.users import UserRole

async def create_admin_user():
    db = SessionLocal()
    try:
        admin_data = UserCreate(
            email="admin@alert.app",
            password="Admin123!",
            full_name="Administrator",
            role=UserRole.ADMIN
        )
        
        admin = crud_user.create(db, obj_in=admin_data)
        print(f"Admin user created: {admin.email}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(create_admin_user())
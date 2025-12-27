from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.database import get_db
from app.schemas.auth import RegisterSchema, LoginSchema, TokenSchema
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService


router = APIRouter(prefix="/auth", tags=["Auth"])




@router.post("/register", response_model=TokenSchema)
def register(payload: RegisterSchema, db: Session = Depends(get_db)):
service = AuthService(UserRepository(db))
token = service.register(payload.full_name, payload.email, payload.password)
return {"access_token": token}




@router.post("/login", response_model=TokenSchema)
def login(payload: LoginSchema, db: Session = Depends(get_db)):
service = AuthService(UserRepository(db))
token = service.login(payload.email, payload.password)
return {"access_token": token}


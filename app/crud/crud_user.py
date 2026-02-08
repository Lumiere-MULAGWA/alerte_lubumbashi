from typing import Optional, List
from sqlalchemy.orm import Session
import uuid
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password

class CRUDUser:
    def get(self, db: Session, user_id: uuid.UUID) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()
    
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).offset(skip).limit(limit).all()
    
    def create(self, db: Session, obj_in: UserCreate) -> User:
        hashed_password = get_password_hash(obj_in.password)
        db_user = User(
            email=obj_in.email,
            hashed_password=hashed_password,
            full_name=obj_in.full_name,
            phone_number=obj_in.phone_number,
            role=obj_in.role
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def update(self, db: Session, db_user: User, obj_in: UserUpdate) -> User:
        update_data = obj_in.dict(exclude_unset=True)
        
        if "new_password" in update_data and "current_password" in update_data:
            if verify_password(update_data["current_password"], db_user.hashed_password):
                update_data["hashed_password"] = get_password_hash(update_data["new_password"])
            else:
                raise ValueError("Current password is incorrect")
        
        for field, value in update_data.items():
            if field not in ["current_password", "new_password"]:
                setattr(db_user, field, value)
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    def is_active(self, user: User) -> bool:
        return user.is_active

crud_user = CRUDUser()
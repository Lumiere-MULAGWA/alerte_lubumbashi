from sqlalchemy.orm import Session
from app.models.users import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db


    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()


    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def update(self , data:User):
        self.db.add(data)
        self.db.commit()
        
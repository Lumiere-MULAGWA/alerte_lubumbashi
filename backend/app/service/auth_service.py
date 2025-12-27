from fastapi import HTTPException, status
from app.core.security import hash_password, verify_password, create_access_token
from app.domain.auth_domain import can_register_user, validate_login
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:


def __init__(self, repo: UserRepository):
self.repo = repo


def register(self, full_name: str, email: str, password: str):
existing = self.repo.get_by_email(email)
try:
can_register_user(existing is not None)
except ValueError:
raise HTTPException(status_code=400, detail="Email déjà utilisé")


user = User(
full_name=full_name,
email=email,
password_hash=hash_password(password)
)
self.repo.create(user)


token = create_access_token({"sub": str(user.id), "role": user.role})
return token


def login(self, email: str, password: str):
user = self.repo.get_by_email(email)
try:
validate_login(user is not None, verify_password(password, user.password_hash) if user else False)
except ValueError:
raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Identifiants invalides")


token = create_access_token({"sub": str(user.id), "role": user.role})
return token
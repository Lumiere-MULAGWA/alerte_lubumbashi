from pydantic_settings import BaseSettings
from typing import List, Optional
import secrets

class Settings(BaseSettings):
    # App
    PROJECT_NAME: str = "Alert App API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # API
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/alert_db"
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    
    # Alert Settings
    ALERT_LIMIT_THRESHOLD: int = 5
    ALERT_DELETE_THRESHOLD: int = 10
    DEFAULT_ALERT_RADIUS: int = 1000  # meters
    MAX_ALERT_RADIUS: int = 5000  # meters
    ALERT_DURATION_HOURS: int = 24
    
    # Firebase
    FCM_SERVER_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
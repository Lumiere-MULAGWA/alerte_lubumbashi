from pydantic_settings import BaseSettings
from typing import List, Optional
import secrets

class Settings(BaseSettings):
    # App
    PROJECT_NAME: str = "Alert App API"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # API
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database - MySQL
    DATABASE_URL: str = "mysql+pymysql://alert_user:strong_password@localhost:3306/alert_db"
    
    # CORS
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    
    # Alert Settings
    ALERT_LIMIT_THRESHOLD: int = 5
    ALERT_DELETE_THRESHOLD: int = 10
    DEFAULT_ALERT_RADIUS: int = 1000
    MAX_ALERT_RADIUS: int = 5000
    ALERT_DURATION_HOURS: int = 24
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"

settings = Settings()
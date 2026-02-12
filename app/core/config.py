# app/core/config.py - Version compatible avec les chaînes simples
from pydantic_settings import BaseSettings
from typing import List, Optional
from pydantic import field_validator
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
    
    # CORS - Utiliser des chaînes séparées par des virgules
    ALLOWED_HOSTS: str = "localhost,127.0.0.1"
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:8080"
    
    # Alert Settings
    ALERT_LIMIT_THRESHOLD: int = 5
    ALERT_DELETE_THRESHOLD: int = 10
    DEFAULT_ALERT_RADIUS: int = 1000
    MAX_ALERT_RADIUS: int = 5000
    ALERT_DURATION_HOURS: int = 24
    
    # Firebase
    FCM_SERVER_KEY: Optional[str] = None
    
    @field_validator("ALLOWED_HOSTS", mode="before")
    @classmethod
    def parse_allowed_hosts(cls, v):
        """Convertit une chaîne CSV en liste"""
        if isinstance(v, str):
            return [host.strip() for host in v.split(",") if host.strip()]
        return v
    
    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        """Convertit une chaîne CSV en liste"""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"  # Ignorer les champs supplémentaires

settings = Settings()
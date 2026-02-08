from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
import uuid
from app.models.alert import AlertType, AlertSource, AlertStatus

# Base
class AlertBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: AlertType
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    radius: int = Field(default=1000, ge=100, le=5000)

# Create
class AlertCreate(AlertBase):
    source: AlertSource = AlertSource.CITIZEN
    
    @validator('title')
    def title_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty')
        return v.strip()

# Update (pour admin)
class AlertUpdate(BaseModel):
    status: Optional[AlertStatus] = None
    is_official: Optional[bool] = None

# In DB
class AlertInDB(AlertBase):
    id: uuid.UUID
    user_id: uuid.UUID
    source: AlertSource
    is_official: bool
    status: AlertStatus
    report_count: int
    created_at: datetime
    updated_at: Optional[datetime]
    expires_at: datetime
    
    class Config:
        from_attributes = True

# Response
class Alert(AlertInDB):
    pass

# List response avec géométrie
class AlertWithDistance(Alert):
    distance: float  # distance en mètres

# Stats
class AlertStats(BaseModel):
    total: int
    active: int
    limited: int
    deleted: int
    by_type: dict
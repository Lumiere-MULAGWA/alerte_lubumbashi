from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum, ForeignKey, Float
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql import func
import uuid
from app.core.database import Base
import enum

class AlertType(str, enum.Enum):
    ACCIDENT = "accident"
    THEFT = "theft"
    FIRE = "fire"
    FLOOD = "flood"
    DANGER = "danger"
    SECURITY = "security"
    HEALTH = "health"
    OTHER = "other"

class AlertSource(str, enum.Enum):
    CITIZEN = "citizen"
    AUTHORITY = "authority"

class AlertStatus(str, enum.Enum):
    ACTIVE = "active"
    LIMITED = "limited"
    DELETED = "deleted"

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000))
    type = Column(Enum(AlertType), nullable=False)
    source = Column(Enum(AlertSource), nullable=False, default=AlertSource.CITIZEN)
    is_official = Column(Boolean, default=False)
    
    # Géolocalisation simple
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    radius = Column(Integer, default=1000)
    
    # Statut
    status = Column(Enum(AlertStatus), default=AlertStatus.ACTIVE, nullable=False)
    report_count = Column(Integer, default=0)
    
    # Relations
    user_id = Column(CHAR(36), ForeignKey("users.id"), nullable=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=False)
    
    def __repr__(self):
        return f"<Alert {self.title} - {self.status}>"
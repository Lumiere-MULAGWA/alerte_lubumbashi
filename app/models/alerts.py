from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func, text
from geoalchemy2 import Geometry
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
    ADMIN = "admin" 

class AlertStatus(str, enum.Enum):
    ACTIVE = "active"
    LIMITED = "limited"
    DELETED = "deleted"

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    type = Column(Enum(AlertType), nullable=False)
    source = Column(Enum(AlertSource), nullable=False, default=AlertSource.CITIZEN)
    is_official = Column(Boolean, default=False)
    
    # Géolocalisation
    location = Column(Geometry('POINT', srid=4326), nullable=False)
    radius = Column(Integer, default=1000)  # en mètres
    
    # Statut
    status = Column(Enum(AlertStatus), default=AlertStatus.ACTIVE, nullable=False)
    report_count = Column(Integer, default=0)
    
    # Relations
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=False)
    
    def __repr__(self):
        return f"<Alert {self.title} - {self.status}>"
from sqlalchemy import Column, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Report(Base):
    __tablename__ = "reports"
    
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    alert_id = Column(CHAR(36), ForeignKey("alerts.id"), nullable=False, index=True)
    user_id = Column(CHAR(36), ForeignKey("users.id"), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (UniqueConstraint('alert_id', 'user_id', name='unique_alert_user_report'),)
    
    def __repr__(self):
        return f"<Report alert:{self.alert_id} user:{self.user_id}>"
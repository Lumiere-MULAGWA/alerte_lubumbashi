import uuid
from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship


from .base import Base


class AlertReport(Base):
    __tablename__ = "alert_reports"
    __table_args__ = (UniqueConstraint("alert_id", "user_id"),)


    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    alert_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("alerts.id", ondelete="CASCADE"))
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())


    alert = relationship("Alert", back_populates="reports")
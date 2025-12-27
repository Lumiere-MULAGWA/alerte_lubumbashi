import uuid
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column


from .base import Base


class NotificationToken(Base):
__tablename__ = "notification_tokens"


id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
token: Mapped[str] = mapped_column(String)
platform: Mapped[str] = mapped_column(String(20)) # web / android / ios
created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
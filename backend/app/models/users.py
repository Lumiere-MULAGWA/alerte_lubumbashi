import uuid
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Mapped, mapped_column


from .base import Base


class User(Base):
__tablename__ = "users"


id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
full_name: Mapped[str] = mapped_column(String(150))
email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
phone: Mapped[str | None] = mapped_column(String(30))
password_hash: Mapped[str] = mapped_column(String)
role: Mapped[str] = mapped_column(String(30), default="citizen")
is_active: Mapped[bool] = mapped_column(Boolean, default=True)
created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())


location = relationship("UserLocation", back_populates="user", uselist=False)
alerts = relationship("Alert", back_populates="creator")
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from geoalchemy2 import Geography


from .base import Base


class UserLocation(Base):
__tablename__ = "user_locations"


id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
location: Mapped = mapped_column(Geography(geometry_type="POINT", srid=4326))
updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


user = relationship("User", back_populates="location")
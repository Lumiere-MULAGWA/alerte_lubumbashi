import uuid
from sqlalchemy import String, Text, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from geoalchemy2 import Geography


from .base import Base


class Alert(Base):
__tablename__ = "alerts"


id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
title: Mapped[str] = mapped_column(String(200))
description: Mapped[str | None] = mapped_column(Text)
category: Mapped[str] = mapped_column(String(50))
alert_type: Mapped[str] = mapped_column(String(20)) # citizen / official
status: Mapped[str] = mapped_column(String(20), default="active")


location: Mapped = mapped_column(Geography(geometry_type="POINT", srid=4326))
radius_meters: Mapped[int] = mapped_column(Integer)


false_reports: Mapped[int] = mapped_column(Integer, default=0)


created_by: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())


creator = relationship("User", back_populates="alerts")
reports = relationship("AlertReport", back_populates="alert", cascade="all, delete")
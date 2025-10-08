"""Invite model."""

from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class InviteStatus(str, Enum):
    """Invite status enumeration."""

    CREATED = "created"
    OPENED = "opened"
    COMPLETED = "completed"


class Invite(Base):
    """Study invite link."""

    __tablename__ = "invites"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    study_id: Mapped[int] = mapped_column(ForeignKey("studies.id", ondelete="CASCADE"), index=True)
    invite_code: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    interviewee_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default=InviteStatus.CREATED.value, nullable=False)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)

    # Relationships
    study: Mapped["Study"] = relationship("Study", back_populates="invites")  # type: ignore
    interview: Mapped["Interview | None"] = relationship(
        "Interview", back_populates="invite", uselist=False
    )

    def __repr__(self) -> str:
        return f"<Invite(id={self.id}, code={self.invite_code}, status={self.status})>"


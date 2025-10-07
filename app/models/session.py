"""Session model for researcher authentication."""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Session(Base):
    """Server-side session for researchers."""

    __tablename__ = "sessions"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default="now()", nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    csrf_secret: Mapped[str] = mapped_column(String(64), nullable=False)

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="sessions")  # type: ignore

    def __repr__(self) -> str:
        return f"<Session(id={self.id}, user_id={self.user_id})>"


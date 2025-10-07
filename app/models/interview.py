"""Interview-related models."""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSON

from app.db.base import Base


class Interview(Base):
    """Interview session."""

    __tablename__ = "interviews"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    study_id: Mapped[int] = mapped_column(ForeignKey("studies.id", ondelete="CASCADE"), index=True)
    invite_id: Mapped[int] = mapped_column(
        ForeignKey("invites.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    started_at: Mapped[datetime] = mapped_column(DateTime, server_default="now()", nullable=False)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    agent_turns: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Relationships
    study: Mapped["Study"] = relationship("Study", back_populates="interviews")  # type: ignore
    invite: Mapped["Invite"] = relationship("Invite", back_populates="interview")  # type: ignore
    interviewee: Mapped["Interviewee | None"] = relationship(
        "Interviewee", back_populates="interview", uselist=False, cascade="all, delete-orphan"
    )
    messages: Mapped[list["Message"]] = relationship(
        "Message", back_populates="interview", cascade="all, delete-orphan", order_by="Message.created_at"
    )
    insight: Mapped["Insight | None"] = relationship(
        "Insight", back_populates="interview", uselist=False, cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Interview(id={self.id}, study_id={self.study_id}, turns={self.agent_turns})>"


class Interviewee(Base):
    """Interviewee information."""

    __tablename__ = "interviewees"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    interview_id: Mapped[int] = mapped_column(
        ForeignKey("interviews.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    demographics_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    consent_at: Mapped[datetime] = mapped_column(DateTime, server_default="now()", nullable=False)

    # Relationships
    interview: Mapped["Interview"] = relationship("Interview", back_populates="interviewee")

    def __repr__(self) -> str:
        return f"<Interviewee(id={self.id}, name={self.name}, email={self.email})>"


class Message(Base):
    """Chat message."""

    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    interview_id: Mapped[int] = mapped_column(ForeignKey("interviews.id", ondelete="CASCADE"), index=True)
    role: Mapped[str] = mapped_column(String(20), nullable=False)  # 'agent', 'user', 'system'
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default="now()", nullable=False)

    # Relationships
    interview: Mapped["Interview"] = relationship("Interview", back_populates="messages")

    def __repr__(self) -> str:
        return f"<Message(id={self.id}, role={self.role}, interview_id={self.interview_id})>"


class Insight(Base):
    """Interview insights."""

    __tablename__ = "insights"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    interview_id: Mapped[int] = mapped_column(
        ForeignKey("interviews.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    sentiment: Mapped[str] = mapped_column(String(20), nullable=False)  # 'pos', 'neu', 'neg'
    keywords_json: Mapped[list] = mapped_column(JSON, nullable=False)
    quotes_json: Mapped[list] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default="now()", nullable=False)

    # Relationships
    interview: Mapped["Interview"] = relationship("Interview", back_populates="insight")

    def __repr__(self) -> str:
        return f"<Insight(id={self.id}, interview_id={self.interview_id}, sentiment={self.sentiment})>"


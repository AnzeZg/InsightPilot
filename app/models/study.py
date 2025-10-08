"""Study-related models."""

from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Study(Base):
    """Research study model."""

    __tablename__ = "studies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    owner_user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    consent_text: Mapped[str] = mapped_column(Text, nullable=False)
    max_agent_turns: Mapped[int] = mapped_column(Integer, default=9, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)

    # Relationships
    owner: Mapped["User"] = relationship("User", back_populates="studies")  # type: ignore
    questions: Mapped[list["StudyQuestion"]] = relationship(
        "StudyQuestion", back_populates="study", cascade="all, delete-orphan", order_by="StudyQuestion.sort_order"
    )
    invites: Mapped[list["Invite"]] = relationship(
        "Invite", back_populates="study", cascade="all, delete-orphan"
    )
    interviews: Mapped[list["Interview"]] = relationship(
        "Interview", back_populates="study", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Study(id={self.id}, title={self.title})>"


class StudyQuestion(Base):
    """Study seed questions."""

    __tablename__ = "study_questions"
    __table_args__ = ({"schema": None},)

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    study_id: Mapped[int] = mapped_column(ForeignKey("studies.id", ondelete="CASCADE"), index=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # Relationships
    study: Mapped["Study"] = relationship("Study", back_populates="questions")

    def __repr__(self) -> str:
        return f"<StudyQuestion(id={self.id}, study_id={self.study_id}, order={self.sort_order})>"


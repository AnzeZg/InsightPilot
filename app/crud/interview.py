"""CRUD operations for Interview, Interviewee, Message, and Insight models."""

from datetime import UTC, datetime

from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.models.interview import Insight, Interview, Interviewee, Message

# Interview CRUD


def create_interview(db: Session, study_id: int, invite_id: int) -> Interview:
    """Create a new interview."""
    interview = Interview(study_id=study_id, invite_id=invite_id, agent_turns=0)
    db.add(interview)
    db.commit()
    db.refresh(interview)
    return interview


def get_interview_by_id(
    db: Session, interview_id: int, load_messages: bool = False, load_all: bool = False
) -> Interview | None:
    """Get interview by ID with optional related data."""
    stmt = select(Interview).where(Interview.id == interview_id)
    if load_all:
        stmt = stmt.options(
            selectinload(Interview.messages),
            selectinload(Interview.interviewee),
            selectinload(Interview.insight),
        )
    elif load_messages:
        stmt = stmt.options(selectinload(Interview.messages))
    return db.scalar(stmt)


def get_interviews_by_study(
    db: Session, study_id: int, load_relations: bool = False
) -> list[Interview]:
    """Get all interviews for a study."""
    stmt = (
        select(Interview)
        .where(Interview.study_id == study_id)
        .order_by(Interview.started_at.desc())
    )
    if load_relations:
        stmt = stmt.options(
            selectinload(Interview.interviewee),
            selectinload(Interview.insight),
        )
    return list(db.scalars(stmt).all())


def get_interview_by_invite(db: Session, invite_id: int) -> Interview | None:
    """Get interview by invite ID."""
    stmt = select(Interview).where(Interview.invite_id == invite_id)
    return db.scalar(stmt)


def complete_interview(db: Session, interview_id: int) -> Interview | None:
    """Mark interview as completed."""
    interview = db.get(Interview, interview_id)
    if interview:
        interview.completed_at = datetime.now(UTC).replace(tzinfo=None)
        db.commit()
        db.refresh(interview)
    return interview


def increment_agent_turns(db: Session, interview_id: int) -> Interview | None:
    """Increment agent turn counter."""
    interview = db.get(Interview, interview_id)
    if interview:
        interview.agent_turns += 1
        db.commit()
        db.refresh(interview)
    return interview


# Interviewee CRUD


def create_interviewee(
    db: Session,
    interview_id: int,
    name: str,
    email: str,
    demographics_json: dict | None = None,
) -> Interviewee:
    """Create interviewee record."""
    interviewee = Interviewee(
        interview_id=interview_id, name=name, email=email, demographics_json=demographics_json
    )
    db.add(interviewee)
    db.commit()
    db.refresh(interviewee)
    return interviewee


def get_interviewee_by_interview(db: Session, interview_id: int) -> Interviewee | None:
    """Get interviewee by interview ID."""
    stmt = select(Interviewee).where(Interviewee.interview_id == interview_id)
    return db.scalar(stmt)


# Message CRUD


def get_message_count(db: Session, interview_id: int) -> int:
    """Get count of messages for an interview."""
    stmt = select(func.count(Message.id)).where(Message.interview_id == interview_id)
    return db.scalar(stmt) or 0


def create_message(db: Session, interview_id: int, role: str, content: str) -> Message:
    """Create a chat message."""
    message = Message(interview_id=interview_id, role=role, content=content)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_messages_by_interview(
    db: Session, interview_id: int, limit: int | None = None
) -> list[Message]:
    """Get messages for an interview, ordered by time."""
    stmt = select(Message).where(Message.interview_id == interview_id).order_by(Message.created_at)
    if limit:
        stmt = stmt.limit(limit)
    return list(db.scalars(stmt).all())


def get_recent_messages(db: Session, interview_id: int, count: int = 8) -> list[Message]:
    """Get the most recent N messages for context."""
    stmt = (
        select(Message)
        .where(Message.interview_id == interview_id)
        .order_by(Message.created_at.desc())
        .limit(count)
    )
    # Reverse to get chronological order
    return list(reversed(db.scalars(stmt).all()))


# Insight CRUD


def create_insight(
    db: Session,
    interview_id: int,
    summary: str,
    sentiment: str,
    keywords_json: list,
    quotes_json: list,
) -> Insight:
    """Create interview insights."""
    insight = Insight(
        interview_id=interview_id,
        summary=summary,
        sentiment=sentiment,
        keywords_json=keywords_json,
        quotes_json=quotes_json,
    )
    db.add(insight)
    db.commit()
    db.refresh(insight)
    return insight


def get_insight_by_interview(db: Session, interview_id: int) -> Insight | None:
    """Get insight by interview ID."""
    stmt = select(Insight).where(Insight.interview_id == interview_id)
    return db.scalar(stmt)


def update_insight(
    db: Session,
    insight_id: int,
    summary: str | None = None,
    sentiment: str | None = None,
    keywords_json: list | None = None,
    quotes_json: list | None = None,
) -> Insight | None:
    """Update existing insight."""
    insight = db.get(Insight, insight_id)
    if insight:
        if summary is not None:
            insight.summary = summary
        if sentiment is not None:
            insight.sentiment = sentiment
        if keywords_json is not None:
            insight.keywords_json = keywords_json
        if quotes_json is not None:
            insight.quotes_json = quotes_json
        db.commit()
        db.refresh(insight)
    return insight

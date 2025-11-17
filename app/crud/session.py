"""CRUD operations for Session model."""

import secrets
from datetime import UTC, datetime, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from app.models.session import Session


def generate_session_id() -> str:
    """Generate a secure session ID."""
    return secrets.token_urlsafe(32)


def generate_csrf_secret() -> str:
    """Generate a CSRF secret."""
    return secrets.token_urlsafe(32)


def create_session(db: DBSession, user_id: int, expires_in_days: int = 7) -> Session:
    """Create a new session."""
    session_id = generate_session_id()
    csrf_secret = generate_csrf_secret()
    expires_at = datetime.now(UTC).replace(tzinfo=None) + timedelta(days=expires_in_days)

    session = Session(
        id=session_id, user_id=user_id, expires_at=expires_at, csrf_secret=csrf_secret
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def get_session_by_id(db: DBSession, session_id: str) -> Session | None:
    """Get session by ID."""
    return db.get(Session, session_id)


def get_sessions_by_user(db: DBSession, user_id: int) -> list[Session]:
    """Get all sessions for a user."""
    stmt = select(Session).where(Session.user_id == user_id)
    return list(db.scalars(stmt).all())


def is_session_valid(session: Session) -> bool:
    """Check if session is still valid (not expired)."""
    return session.expires_at > datetime.now(UTC).replace(tzinfo=None)


def delete_session(db: DBSession, session_id: str) -> bool:
    """Delete a session (logout)."""
    session = db.get(Session, session_id)
    if session:
        db.delete(session)
        db.commit()
        return True
    return False


def delete_expired_sessions(db: DBSession) -> int:
    """Delete all expired sessions. Returns count of deleted sessions."""
    stmt = select(Session).where(Session.expires_at < datetime.now(UTC).replace(tzinfo=None))
    expired = db.scalars(stmt).all()
    count = len(expired)
    for session in expired:
        db.delete(session)
    db.commit()
    return count


def delete_user_sessions(db: DBSession, user_id: int) -> int:
    """Delete all sessions for a user. Returns count of deleted sessions."""
    stmt = select(Session).where(Session.user_id == user_id)
    sessions = db.scalars(stmt).all()
    count = len(sessions)
    for session in sessions:
        db.delete(session)
    db.commit()
    return count

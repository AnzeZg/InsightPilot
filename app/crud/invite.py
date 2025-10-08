"""CRUD operations for Invite model."""

import secrets
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.invite import Invite, InviteStatus


def generate_invite_code() -> str:
    """Generate a unique invite code."""
    return secrets.token_urlsafe(32)


def create_invite(
    db: Session,
    study_id: int,
    interviewee_email: str | None = None,
    expires_at: datetime | None = None,
) -> Invite:
    """Create a new invite."""
    invite_code = generate_invite_code()
    invite = Invite(
        study_id=study_id,
        invite_code=invite_code,
        interviewee_email=interviewee_email,
        status=InviteStatus.CREATED.value,
        expires_at=expires_at,
    )
    db.add(invite)
    db.commit()
    db.refresh(invite)
    return invite


def get_invite_by_code(db: Session, invite_code: str) -> Invite | None:
    """Get invite by code."""
    stmt = select(Invite).where(Invite.invite_code == invite_code)
    return db.scalar(stmt)


def get_invite_by_id(db: Session, invite_id: int) -> Invite | None:
    """Get invite by ID."""
    return db.get(Invite, invite_id)


def get_invites_by_study(db: Session, study_id: int) -> list[Invite]:
    """Get all invites for a study."""
    stmt = select(Invite).where(Invite.study_id == study_id).order_by(Invite.created_at.desc())
    return list(db.scalars(stmt).all())


def update_invite_status(db: Session, invite_id: int, status: InviteStatus) -> Invite | None:
    """Update invite status."""
    invite = db.get(Invite, invite_id)
    if invite:
        invite.status = status.value
        db.commit()
        db.refresh(invite)
    return invite


def is_invite_valid(invite: Invite) -> bool:
    """Check if invite is valid (not expired, not completed)."""
    if invite.status == InviteStatus.COMPLETED.value:
        return False
    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return False
    return True


def delete_invite(db: Session, invite_id: int) -> bool:
    """Delete an invite."""
    invite = db.get(Invite, invite_id)
    if invite:
        db.delete(invite)
        db.commit()
        return True
    return False


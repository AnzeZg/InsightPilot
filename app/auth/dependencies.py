"""Authentication dependencies for route protection."""

from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.auth.sessions import get_session
from app.crud import session as session_crud
from app.db.session import get_db
from app.models.user import User


def get_current_session_id(request: Request) -> str:
    """Extract session ID from cookie."""
    session_id = get_session(request)
    if not session_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    return session_id


def get_current_user(
    session_id: str = Depends(get_current_session_id),
    db: Session = Depends(get_db),
) -> User:
    """Get current authenticated user from session."""
    session = session_crud.get_session_by_id(db, session_id)

    if not session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session",
        )

    if not session_crud.is_session_valid(session):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired",
        )

    user = db.get(User, session.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user

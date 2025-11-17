"""CRUD operations for User model."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def create_user(db: Session, email: str, password_hash: str) -> User:
    """Create a new user."""
    user = User(email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: int) -> User | None:
    """Get user by ID."""
    return db.get(User, user_id)


def get_user_by_email(db: Session, email: str) -> User | None:
    """Get user by email."""
    stmt = select(User).where(User.email == email)
    return db.scalar(stmt)


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """Get list of users with pagination."""
    stmt = select(User).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())


def update_user_password(db: Session, user_id: int, new_password_hash: str) -> User | None:
    """Update user password."""
    user = db.get(User, user_id)
    if user:
        user.password_hash = new_password_hash
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> bool:
    """Delete a user."""
    user = db.get(User, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

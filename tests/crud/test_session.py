"""Unit tests for session CRUD operations."""

from datetime import UTC, datetime, timedelta

import pytest

from app.crud import session as session_crud
from app.crud import user as user_crud


@pytest.fixture
def db_session(test_db):
    """Get a database session for testing."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_user(db_session):
    """Create a test user."""
    return user_crud.create_user(db_session, "testuser@example.com", "hash123")


def test_generate_session_id():
    """Test that session ID generation produces unique values."""
    id1 = session_crud.generate_session_id()
    id2 = session_crud.generate_session_id()

    assert len(id1) > 20  # Should be a long random string
    assert len(id2) > 20
    assert id1 != id2  # Should be unique


def test_generate_csrf_secret():
    """Test that CSRF secret generation produces unique values."""
    secret1 = session_crud.generate_csrf_secret()
    secret2 = session_crud.generate_csrf_secret()

    assert len(secret1) > 20
    assert len(secret2) > 20
    assert secret1 != secret2


def test_create_session(db_session, test_user):
    """Test creating a session."""
    session = session_crud.create_session(db_session, test_user.id)

    assert session.id is not None
    assert len(session.id) > 20  # Generated session ID
    assert session.user_id == test_user.id
    assert session.expires_at is not None
    assert session.csrf_secret is not None
    assert len(session.csrf_secret) > 20

    # Default expiration is 7 days
    expected_expiry = datetime.now(UTC).replace(tzinfo=None) + timedelta(days=7)
    # Allow 1 minute tolerance for test execution time
    assert abs((session.expires_at - expected_expiry).total_seconds()) < 60


def test_create_session_custom_expiry(db_session, test_user):
    """Test creating a session with custom expiration."""
    session = session_crud.create_session(db_session, test_user.id, expires_in_days=30)

    expected_expiry = datetime.now(UTC).replace(tzinfo=None) + timedelta(days=30)
    assert abs((session.expires_at - expected_expiry).total_seconds()) < 60


def test_get_session_by_id(db_session, test_user):
    """Test getting a session by ID."""
    created = session_crud.create_session(db_session, test_user.id)

    retrieved = session_crud.get_session_by_id(db_session, created.id)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.user_id == test_user.id


def test_get_session_by_id_not_found(db_session):
    """Test getting a non-existent session returns None."""
    result = session_crud.get_session_by_id(db_session, "nonexistent_session_id")
    assert result is None


def test_get_sessions_by_user(db_session, test_user):
    """Test getting all sessions for a user."""
    # Create multiple sessions for the same user
    session1 = session_crud.create_session(db_session, test_user.id)
    session2 = session_crud.create_session(db_session, test_user.id)

    sessions = session_crud.get_sessions_by_user(db_session, test_user.id)

    assert len(sessions) == 2
    session_ids = [s.id for s in sessions]
    assert session1.id in session_ids
    assert session2.id in session_ids


def test_get_sessions_by_user_empty(db_session, test_user):
    """Test getting sessions when none exist."""
    sessions = session_crud.get_sessions_by_user(db_session, test_user.id)
    assert sessions == []


def test_is_session_valid_active(db_session, test_user):
    """Test that a newly created session is valid."""
    session = session_crud.create_session(db_session, test_user.id)

    assert session_crud.is_session_valid(session) is True


def test_is_session_valid_expired(db_session, test_user):
    """Test that an expired session is not valid."""
    session = session_crud.create_session(db_session, test_user.id)

    # Manually set expiration to past
    session.expires_at = datetime.now(UTC).replace(tzinfo=None) - timedelta(days=1)
    db_session.commit()
    db_session.refresh(session)

    assert session_crud.is_session_valid(session) is False


def test_delete_session(db_session, test_user):
    """Test deleting a session."""
    session = session_crud.create_session(db_session, test_user.id)

    result = session_crud.delete_session(db_session, session.id)
    assert result is True

    # Verify it's gone
    retrieved = session_crud.get_session_by_id(db_session, session.id)
    assert retrieved is None


def test_delete_session_not_found(db_session):
    """Test deleting non-existent session returns False."""
    result = session_crud.delete_session(db_session, "nonexistent_id")
    assert result is False


def test_delete_expired_sessions(db_session, test_user):
    """Test deleting all expired sessions."""
    # Create active session
    active_session = session_crud.create_session(db_session, test_user.id)

    # Create expired session
    expired_session = session_crud.create_session(db_session, test_user.id)
    expired_session.expires_at = datetime.now(UTC).replace(tzinfo=None) - timedelta(days=1)
    db_session.commit()

    # Delete expired sessions
    count = session_crud.delete_expired_sessions(db_session)

    assert count == 1

    # Active session should still exist
    assert session_crud.get_session_by_id(db_session, active_session.id) is not None

    # Expired session should be gone
    assert session_crud.get_session_by_id(db_session, expired_session.id) is None


def test_delete_expired_sessions_none_expired(db_session, test_user):
    """Test deleting expired sessions when none are expired."""
    session_crud.create_session(db_session, test_user.id)
    session_crud.create_session(db_session, test_user.id)

    count = session_crud.delete_expired_sessions(db_session)

    assert count == 0


def test_delete_user_sessions(db_session):
    """Test deleting all sessions for a user."""
    user1 = user_crud.create_user(db_session, "user1@example.com", "hash1")
    user2 = user_crud.create_user(db_session, "user2@example.com", "hash2")

    # Create sessions for both users
    session1 = session_crud.create_session(db_session, user1.id)
    session2 = session_crud.create_session(db_session, user1.id)
    session3 = session_crud.create_session(db_session, user2.id)

    # Delete user1's sessions
    count = session_crud.delete_user_sessions(db_session, user1.id)

    assert count == 2

    # User1's sessions should be gone
    assert session_crud.get_session_by_id(db_session, session1.id) is None
    assert session_crud.get_session_by_id(db_session, session2.id) is None

    # User2's session should still exist
    assert session_crud.get_session_by_id(db_session, session3.id) is not None


def test_delete_user_sessions_none_exist(db_session, test_user):
    """Test deleting sessions when user has none."""
    count = session_crud.delete_user_sessions(db_session, test_user.id)
    assert count == 0


def test_session_isolation_between_users(db_session):
    """Test that sessions are properly isolated between users."""
    user1 = user_crud.create_user(db_session, "user1@example.com", "hash1")
    user2 = user_crud.create_user(db_session, "user2@example.com", "hash2")

    session1 = session_crud.create_session(db_session, user1.id)
    session2 = session_crud.create_session(db_session, user2.id)

    # Get sessions for user1
    user1_sessions = session_crud.get_sessions_by_user(db_session, user1.id)
    assert len(user1_sessions) == 1
    assert user1_sessions[0].id == session1.id

    # Get sessions for user2
    user2_sessions = session_crud.get_sessions_by_user(db_session, user2.id)
    assert len(user2_sessions) == 1
    assert user2_sessions[0].id == session2.id

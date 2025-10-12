"""Unit tests for authentication dependencies."""

import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

from fastapi import HTTPException
from starlette.requests import Request

from app.auth import dependencies
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


@pytest.fixture
def test_session(db_session, test_user):
    """Create a valid test session."""
    return session_crud.create_session(db_session, test_user.id)


@pytest.fixture
def mock_request_with_session(test_session):
    """Create a mock request with a valid session cookie."""
    request = MagicMock(spec=Request)
    
    # Mock the session cookie with proper serialization
    from app.auth.sessions import serializer, SESSION_COOKIE
    import time
    token = serializer.dumps({"sid": test_session.id, "ts": int(time.time())})
    request.cookies = {SESSION_COOKIE: token}
    
    return request


@pytest.fixture
def mock_request_no_session():
    """Create a mock request with no session cookie."""
    request = MagicMock(spec=Request)
    request.cookies = {}
    return request


# Tests for get_current_session_id


def test_get_current_session_id_valid(mock_request_with_session):
    """Test getting session ID from valid cookie."""
    session_id = dependencies.get_current_session_id(mock_request_with_session)
    
    assert session_id is not None
    assert isinstance(session_id, str)
    assert len(session_id) > 20  # Should be a long random string


def test_get_current_session_id_no_cookie(mock_request_no_session):
    """Test that missing cookie raises 401."""
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(mock_request_no_session)
    
    assert exc_info.value.status_code == 401
    assert "not authenticated" in exc_info.value.detail.lower()


def test_get_current_session_id_invalid_cookie():
    """Test that invalid cookie raises 401."""
    request = MagicMock(spec=Request)
    from app.auth.sessions import SESSION_COOKIE
    request.cookies = {SESSION_COOKIE: "invalid_token"}
    
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)
    
    assert exc_info.value.status_code == 401


def test_get_current_session_id_tampered_cookie():
    """Test that tampered cookie raises 401."""
    request = MagicMock(spec=Request)
    from app.auth.sessions import serializer, SESSION_COOKIE
    import time
    
    # Create valid token then tamper with it
    token = serializer.dumps({"sid": "test_session", "ts": int(time.time())})
    tampered = token[:-10] + "tampered123"
    request.cookies = {SESSION_COOKIE: tampered}
    
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)
    
    assert exc_info.value.status_code == 401


# Tests for get_current_user


def test_get_current_user_valid_session(db_session, test_user, test_session):
    """Test getting current user with valid session."""
    user = dependencies.get_current_user(test_session.id, db_session)
    
    assert user is not None
    assert user.id == test_user.id
    assert user.email == test_user.email


def test_get_current_user_invalid_session_id(db_session):
    """Test that invalid session ID raises 401."""
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user("nonexistent_session_id", db_session)
    
    assert exc_info.value.status_code == 401
    assert "invalid session" in exc_info.value.detail.lower()


def test_get_current_user_expired_session(db_session, test_user):
    """Test that expired session raises 401."""
    # Create expired session
    session = session_crud.create_session(db_session, test_user.id)
    
    # Manually expire the session
    session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=1)
    db_session.commit()
    db_session.refresh(session)
    
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user(session.id, db_session)
    
    assert exc_info.value.status_code == 401
    assert "expired" in exc_info.value.detail.lower()


def test_get_current_user_deleted_user(db_session, test_user, test_session):
    """Test that session with deleted user raises 401."""
    # Delete the user
    # Note: Due to CASCADE delete on foreign key, the session is also deleted
    user_crud.delete_user(db_session, test_user.id)
    
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user(test_session.id, db_session)
    
    assert exc_info.value.status_code == 401
    # Session is cascade-deleted with user, so we get "invalid session" error
    assert "invalid session" in exc_info.value.detail.lower()


def test_get_current_user_multiple_sessions(db_session, test_user):
    """Test that each session correctly identifies the user."""
    # Create multiple sessions for same user
    session1 = session_crud.create_session(db_session, test_user.id)
    session2 = session_crud.create_session(db_session, test_user.id)
    
    # Both sessions should return same user
    user1 = dependencies.get_current_user(session1.id, db_session)
    user2 = dependencies.get_current_user(session2.id, db_session)
    
    assert user1.id == test_user.id
    assert user2.id == test_user.id
    assert user1.id == user2.id


def test_get_current_user_different_users(db_session):
    """Test that sessions correctly identify different users."""
    user1 = user_crud.create_user(db_session, "user1@example.com", "hash1")
    user2 = user_crud.create_user(db_session, "user2@example.com", "hash2")
    
    session1 = session_crud.create_session(db_session, user1.id)
    session2 = session_crud.create_session(db_session, user2.id)
    
    retrieved_user1 = dependencies.get_current_user(session1.id, db_session)
    retrieved_user2 = dependencies.get_current_user(session2.id, db_session)
    
    assert retrieved_user1.id == user1.id
    assert retrieved_user2.id == user2.id
    assert retrieved_user1.id != retrieved_user2.id


def test_get_current_user_returns_fresh_data(db_session, test_user, test_session):
    """Test that get_current_user returns fresh user data."""
    # Get user initially
    user = dependencies.get_current_user(test_session.id, db_session)
    old_password_hash = user.password_hash
    
    # Update user password
    new_hash = "new_password_hash_123"
    user_crud.update_user_password(db_session, test_user.id, new_hash)
    
    # Get user again - should have new data
    user_refreshed = dependencies.get_current_user(test_session.id, db_session)
    
    assert user_refreshed.password_hash == new_hash
    assert user_refreshed.password_hash != old_password_hash


def test_get_current_user_session_validation_order(db_session, test_user):
    """Test that session validation happens before user lookup."""
    # Create expired session
    session = session_crud.create_session(db_session, test_user.id)
    session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=1)
    db_session.commit()
    
    # Even though user exists, expired session should fail first
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user(session.id, db_session)
    
    # Should get "expired" error, not "user not found"
    assert "expired" in exc_info.value.detail.lower()


def test_get_current_user_with_newly_created_session(db_session, test_user):
    """Test getting user immediately after session creation."""
    session = session_crud.create_session(db_session, test_user.id)
    
    # Should work immediately
    user = dependencies.get_current_user(session.id, db_session)
    
    assert user.id == test_user.id


def test_get_current_user_session_about_to_expire(db_session, test_user):
    """Test that session that's about to expire (but not yet) still works."""
    session = session_crud.create_session(db_session, test_user.id)
    
    # Set expiration to 1 second in the future
    session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(seconds=1)
    db_session.commit()
    db_session.refresh(session)
    
    # Should still be valid
    user = dependencies.get_current_user(session.id, db_session)
    assert user.id == test_user.id


def test_get_current_user_session_just_expired(db_session, test_user):
    """Test that session that just expired is invalid."""
    session = session_crud.create_session(db_session, test_user.id)
    
    # Set expiration to 1 second in the past
    session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(seconds=1)
    db_session.commit()
    db_session.refresh(session)
    
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user(session.id, db_session)
    
    assert exc_info.value.status_code == 401


# Integration tests


def test_full_auth_flow(db_session):
    """Test complete authentication flow from request to user."""
    # Create user
    user = user_crud.create_user(db_session, "fullflow@example.com", "hash123")
    
    # Create session
    session = session_crud.create_session(db_session, user.id)
    
    # Create request with session cookie
    from app.auth.sessions import serializer, SESSION_COOKIE
    import time
    token = serializer.dumps({"sid": session.id, "ts": int(time.time())})
    request = MagicMock(spec=Request)
    request.cookies = {SESSION_COOKIE: token}
    
    # Extract session ID from request
    session_id = dependencies.get_current_session_id(request)
    assert session_id == session.id
    
    # Get user from session
    retrieved_user = dependencies.get_current_user(session_id, db_session)
    assert retrieved_user.id == user.id
    assert retrieved_user.email == "fullflow@example.com"


def test_auth_flow_with_invalid_session(db_session):
    """Test auth flow fails gracefully with invalid session."""
    # Create request with invalid session
    request = MagicMock(spec=Request)
    from app.auth.sessions import SESSION_COOKIE
    request.cookies = {SESSION_COOKIE: "invalid_token"}
    
    # Should raise 401 at session extraction
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)
    
    assert exc_info.value.status_code == 401


def test_auth_flow_with_no_session(db_session):
    """Test auth flow fails gracefully with no session."""
    request = MagicMock(spec=Request)
    request.cookies = {}
    
    # Should raise 401 at session extraction
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)
    
    assert exc_info.value.status_code == 401


def test_error_messages_are_informative():
    """Test that error messages help with debugging."""
    request = MagicMock(spec=Request)
    request.cookies = {}
    
    # No session error
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)
    assert exc_info.value.detail  # Should have a message
    assert len(exc_info.value.detail) > 0


def test_get_current_user_preserves_user_model(db_session, test_user, test_session):
    """Test that returned user is a proper User model instance."""
    from app.models.user import User
    
    user = dependencies.get_current_user(test_session.id, db_session)
    
    assert isinstance(user, User)
    assert hasattr(user, "id")
    assert hasattr(user, "email")
    assert hasattr(user, "password_hash")
    assert hasattr(user, "created_at")


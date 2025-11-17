"""Unit tests for session cookie utilities."""

import time
from unittest.mock import MagicMock, patch

import pytest
from itsdangerous import URLSafeSerializer
from starlette.requests import Request
from starlette.responses import Response

from app.auth import sessions
from app.settings import settings


@pytest.fixture
def mock_response():
    """Create a mock response object."""
    response = MagicMock(spec=Response)
    response.set_cookie = MagicMock()
    response.delete_cookie = MagicMock()
    return response


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    request = MagicMock(spec=Request)
    request.cookies = {}
    return request


def test_serializer_initialization():
    """Test that serializer is initialized with correct settings."""
    assert sessions.serializer is not None
    assert isinstance(sessions.serializer, URLSafeSerializer)
    assert sessions.SESSION_COOKIE == settings.session_cookie_name


def test_set_session_basic(mock_response):
    """Test setting a session cookie."""
    session_id = "test_session_123"

    sessions.set_session(mock_response, session_id)

    # Verify set_cookie was called
    mock_response.set_cookie.assert_called_once()
    call_args = mock_response.set_cookie.call_args

    # Check cookie name (first positional arg)
    assert call_args[0][0] == settings.session_cookie_name

    # Check cookie value is a token (second positional arg)
    token = call_args[0][1]
    assert isinstance(token, str)
    assert len(token) > 20  # Serialized token should be long

    # Check kwargs
    assert call_args[1]["httponly"] is True
    assert call_args[1]["samesite"] == "lax"
    assert call_args[1]["secure"] == settings.is_production
    assert call_args[1]["max_age"] == 60 * 60 * 24 * 7  # Default 7 days


def test_set_session_custom_max_age(mock_response):
    """Test setting a session cookie with custom max_age."""
    session_id = "test_session_123"
    custom_max_age = 3600  # 1 hour

    sessions.set_session(mock_response, session_id, max_age=custom_max_age)

    call_args = mock_response.set_cookie.call_args
    assert call_args[1]["max_age"] == custom_max_age


def test_set_session_token_structure(mock_response):
    """Test that the session token contains correct data."""
    session_id = "test_session_123"

    with patch("time.time", return_value=1234567890.0):
        sessions.set_session(mock_response, session_id)

    # Extract the token that was set
    token = mock_response.set_cookie.call_args[0][1]

    # Deserialize and verify structure
    data = sessions.serializer.loads(token)
    assert data["sid"] == session_id
    assert data["ts"] == 1234567890
    assert isinstance(data["ts"], int)


def test_get_session_valid_token(mock_request):
    """Test getting session ID from valid cookie."""
    session_id = "test_session_123"

    # Create a valid token
    token = sessions.serializer.dumps({"sid": session_id, "ts": int(time.time())})
    mock_request.cookies = {settings.session_cookie_name: token}

    result = sessions.get_session(mock_request)

    assert result == session_id


def test_get_session_no_cookie(mock_request):
    """Test getting session when no cookie exists."""
    mock_request.cookies = {}

    result = sessions.get_session(mock_request)

    assert result is None


def test_get_session_invalid_token(mock_request):
    """Test getting session with invalid/corrupted token."""
    mock_request.cookies = {settings.session_cookie_name: "invalid_token_data"}

    result = sessions.get_session(mock_request)

    assert result is None


def test_get_session_tampered_token(mock_request):
    """Test getting session with tampered token."""
    # Create a valid token then tamper with it
    session_id = "test_session_123"
    token = sessions.serializer.dumps({"sid": session_id, "ts": int(time.time())})
    tampered_token = token[:-5] + "xxxxx"  # Tamper with the end

    mock_request.cookies = {settings.session_cookie_name: tampered_token}

    result = sessions.get_session(mock_request)

    assert result is None


def test_get_session_missing_sid(mock_request):
    """Test getting session when token is missing 'sid' key."""
    # Create token with wrong structure
    serializer = URLSafeSerializer(settings.secret_key, salt="session")
    token = serializer.dumps({"session_id": "test", "ts": int(time.time())})  # Wrong key

    mock_request.cookies = {settings.session_cookie_name: token}

    result = sessions.get_session(mock_request)

    # Should return None since 'sid' key is missing
    assert result is None


def test_get_session_different_secret_key(mock_request):
    """Test that tokens signed with different secret can't be validated."""
    session_id = "test_session_123"

    # Sign with different secret
    wrong_serializer = URLSafeSerializer("wrong_secret_key", salt="session")
    token = wrong_serializer.dumps({"sid": session_id, "ts": int(time.time())})

    mock_request.cookies = {settings.session_cookie_name: token}

    result = sessions.get_session(mock_request)

    assert result is None


def test_clear_session(mock_response):
    """Test clearing a session cookie."""
    sessions.clear_session(mock_response)

    mock_response.delete_cookie.assert_called_once_with(settings.session_cookie_name)


def test_roundtrip_session_set_and_get():
    """Test complete roundtrip: set cookie and retrieve session."""
    session_id = "roundtrip_test_session"

    # Set session
    mock_response = MagicMock(spec=Response)
    mock_response.set_cookie = MagicMock()
    sessions.set_session(mock_response, session_id)

    # Get the token that was set
    token = mock_response.set_cookie.call_args[0][1]

    # Create request with that token
    mock_request = MagicMock(spec=Request)
    mock_request.cookies = {settings.session_cookie_name: token}

    # Get session
    retrieved_session_id = sessions.get_session(mock_request)

    assert retrieved_session_id == session_id


def test_multiple_sessions_different_ids():
    """Test that different session IDs produce different tokens."""
    mock_response1 = MagicMock(spec=Response)
    mock_response2 = MagicMock(spec=Response)
    mock_response1.set_cookie = MagicMock()
    mock_response2.set_cookie = MagicMock()

    sessions.set_session(mock_response1, "session_1")
    sessions.set_session(mock_response2, "session_2")

    token1 = mock_response1.set_cookie.call_args[0][1]
    token2 = mock_response2.set_cookie.call_args[0][1]

    # Tokens should be different
    assert token1 != token2

    # But both should be valid
    data1 = sessions.serializer.loads(token1)
    data2 = sessions.serializer.loads(token2)

    assert data1["sid"] == "session_1"
    assert data2["sid"] == "session_2"


def test_session_cookie_security_flags():
    """Test that security flags are set correctly based on environment."""
    mock_response = MagicMock(spec=Response)
    mock_response.set_cookie = MagicMock()

    sessions.set_session(mock_response, "test_session")

    call_args = mock_response.set_cookie.call_args[1]

    # Verify security settings
    assert call_args["httponly"] is True  # Prevent XSS
    assert call_args["samesite"] == "lax"  # CSRF protection
    # Secure flag depends on environment
    assert call_args["secure"] == settings.is_production


def test_session_with_empty_string_id(mock_response):
    """Test setting session with empty string ID (edge case)."""
    sessions.set_session(mock_response, "")

    # Should still work
    mock_response.set_cookie.assert_called_once()
    token = mock_response.set_cookie.call_args[0][1]

    # Should be able to deserialize
    data = sessions.serializer.loads(token)
    assert data["sid"] == ""


def test_session_with_special_characters_id(mock_response):
    """Test setting session with special characters in ID."""
    special_id = "session!@#$%^&*()_+-=[]{}|;:',.<>?/"

    sessions.set_session(mock_response, special_id)

    token = mock_response.set_cookie.call_args[0][1]
    data = sessions.serializer.loads(token)

    assert data["sid"] == special_id


def test_session_timestamp_is_integer(mock_response):
    """Test that timestamp in token is an integer."""
    sessions.set_session(mock_response, "test_session")

    token = mock_response.set_cookie.call_args[0][1]
    data = sessions.serializer.loads(token)

    assert isinstance(data["ts"], int)
    assert data["ts"] > 0


def test_get_session_with_wrong_cookie_name(mock_request):
    """Test that wrong cookie name returns None."""
    session_id = "test_session"
    token = sessions.serializer.dumps({"sid": session_id, "ts": int(time.time())})

    # Set token with wrong cookie name
    mock_request.cookies = {"wrong_cookie_name": token}

    result = sessions.get_session(mock_request)

    assert result is None

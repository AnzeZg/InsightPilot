"""Tests for application constants."""

from app.constants import (
    AI_FREQUENCY_PENALTY,
    AI_INITIAL_MAX_TOKENS,
    AI_MAX_TOKENS,
    AI_PRESENCE_PENALTY,
    AI_TEMPERATURE,
    DEFAULT_AI_MODEL,
    DEV_DEFAULT_PASSWORD,
    DEV_TEST_USER_EMAIL,
    INSIGHT_GENERATION_TEMPERATURE,
    MAX_CONVERSATION_HISTORY,
    MAX_INTERVIEW_TURNS,
    MAX_MESSAGE_LENGTH,
    RECENT_MESSAGES_DEFAULT,
    SAMPLE_QUOTES_LIMIT,
    SESSION_COOKIE_SALT,
    SESSION_MAX_AGE_SECONDS,
    TOP_KEYWORDS_LIMIT,
)


def test_session_constants_are_defined():
    """Test that session constants are properly defined."""
    assert SESSION_MAX_AGE_SECONDS > 0
    assert SESSION_MAX_AGE_SECONDS == 60 * 60 * 24 * 7  # 7 days
    assert isinstance(SESSION_COOKIE_SALT, str)
    assert SESSION_COOKIE_SALT == "session"


def test_ai_agent_constants_are_defined():
    """Test that AI agent constants are properly defined."""
    assert isinstance(DEFAULT_AI_MODEL, str)
    assert DEFAULT_AI_MODEL == "gpt-4o-mini"
    assert AI_MAX_TOKENS > 0
    assert AI_TEMPERATURE >= 0 and AI_TEMPERATURE <= 2
    assert AI_INITIAL_MAX_TOKENS > 0
    assert AI_PRESENCE_PENALTY >= -2 and AI_PRESENCE_PENALTY <= 2
    assert AI_FREQUENCY_PENALTY >= -2 and AI_FREQUENCY_PENALTY <= 2


def test_insight_generation_constants():
    """Test insight generation constants."""
    assert INSIGHT_GENERATION_TEMPERATURE >= 0 and INSIGHT_GENERATION_TEMPERATURE <= 2


def test_analytics_constants():
    """Test analytics configuration constants."""
    assert TOP_KEYWORDS_LIMIT > 0
    assert SAMPLE_QUOTES_LIMIT > 0
    assert RECENT_MESSAGES_DEFAULT > 0
    assert MAX_CONVERSATION_HISTORY > 0


def test_dev_constants():
    """Test development/testing constants."""
    assert isinstance(DEV_DEFAULT_PASSWORD, str)
    assert len(DEV_DEFAULT_PASSWORD) > 0
    assert isinstance(DEV_TEST_USER_EMAIL, str)
    assert "@" in DEV_TEST_USER_EMAIL


def test_interview_constants():
    """Test interview configuration constants."""
    assert MAX_INTERVIEW_TURNS > 0
    assert MAX_MESSAGE_LENGTH > 0


def test_constants_relationships():
    """Test logical relationships between constants."""
    # Initial message tokens should be less than max tokens
    assert AI_INITIAL_MAX_TOKENS < AI_MAX_TOKENS
    # Sample quotes limit should be reasonable compared to keywords
    assert SAMPLE_QUOTES_LIMIT <= TOP_KEYWORDS_LIMIT


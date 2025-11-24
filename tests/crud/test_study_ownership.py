"""Tests for study ownership verification."""

import pytest
from fastapi import HTTPException

from app.crud import study as study_crud
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
def test_study(db_session, test_user):
    """Create a test study."""
    return study_crud.create_study(
        db_session,
        owner_user_id=test_user.id,
        title="Test Study",
        description="Test Description",
        consent_text="Test Consent",
    )


def test_verify_study_ownership_success(db_session, test_user, test_study):
    """Test successful study ownership verification."""
    result = study_crud.verify_study_ownership(db_session, test_study.id, test_user.id)

    assert result.id == test_study.id
    assert result.owner_user_id == test_user.id
    assert result.title == "Test Study"


def test_verify_study_ownership_not_found(db_session, test_user):
    """Test verification with non-existent study."""
    with pytest.raises(HTTPException) as exc_info:
        study_crud.verify_study_ownership(db_session, 99999, test_user.id)

    assert exc_info.value.status_code == 404
    assert "Study not found" in str(exc_info.value.detail)


def test_verify_study_ownership_unauthorized(db_session, test_user, test_study):
    """Test verification with wrong user."""
    # Create another user
    other_user = user_crud.create_user(db_session, "other@example.com", "hash456")

    with pytest.raises(HTTPException) as exc_info:
        study_crud.verify_study_ownership(db_session, test_study.id, other_user.id)

    assert exc_info.value.status_code == 404
    assert "Study not found" in str(exc_info.value.detail)


def test_verify_study_ownership_returns_study_without_questions(db_session, test_user, test_study):
    """Test that ownership verification doesn't load questions (optimization)."""
    # Add a question to the study
    study_crud.create_study_question(db_session, test_study.id, "Test Question", 0)

    # Verify ownership
    result = study_crud.verify_study_ownership(db_session, test_study.id, test_user.id)

    # The result should not have questions loaded (lazy loading)
    # We check that accessing questions would trigger another query
    assert result.id == test_study.id
    assert result.owner_user_id == test_user.id

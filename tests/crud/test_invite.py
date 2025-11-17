"""Unit tests for invite CRUD operations."""

from datetime import UTC, datetime, timedelta

import pytest

from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


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


def test_generate_invite_code():
    """Test that invite code generation produces unique values."""
    code1 = invite_crud.generate_invite_code()
    code2 = invite_crud.generate_invite_code()

    assert len(code1) > 20  # Should be a long random string
    assert len(code2) > 20
    assert code1 != code2  # Should be unique


def test_create_invite_basic(db_session, test_study):
    """Test creating a basic invite."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    assert invite.id is not None
    assert invite.study_id == test_study.id
    assert invite.invite_code is not None
    assert len(invite.invite_code) > 20
    assert invite.status == InviteStatus.CREATED.value
    assert invite.interviewee_email is None
    assert invite.expires_at is None
    assert invite.created_at is not None


def test_create_invite_with_email(db_session, test_study):
    """Test creating an invite with interviewee email."""
    email = "participant@example.com"
    invite = invite_crud.create_invite(db_session, test_study.id, interviewee_email=email)

    assert invite.interviewee_email == email


def test_create_invite_with_expiry(db_session, test_study):
    """Test creating an invite with expiration date."""
    expires_at = datetime.now(UTC).replace(tzinfo=None) + timedelta(days=7)
    invite = invite_crud.create_invite(db_session, test_study.id, expires_at=expires_at)

    assert invite.expires_at is not None
    # Allow 1 second tolerance
    assert abs((invite.expires_at - expires_at).total_seconds()) < 1


def test_create_invite_unique_codes(db_session, test_study):
    """Test that each invite gets a unique code."""
    invite1 = invite_crud.create_invite(db_session, test_study.id)
    invite2 = invite_crud.create_invite(db_session, test_study.id)

    assert invite1.invite_code != invite2.invite_code


def test_get_invite_by_code(db_session, test_study):
    """Test getting an invite by code."""
    created = invite_crud.create_invite(db_session, test_study.id)

    retrieved = invite_crud.get_invite_by_code(db_session, created.invite_code)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.invite_code == created.invite_code


def test_get_invite_by_code_not_found(db_session):
    """Test getting non-existent invite by code returns None."""
    result = invite_crud.get_invite_by_code(db_session, "nonexistent_code")
    assert result is None


def test_get_invite_by_id(db_session, test_study):
    """Test getting an invite by ID."""
    created = invite_crud.create_invite(db_session, test_study.id)

    retrieved = invite_crud.get_invite_by_id(db_session, created.id)

    assert retrieved is not None
    assert retrieved.id == created.id


def test_get_invite_by_id_not_found(db_session):
    """Test getting non-existent invite by ID returns None."""
    result = invite_crud.get_invite_by_id(db_session, 99999)
    assert result is None


def test_get_invites_by_study(db_session, test_study):
    """Test getting all invites for a study."""
    invite1 = invite_crud.create_invite(db_session, test_study.id)
    invite2 = invite_crud.create_invite(db_session, test_study.id)

    invites = invite_crud.get_invites_by_study(db_session, test_study.id)

    assert len(invites) == 2
    invite_ids = [i.id for i in invites]
    assert invite1.id in invite_ids
    assert invite2.id in invite_ids

    # Should be ordered by created_at desc (newest first)
    assert invites[0].id == invite2.id
    assert invites[1].id == invite1.id


def test_get_invites_by_study_empty(db_session, test_study):
    """Test getting invites when none exist."""
    invites = invite_crud.get_invites_by_study(db_session, test_study.id)
    assert invites == []


def test_invites_isolated_by_study(db_session, test_user):
    """Test that invites are isolated by study."""
    study1 = study_crud.create_study(db_session, test_user.id, "Study 1", "D", "C")
    study2 = study_crud.create_study(db_session, test_user.id, "Study 2", "D", "C")

    invite1 = invite_crud.create_invite(db_session, study1.id)
    invite2 = invite_crud.create_invite(db_session, study2.id)

    study1_invites = invite_crud.get_invites_by_study(db_session, study1.id)
    assert len(study1_invites) == 1
    assert study1_invites[0].id == invite1.id

    study2_invites = invite_crud.get_invites_by_study(db_session, study2.id)
    assert len(study2_invites) == 1
    assert study2_invites[0].id == invite2.id


def test_update_invite_status(db_session, test_study):
    """Test updating invite status."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    updated = invite_crud.update_invite_status(db_session, invite.id, InviteStatus.OPENED)

    assert updated is not None
    assert updated.id == invite.id
    assert updated.status == InviteStatus.OPENED.value


def test_update_invite_status_to_completed(db_session, test_study):
    """Test updating invite status to completed."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    updated = invite_crud.update_invite_status(db_session, invite.id, InviteStatus.COMPLETED)

    assert updated.status == InviteStatus.COMPLETED.value


def test_update_invite_status_not_found(db_session):
    """Test updating non-existent invite returns None."""
    result = invite_crud.update_invite_status(db_session, 99999, InviteStatus.OPENED)
    assert result is None


def test_is_invite_valid_new_invite(db_session, test_study):
    """Test that a newly created invite is valid."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    assert invite_crud.is_invite_valid(invite) is True


def test_is_invite_valid_completed(db_session, test_study):
    """Test that a completed invite is not valid."""
    invite = invite_crud.create_invite(db_session, test_study.id)
    invite_crud.update_invite_status(db_session, invite.id, InviteStatus.COMPLETED)

    # Refresh to get updated status
    updated_invite = invite_crud.get_invite_by_id(db_session, invite.id)

    assert invite_crud.is_invite_valid(updated_invite) is False


def test_is_invite_valid_expired(db_session, test_study):
    """Test that an expired invite is not valid."""
    past_date = datetime.now(UTC).replace(tzinfo=None) - timedelta(days=1)
    invite = invite_crud.create_invite(db_session, test_study.id, expires_at=past_date)

    assert invite_crud.is_invite_valid(invite) is False


def test_is_invite_valid_not_yet_expired(db_session, test_study):
    """Test that an invite with future expiry is valid."""
    future_date = datetime.now(UTC).replace(tzinfo=None) + timedelta(days=7)
    invite = invite_crud.create_invite(db_session, test_study.id, expires_at=future_date)

    assert invite_crud.is_invite_valid(invite) is True


def test_is_invite_valid_no_expiry(db_session, test_study):
    """Test that an invite with no expiry date is valid."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    assert invite.expires_at is None
    assert invite_crud.is_invite_valid(invite) is True


def test_delete_invite(db_session, test_study):
    """Test deleting an invite."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    result = invite_crud.delete_invite(db_session, invite.id)
    assert result is True

    # Verify it's gone
    retrieved = invite_crud.get_invite_by_id(db_session, invite.id)
    assert retrieved is None


def test_delete_invite_not_found(db_session):
    """Test deleting non-existent invite returns False."""
    result = invite_crud.delete_invite(db_session, 99999)
    assert result is False


def test_invite_status_transitions(db_session, test_study):
    """Test typical invite status transitions."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    # Initially CREATED
    assert invite.status == InviteStatus.CREATED.value

    # Open invite
    invite = invite_crud.update_invite_status(db_session, invite.id, InviteStatus.OPENED)
    assert invite.status == InviteStatus.OPENED.value

    # Complete interview
    invite = invite_crud.update_invite_status(db_session, invite.id, InviteStatus.COMPLETED)
    assert invite.status == InviteStatus.COMPLETED.value


def test_multiple_invites_for_same_study(db_session, test_study):
    """Test that multiple invites can be created for the same study."""
    invites = []
    for i in range(5):
        invite = invite_crud.create_invite(
            db_session,
            test_study.id,
            interviewee_email=f"participant{i}@example.com",
        )
        invites.append(invite)

    retrieved = invite_crud.get_invites_by_study(db_session, test_study.id)
    assert len(retrieved) == 5

    # All should have unique codes
    codes = [inv.invite_code for inv in retrieved]
    assert len(codes) == len(set(codes))  # No duplicates

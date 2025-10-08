"""Tests for invite landing page flow."""

from datetime import datetime, timedelta, timezone

import pytest
from httpx import AsyncClient

from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def db(test_db):
    """Create a database session for tests."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.mark.asyncio
async def test_invite_landing_page_valid(client: AsyncClient, db):
    """Test landing page with valid invite."""
    # Create test user and study
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hashed_password")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test study description",
        consent_text="I consent to participate",
    )
    
    # Create invite
    invite = invite_crud.create_invite(db, study_id=study.id)
    
    # Access landing page
    response = await client.get(f"/interview/{invite.invite_code}")
    
    assert response.status_code == 200
    assert "Test Study" in response.text
    assert "Test study description" in response.text
    assert "Continue to Consent Form" in response.text
    
    # Verify status updated to 'opened'
    db.refresh(invite)
    assert invite.status == InviteStatus.OPENED.value


@pytest.mark.asyncio
async def test_invite_landing_page_not_found(client: AsyncClient, db):
    """Test landing page with invalid invite code."""
    response = await client.get("/interview/invalid_code_12345")
    
    assert response.status_code == 404
    assert "Invitation Not Found" in response.text


@pytest.mark.asyncio
async def test_invite_landing_page_expired(client: AsyncClient, db):
    """Test landing page with expired invite."""
    # Create test user and study
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hashed_password")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test study description",
        consent_text="I consent to participate",
    )
    
    # Create expired invite
    expired_time = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(hours=1)
    invite = invite_crud.create_invite(
        db,
        study_id=study.id,
        expires_at=expired_time,
    )
    
    # Access landing page
    response = await client.get(f"/interview/{invite.invite_code}")
    
    assert response.status_code == 200
    assert "Invite Has Expired" in response.text


@pytest.mark.asyncio
async def test_invite_landing_page_completed(client: AsyncClient, db):
    """Test landing page with completed invite."""
    # Create test user and study
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hashed_password")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test study description",
        consent_text="I consent to participate",
    )
    
    # Create invite and mark as completed
    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
    
    # Access landing page
    response = await client.get(f"/interview/{invite.invite_code}")
    
    assert response.status_code == 200
    assert "Already Completed" in response.text


@pytest.mark.asyncio
async def test_invite_status_only_updated_once(client: AsyncClient, db):
    """Test that invite status is only updated to 'opened' once."""
    # Create test user and study
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hashed_password")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test study description",
        consent_text="I consent to participate",
    )
    
    # Create invite
    invite = invite_crud.create_invite(db, study_id=study.id)
    assert invite.status == InviteStatus.CREATED.value
    
    # First visit - should update to 'opened'
    response = await client.get(f"/interview/{invite.invite_code}")
    assert response.status_code == 200
    db.refresh(invite)
    assert invite.status == InviteStatus.OPENED.value
    
    # Second visit - should remain 'opened'
    response = await client.get(f"/interview/{invite.invite_code}")
    assert response.status_code == 200
    db.refresh(invite)
    assert invite.status == InviteStatus.OPENED.value


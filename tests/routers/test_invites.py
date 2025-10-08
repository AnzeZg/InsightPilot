"""Tests for invites routes."""

import pytest
from httpx import AsyncClient


@pytest.fixture
async def test_study(authenticated_client: AsyncClient):
    """Create a test study and return its ID."""
    response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Test Study",
            "description": "For testing invites",
            "consent_text": "I consent",
        },
    )
    return response.json()["id"]


@pytest.mark.asyncio
async def test_create_invite(authenticated_client: AsyncClient, test_study):
    """Test creating an invite."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={},
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["study_id"] == test_study
    assert "invite_code" in data
    assert len(data["invite_code"]) > 20  # Should be a long random string
    assert data["status"] == "created"


@pytest.mark.asyncio
async def test_create_invite_with_email(authenticated_client: AsyncClient, test_study):
    """Test creating an invite with interviewee email."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={"interviewee_email": "participant@example.com"},
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["interviewee_email"] == "participant@example.com"


@pytest.mark.asyncio
async def test_create_invite_invalid_email(authenticated_client: AsyncClient, test_study):
    """Test creating invite with invalid email fails."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={"interviewee_email": "not-an-email"},
    )
    
    assert response.status_code == 422  # Validation error


@pytest.mark.asyncio
async def test_list_invites(authenticated_client: AsyncClient, test_study):
    """Test listing invites for a study."""
    # Create invites
    await authenticated_client.post(f"/studies/{test_study}/invites", json={})
    await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={"interviewee_email": "person@example.com"},
    )
    
    # List invites
    response = await authenticated_client.get(f"/studies/{test_study}/invites")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all("invite_code" in invite for invite in data)


@pytest.mark.asyncio
async def test_delete_invite(authenticated_client: AsyncClient, test_study):
    """Test deleting an invite."""
    # Create invite
    create_response = await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={},
    )
    invite_id = create_response.json()["id"]
    
    # Delete invite
    response = await authenticated_client.delete(
        f"/studies/{test_study}/invites/{invite_id}"
    )
    assert response.status_code == 204
    
    # Verify it's gone
    list_response = await authenticated_client.get(f"/studies/{test_study}/invites")
    assert len(list_response.json()) == 0


@pytest.mark.asyncio
async def test_invite_codes_unique(authenticated_client: AsyncClient, test_study):
    """Test that each invite gets a unique code."""
    invite1 = await authenticated_client.post(f"/studies/{test_study}/invites", json={})
    invite2 = await authenticated_client.post(f"/studies/{test_study}/invites", json={})
    
    code1 = invite1.json()["invite_code"]
    code2 = invite2.json()["invite_code"]
    
    assert code1 != code2


@pytest.mark.asyncio
async def test_invites_isolated_by_study(authenticated_client: AsyncClient):
    """Test invites from one study don't appear in another."""
    # Create two studies
    study1_response = await authenticated_client.post(
        "/studies/",
        json={"title": "Study 1", "description": "First", "consent_text": "Consent"},
    )
    study2_response = await authenticated_client.post(
        "/studies/",
        json={"title": "Study 2", "description": "Second", "consent_text": "Consent"},
    )
    
    study1_id = study1_response.json()["id"]
    study2_id = study2_response.json()["id"]
    
    # Create invite for study 1
    await authenticated_client.post(f"/studies/{study1_id}/invites", json={})
    
    # Study 2 should have no invites
    study2_invites = await authenticated_client.get(f"/studies/{study2_id}/invites")
    assert len(study2_invites.json()) == 0



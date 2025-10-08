"""Tests for studies routes."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_study(authenticated_client: AsyncClient):
    """Test creating a study."""
    response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Product Feedback Study",
            "description": "Understanding user needs for our product",
            "consent_text": "I consent to participate in this research",
            "max_agent_turns": 10,
        },
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Product Feedback Study"
    assert data["max_agent_turns"] == 10
    assert "id" in data
    assert "created_at" in data


@pytest.mark.asyncio
async def test_create_study_unauthenticated(client: AsyncClient):
    """Test creating a study without auth fails."""
    response = await client.post(
        "/studies/",
        json={
            "title": "Test Study",
            "description": "Test",
            "consent_text": "I consent",
        },
    )
    
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_list_studies(authenticated_client: AsyncClient):
    """Test listing studies returns only user's studies."""
    # Create two studies
    await authenticated_client.post(
        "/studies/",
        json={
            "title": "Study 1",
            "description": "First study",
            "consent_text": "Consent",
        },
    )
    await authenticated_client.post(
        "/studies/",
        json={
            "title": "Study 2",
            "description": "Second study",
            "consent_text": "Consent",
        },
    )
    
    # List studies
    response = await authenticated_client.get("/studies/")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(isinstance(study, dict) for study in data)


@pytest.mark.asyncio
async def test_get_study(authenticated_client: AsyncClient):
    """Test getting a specific study."""
    # Create study
    create_response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Test Study",
            "description": "Description",
            "consent_text": "Consent",
        },
    )
    study_id = create_response.json()["id"]
    
    # Get study
    response = await authenticated_client.get(f"/studies/{study_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == study_id
    assert data["title"] == "Test Study"


@pytest.mark.asyncio
async def test_get_nonexistent_study(authenticated_client: AsyncClient):
    """Test getting non-existent study returns 404."""
    response = await authenticated_client.get("/studies/99999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_study(authenticated_client: AsyncClient):
    """Test updating a study."""
    # Create study
    create_response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Original Title",
            "description": "Original Description",
            "consent_text": "Consent",
        },
    )
    study_id = create_response.json()["id"]
    
    # Update study
    response = await authenticated_client.patch(
        f"/studies/{study_id}",
        json={"title": "Updated Title"},
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["description"] == "Original Description"  # Unchanged


@pytest.mark.asyncio
async def test_delete_study(authenticated_client: AsyncClient):
    """Test deleting a study."""
    # Create study
    create_response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "To Delete",
            "description": "Will be deleted",
            "consent_text": "Consent",
        },
    )
    study_id = create_response.json()["id"]
    
    # Delete study
    response = await authenticated_client.delete(f"/studies/{study_id}")
    assert response.status_code == 204
    
    # Verify it's gone
    get_response = await authenticated_client.get(f"/studies/{study_id}")
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_create_study_validation(authenticated_client: AsyncClient):
    """Test study creation validates required fields."""
    response = await authenticated_client.post(
        "/studies/",
        json={"title": ""},  # Empty title should fail
    )
    
    assert response.status_code == 422  # Validation error



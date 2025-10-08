"""Tests for study questions routes."""

import pytest
from httpx import AsyncClient


@pytest.fixture
async def test_study(authenticated_client: AsyncClient):
    """Create a test study and return its ID."""
    response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Test Study",
            "description": "For testing questions",
            "consent_text": "I consent",
        },
    )
    return response.json()["id"]


@pytest.mark.asyncio
async def test_create_question(authenticated_client: AsyncClient, test_study):
    """Test adding a question to a study."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "What is your biggest challenge?", "sort_order": 0},
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["text"] == "What is your biggest challenge?"
    assert data["sort_order"] == 0
    assert data["study_id"] == test_study


@pytest.mark.asyncio
async def test_list_questions(authenticated_client: AsyncClient, test_study):
    """Test listing questions returns them in order."""
    # Create questions
    await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "Question 1", "sort_order": 0},
    )
    await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "Question 2", "sort_order": 1},
    )
    await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "Question 3", "sort_order": 2},
    )
    
    # List questions
    response = await authenticated_client.get(f"/studies/{test_study}/questions")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["text"] == "Question 1"
    assert data[1]["text"] == "Question 2"
    assert data[2]["text"] == "Question 3"


@pytest.mark.asyncio
async def test_reorder_questions(authenticated_client: AsyncClient, test_study):
    """Test reordering questions."""
    # Create questions
    q1 = await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "First", "sort_order": 0},
    )
    q2 = await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "Second", "sort_order": 1},
    )
    
    q1_id = q1.json()["id"]
    q2_id = q2.json()["id"]
    
    # Reorder (swap them)
    response = await authenticated_client.post(
        f"/studies/{test_study}/questions/reorder",
        json={
            "updates": [
                {"question_id": q1_id, "sort_order": 1},
                {"question_id": q2_id, "sort_order": 0},
            ]
        },
    )
    
    assert response.status_code == 204
    
    # Verify new order
    list_response = await authenticated_client.get(f"/studies/{test_study}/questions")
    questions = list_response.json()
    assert questions[0]["text"] == "Second"  # Now first
    assert questions[1]["text"] == "First"  # Now second


@pytest.mark.asyncio
async def test_reorder_invalid_question(authenticated_client: AsyncClient, test_study):
    """Test reordering with invalid question ID fails."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/questions/reorder",
        json={
            "updates": [
                {"question_id": 99999, "sort_order": 0},  # Doesn't exist
            ]
        },
    )
    
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_delete_question(authenticated_client: AsyncClient, test_study):
    """Test deleting a question."""
    # Create question
    create_response = await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "To delete", "sort_order": 0},
    )
    question_id = create_response.json()["id"]
    
    # Delete question
    response = await authenticated_client.delete(
        f"/studies/{test_study}/questions/{question_id}"
    )
    assert response.status_code == 204
    
    # Verify it's gone
    list_response = await authenticated_client.get(f"/studies/{test_study}/questions")
    assert len(list_response.json()) == 0


@pytest.mark.asyncio
async def test_questions_isolated_by_study(authenticated_client: AsyncClient):
    """Test questions from one study don't appear in another."""
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
    
    # Add question to study 1
    await authenticated_client.post(
        f"/studies/{study1_id}/questions",
        json={"text": "Study 1 question", "sort_order": 0},
    )
    
    # Study 2 should have no questions
    study2_questions = await authenticated_client.get(f"/studies/{study2_id}/questions")
    assert len(study2_questions.json()) == 0


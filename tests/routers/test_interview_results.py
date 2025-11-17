"""Tests for interview results API endpoints."""

import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def db(test_db):
    """Get database session from test_db fixture."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def researcher_with_study(db: Session, test_user):
    """Create a researcher user with a study and completed interview."""
    user = user_crud.get_user_by_email(db, test_user["email"])

    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Product Research",
        description="Understanding user experience",
        consent_text="Test consent",
        max_agent_turns=5,
    )

    study_crud.create_study_question(
        db, study_id=study.id, text="What do you think about the product?", sort_order=0
    )

    study_crud.create_study_question(
        db, study_id=study.id, text="How can we improve?", sort_order=1
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
        demographics_json={"age_range": "25-34", "location": "USA"},
    )

    interview_crud.create_message(
        db, interview_id=interview.id, role="assistant", content="Hello! What brings you here?"
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="user",
        content="I really love the new design. The interface is very intuitive.",
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="assistant",
        content="That's great to hear! Can you tell me more?",
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="user",
        content="The navigation is smooth and all the features I need are easily accessible.",
    )

    interview_crud.complete_interview(db, interview.id)

    interview_crud.create_insight(
        db,
        interview_id=interview.id,
        summary="Participant expressed positive sentiment about the product design and usability.",
        sentiment="positive",
        keywords_json=["design", "interface", "navigation", "features"],
        quotes_json=[
            "I really love the new design. The interface is very intuitive.",
            "The navigation is smooth and all the features I need are easily accessible.",
        ],
    )

    return {"user": user, "study": study, "interview": interview}


@pytest.mark.asyncio
async def test_list_interviews_success(
    authenticated_client: AsyncClient, db: Session, researcher_with_study
):
    """Test listing interviews for a study."""
    study = researcher_with_study["study"]

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews",
    )

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    interview = data[0]

    assert interview["study_id"] == study.id
    assert interview["completed_at"] is not None
    assert interview["interviewee"]["name"] == "Test User"
    assert interview["interviewee"]["email"] == "test@example.com"
    assert interview["insight"]["sentiment"] == "positive"
    assert interview["insight"]["summary"] is not None
    assert len(interview["insight"]["keywords_json"]) > 0
    assert interview["message_count"] == 4


@pytest.mark.asyncio
async def test_list_interviews_empty_study(
    authenticated_client: AsyncClient, test_user, db: Session
):
    """Test listing interviews for a study with no interviews."""
    user = user_crud.get_user_by_email(db, test_user["email"])
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Empty Study",
        description="No interviews yet",
        consent_text="Test",
    )

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews",
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 0


@pytest.mark.asyncio
async def test_list_interviews_unauthorized(
    client: AsyncClient, db: Session, researcher_with_study
):
    """Test that unauthorized users cannot list interviews."""
    study = researcher_with_study["study"]

    # Create another user properly using registration endpoint
    await client.post(
        "/auth/dev/register",
        data={"email": "other@test.com", "password": "testpass123"},
    )

    # Login as the other user
    response = await client.post(
        "/auth/dev/login",
        data={"email": "other@test.com", "password": "testpass123"},
        follow_redirects=False,
    )

    response = await client.get(
        f"/studies/{study.id}/interviews",
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_list_interviews_no_auth(client: AsyncClient, db: Session, researcher_with_study):
    """Test that unauthenticated requests are rejected."""
    study = researcher_with_study["study"]

    response = await client.get(f"/studies/{study.id}/interviews")

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_interview_transcript_success(
    authenticated_client: AsyncClient, db: Session, researcher_with_study
):
    """Test getting full interview transcript."""
    study = researcher_with_study["study"]
    interview = researcher_with_study["interview"]

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/{interview.id}",
    )

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == interview.id
    assert data["study_id"] == study.id
    assert data["completed_at"] is not None

    assert data["interviewee"]["name"] == "Test User"
    assert data["interviewee"]["demographics_json"]["age_range"] == "25-34"

    assert len(data["messages"]) == 4
    assert data["messages"][0]["role"] == "assistant"
    assert data["messages"][1]["role"] == "user"
    assert "Hello" in data["messages"][0]["content"]

    assert data["insight"] is not None
    assert data["insight"]["sentiment"] == "positive"
    assert len(data["insight"]["keywords_json"]) == 4
    assert len(data["insight"]["quotes_json"]) == 2


@pytest.mark.asyncio
async def test_get_interview_transcript_not_found(
    authenticated_client: AsyncClient, test_user, db: Session
):
    """Test getting transcript for non-existent interview."""
    user = user_crud.get_user_by_email(db, test_user["email"])
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test",
        consent_text="Test",
    )

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/99999",
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_interview_transcript_wrong_study(
    authenticated_client: AsyncClient, db: Session, researcher_with_study
):
    """Test that interview cannot be accessed from wrong study."""
    user = researcher_with_study["user"]
    interview = researcher_with_study["interview"]

    other_study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Other Study",
        description="Different study",
        consent_text="Test",
    )

    response = await authenticated_client.get(
        f"/studies/{other_study.id}/interviews/{interview.id}",
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_interview_transcript_unauthorized(
    client: AsyncClient, db: Session, researcher_with_study
):
    """Test that unauthorized users cannot view transcripts."""
    study = researcher_with_study["study"]
    interview = researcher_with_study["interview"]

    # Create another user properly using registration endpoint
    await client.post(
        "/auth/dev/register",
        data={"email": "other@test.com", "password": "testpass123"},
    )

    # Login as the other user
    await client.post(
        "/auth/dev/login",
        data={"email": "other@test.com", "password": "testpass123"},
        follow_redirects=False,
    )

    response = await client.get(
        f"/studies/{study.id}/interviews/{interview.id}",
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_list_interviews_multiple_interviews(
    authenticated_client: AsyncClient, test_user, db: Session
):
    """Test listing multiple interviews with different statuses."""
    user = user_crud.get_user_by_email(db, test_user["email"])
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Multi-Interview Study",
        description="Test",
        consent_text="Test",
    )

    for i in range(3):
        invite = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
        interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

        interview_crud.create_interviewee(
            db, interview_id=interview.id, name=f"User {i}", email=f"user{i}@test.com"
        )

        interview_crud.create_message(
            db, interview_id=interview.id, role="assistant", content="Hello"
        )
        interview_crud.create_message(
            db, interview_id=interview.id, role="user", content="Hi there"
        )

        if i < 2:
            interview_crud.complete_interview(db, interview.id)
            interview_crud.create_insight(
                db,
                interview_id=interview.id,
                summary="Test summary",
                sentiment="neutral",
                keywords_json=["test"],
                quotes_json=["Hi there"],
            )

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews",
    )

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 3

    completed = [d for d in data if d["completed_at"] is not None]
    in_progress = [d for d in data if d["completed_at"] is None]

    assert len(completed) == 2
    assert len(in_progress) == 1

    for interview in completed:
        assert interview["insight"] is not None

    for interview in in_progress:
        assert interview["insight"] is None

"""Tests for study analytics endpoint."""

import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def study_with_varied_interviews(test_db, test_user):
    """Create a study with multiple interviews with varied data."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Analytics Test Study",
            description="Study for testing analytics",
            consent_text="Test consent",
            max_agent_turns=5,
        )
        
        # Interview 1: Positive sentiment
        invite1 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite1.id, InviteStatus.COMPLETED)
        interview1 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite1.id)
        
        interview_crud.create_interviewee(
            db,
            interview_id=interview1.id,
            name="Alice Smith",
            email="alice@example.com",
            demographics_json={"age_range": "25-34", "location": "USA", "occupation": "Engineer"},
        )
        
        interview_crud.create_message(
            db, interview_id=interview1.id, role="assistant", content="Hello!"
        )
        interview_crud.create_message(
            db, interview_id=interview1.id, role="user", content="This product is amazing and intuitive!"
        )
        interview_crud.create_message(
            db, interview_id=interview1.id, role="assistant", content="Great to hear!"
        )
        interview_crud.create_message(
            db, interview_id=interview1.id, role="user", content="I love using it every day."
        )
        
        interview_crud.complete_interview(db, interview1.id)
        interview_crud.create_insight(
            db,
            interview_id=interview1.id,
            summary="User loves the product",
            sentiment="positive",
            keywords_json=["product", "amazing", "intuitive", "love"],
            quotes_json=["This product is amazing and intuitive!", "I love using it every day."],
        )
        
        # Interview 2: Neutral sentiment
        invite2 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite2.id, InviteStatus.COMPLETED)
        interview2 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite2.id)
        
        interview_crud.create_interviewee(
            db,
            interview_id=interview2.id,
            name="Bob Jones",
            email="bob@example.com",
            demographics_json={"age_range": "35-44", "location": "Canada", "occupation": "Designer"},
        )
        
        interview_crud.create_message(
            db, interview_id=interview2.id, role="assistant", content="Hello!"
        )
        interview_crud.create_message(
            db, interview_id=interview2.id, role="user", content="The product is okay, nothing special."
        )
        
        interview_crud.complete_interview(db, interview2.id)
        interview_crud.create_insight(
            db,
            interview_id=interview2.id,
            summary="User finds it adequate",
            sentiment="neutral",
            keywords_json=["product", "okay"],
            quotes_json=["The product is okay, nothing special."],
        )
        
        # Interview 3: Negative sentiment
        invite3 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite3.id, InviteStatus.COMPLETED)
        interview3 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite3.id)
        
        interview_crud.create_interviewee(
            db,
            interview_id=interview3.id,
            name="Charlie Brown",
            email="charlie@example.com",
            demographics_json={"age_range": "25-34", "location": "USA", "occupation": "Manager"},
        )
        
        interview_crud.create_message(
            db, interview_id=interview3.id, role="assistant", content="Hi!"
        )
        interview_crud.create_message(
            db, interview_id=interview3.id, role="user", content="I'm frustrated with the interface."
        )
        interview_crud.create_message(
            db, interview_id=interview3.id, role="assistant", content="Sorry to hear that"
        )
        interview_crud.create_message(
            db, interview_id=interview3.id, role="user", content="It's confusing."
        )
        
        interview_crud.complete_interview(db, interview3.id)
        interview_crud.create_insight(
            db,
            interview_id=interview3.id,
            summary="User frustrated with interface",
            sentiment="negative",
            keywords_json=["interface", "frustrated", "confusing"],
            quotes_json=["I'm frustrated with the interface."],
        )
        
        # Interview 4: In progress (not completed)
        invite4 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite4.id, InviteStatus.OPENED)
        interview4 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite4.id)
        
        interview_crud.create_interviewee(
            db,
            interview_id=interview4.id,
            name="Diana Prince",
            email="diana@example.com",
            demographics_json={"age_range": "45-54", "location": "UK"},
        )
        
        interview_crud.create_message(
            db, interview_id=interview4.id, role="assistant", content="Welcome!"
        )
        
        yield {"user": user, "study": study, "interviews": [interview1, interview2, interview3, interview4]}
    finally:
        db.close()


@pytest.mark.asyncio
async def test_get_analytics_success(
    authenticated_client: AsyncClient, study_with_varied_interviews
):
    """Test retrieving analytics for a study with varied data."""
    study = study_with_varied_interviews["study"]
    
    response = await authenticated_client.get(
        f"/studies/{study.id}/analytics"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Basic counts
    assert data["study_id"] == study.id
    assert data["study_title"] == "Analytics Test Study"
    assert data["total_interviews"] == 4
    assert data["completed_interviews"] == 3
    
    # Sentiment distribution
    sentiment = data["sentiment_distribution"]
    assert sentiment["positive"] == 1
    assert sentiment["neutral"] == 1
    assert sentiment["negative"] == 1
    assert sentiment["total"] == 3
    
    # Keywords
    keywords = data["top_keywords"]
    assert len(keywords) > 0
    # "product" appears in 2 completed interviews (1 and 2)
    product_kw = next((kw for kw in keywords if kw["keyword"] == "product"), None)
    assert product_kw is not None
    assert product_kw["count"] == 2
    
    # Response metrics
    metrics = data["response_metrics"]
    assert metrics["total_messages"] > 0
    assert metrics["avg_message_count"] > 0
    assert metrics["avg_response_length"] > 0
    
    # Demographics
    demographics = data["demographics"]
    assert len(demographics) > 0
    
    # Check age_range demographic
    age_demo = next((d for d in demographics if d["field"] == "age_range"), None)
    assert age_demo is not None
    assert age_demo["values"]["25-34"] == 2  # Alice and Charlie
    assert age_demo["values"]["35-44"] == 1  # Bob
    assert age_demo["values"]["45-54"] == 1  # Diana
    
    # Check location demographic
    location_demo = next((d for d in demographics if d["field"] == "location"), None)
    assert location_demo is not None
    assert location_demo["values"]["USA"] == 2
    assert location_demo["values"]["Canada"] == 1
    assert location_demo["values"]["UK"] == 1
    
    # Timeline
    timeline = data["timeline"]
    assert len(timeline) > 0
    # All interviews started on same day in test
    assert timeline[0]["completed"] == 3
    assert timeline[0]["in_progress"] == 1
    
    # Sample quotes
    quotes = data["sample_quotes"]
    assert len(quotes) > 0
    assert "This product is amazing and intuitive!" in quotes


@pytest.mark.asyncio
async def test_get_analytics_empty_study(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test analytics for a study with no interviews."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Empty Study",
            description="No interviews",
            consent_text="Test",
        )
        
        response = await authenticated_client.get(
            f"/studies/{study.id}/analytics"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["total_interviews"] == 0
        assert data["completed_interviews"] == 0
        assert data["sentiment_distribution"]["total"] == 0
        assert len(data["top_keywords"]) == 0
        assert data["response_metrics"]["total_messages"] == 0
        assert len(data["demographics"]) == 0
        assert len(data["timeline"]) == 0
        assert len(data["sample_quotes"]) == 0
    finally:
        db.close()


@pytest.mark.asyncio
async def test_get_analytics_unauthorized(
    client: AsyncClient, study_with_varied_interviews
):
    """Test that unauthorized users cannot access analytics."""
    study = study_with_varied_interviews["study"]
    
    # Create and login as different user
    await client.post(
        "/auth/dev/register",
        data={"email": "other@example.com", "password": "testpass123"},
    )
    
    await client.post(
        "/auth/dev/login",
        data={"email": "other@example.com", "password": "testpass123"},
        follow_redirects=False,
    )
    
    response = await client.get(
        f"/studies/{study.id}/analytics"
    )
    
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_analytics_no_auth(
    client: AsyncClient, study_with_varied_interviews
):
    """Test that unauthenticated requests are rejected."""
    study = study_with_varied_interviews["study"]
    
    response = await client.get(f"/studies/{study.id}/analytics")
    
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_analytics_not_found(
    authenticated_client: AsyncClient
):
    """Test analytics for non-existent study."""
    response = await authenticated_client.get("/studies/99999/analytics")
    
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_analytics_keyword_frequency(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test keyword frequency calculation."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Keyword Test",
            description="Test",
            consent_text="Test",
        )
        
        # Create interviews with overlapping keywords
        for i in range(3):
            invite = invite_crud.create_invite(db, study_id=study.id)
            invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
            interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
            
            interview_crud.create_interviewee(
                db, interview_id=interview.id, name=f"User {i}", email=f"user{i}@test.com"
            )
            
            interview_crud.create_message(
                db, interview_id=interview.id, role="user", content="Test"
            )
            
            interview_crud.complete_interview(db, interview.id)
            
            # All have "design", two have "interface"
            keywords = ["design"]
            if i < 2:
                keywords.append("interface")
            
            interview_crud.create_insight(
                db,
                interview_id=interview.id,
                summary="Test",
                sentiment="neutral",
                keywords_json=keywords,
                quotes_json=[],
            )
        
        response = await authenticated_client.get(f"/studies/{study.id}/analytics")
        
        assert response.status_code == 200
        data = response.json()
        
        keywords = {kw["keyword"]: kw["count"] for kw in data["top_keywords"]}
        assert keywords["design"] == 3
        assert keywords["interface"] == 2
    finally:
        db.close()


@pytest.mark.asyncio
async def test_get_analytics_response_metrics(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test response metrics calculation."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Metrics Test",
            description="Test",
            consent_text="Test",
        )
        
        invite = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
        interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
        
        interview_crud.create_interviewee(
            db, interview_id=interview.id, name="Test User", email="test@example.com"
        )
        
        # Add messages with known lengths
        interview_crud.create_message(
            db, interview_id=interview.id, role="assistant", content="Hello there!"  # 12 chars
        )
        interview_crud.create_message(
            db, interview_id=interview.id, role="user", content="Hi!"  # 3 chars
        )
        interview_crud.create_message(
            db, interview_id=interview.id, role="user", content="How are you?"  # 12 chars
        )
        
        interview_crud.complete_interview(db, interview.id)
        interview_crud.create_insight(
            db, interview_id=interview.id, summary="Test", sentiment="neutral",
            keywords_json=[], quotes_json=[]
        )
        
        response = await authenticated_client.get(f"/studies/{study.id}/analytics")
        
        assert response.status_code == 200
        data = response.json()
        
        metrics = data["response_metrics"]
        assert metrics["total_messages"] == 3
        assert metrics["avg_message_count"] == 3.0
        # 2 user messages: 3 + 12 = 15 chars, avg = 7.5
        assert metrics["avg_response_length"] == 7.5
    finally:
        db.close()


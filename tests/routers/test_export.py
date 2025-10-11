"""Tests for data export endpoints."""

import csv
import io
import json

import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def study_with_interviews(test_db, test_user):
    """Create a study with multiple completed interviews."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Export Test Study",
            description="Study for testing exports",
            consent_text="Test consent",
            max_agent_turns=5,
        )
        
        # Create first interview
        invite1 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite1.id, InviteStatus.COMPLETED)
        interview1 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite1.id)
        
        interview_crud.create_interviewee(
            db,
            interview_id=interview1.id,
            name="Alice Smith",
            email="alice@example.com",
            demographics_json={"age_range": "25-34", "location": "USA"},
        )
        
        interview_crud.create_message(
            db, interview_id=interview1.id, role="assistant", content="Hello Alice!"
        )
        interview_crud.create_message(
            db, interview_id=interview1.id, role="user", content="Hi there!"
        )
        
        interview_crud.complete_interview(db, interview1.id)
        interview_crud.create_insight(
            db,
            interview_id=interview1.id,
            summary="Positive feedback about product design",
            sentiment="positive",
            keywords_json=["design", "interface"],
            quotes_json=["Hi there!"],
        )
        
        # Create second interview
        invite2 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite2.id, InviteStatus.COMPLETED)
        interview2 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite2.id)
        
        interview_crud.create_interviewee(
            db,
            interview_id=interview2.id,
            name="Bob Jones",
            email="bob@example.com",
            demographics_json={"age_range": "35-44", "location": "Canada"},
        )
        
        interview_crud.create_message(
            db, interview_id=interview2.id, role="assistant", content="Hello Bob!"
        )
        interview_crud.create_message(
            db, interview_id=interview2.id, role="user", content="Good morning!"
        )
        interview_crud.create_message(
            db, interview_id=interview2.id, role="assistant", content="How are you?"
        )
        interview_crud.create_message(
            db, interview_id=interview2.id, role="user", content="Great, thanks!"
        )
        
        interview_crud.complete_interview(db, interview2.id)
        interview_crud.create_insight(
            db,
            interview_id=interview2.id,
            summary="User satisfied with service",
            sentiment="neutral",
            keywords_json=["service", "satisfaction"],
            quotes_json=["Great, thanks!"],
        )
        
        yield {"user": user, "study": study, "interviews": [interview1, interview2]}
    finally:
        db.close()


@pytest.mark.asyncio
async def test_export_single_interview_json(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting a single interview as JSON."""
    study = study_with_interviews["study"]
    interview = study_with_interviews["interviews"][0]
    
    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/{interview.id}/export?format=json"
    )
    
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert "attachment" in response.headers["content-disposition"]
    assert f"interview_{interview.id}" in response.headers["content-disposition"]
    
    data = json.loads(response.content)
    
    assert data["study"]["title"] == "Export Test Study"
    assert data["interview_count"] == 1
    assert len(data["interviews"]) == 1
    
    interview_data = data["interviews"][0]
    assert interview_data["id"] == interview.id
    assert interview_data["interviewee"]["name"] == "Alice Smith"
    assert interview_data["interviewee"]["email"] == "alice@example.com"
    assert interview_data["insight"]["sentiment"] == "positive"
    assert len(interview_data["messages"]) == 2


@pytest.mark.asyncio
async def test_export_single_interview_csv(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting a single interview as CSV."""
    study = study_with_interviews["study"]
    interview = study_with_interviews["interviews"][0]
    
    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/{interview.id}/export?format=csv"
    )
    
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    assert "attachment" in response.headers["content-disposition"]
    
    # Parse CSV content
    csv_content = response.content.decode("utf-8")
    csv_reader = csv.DictReader(io.StringIO(csv_content))
    rows = list(csv_reader)
    
    assert len(rows) == 1
    row = rows[0]
    
    assert row["study_title"] == "Export Test Study"
    assert row["interview_id"] == str(interview.id)
    assert row["interviewee_name"] == "Alice Smith"
    assert row["interviewee_email"] == "alice@example.com"
    assert row["sentiment"] == "positive"
    assert row["message_count"] == "2"
    assert "[ASSISTANT]:" in row["conversation"]
    assert "[USER]:" in row["conversation"]


@pytest.mark.asyncio
async def test_export_study_all_interviews_json(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting all interviews for a study as JSON."""
    study = study_with_interviews["study"]
    
    response = await authenticated_client.get(
        f"/studies/{study.id}/export?format=json"
    )
    
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    
    data = json.loads(response.content)
    
    assert data["study"]["title"] == "Export Test Study"
    assert data["interview_count"] == 2
    assert len(data["interviews"]) == 2
    
    # Check both interviews are present
    names = {i["interviewee"]["name"] for i in data["interviews"]}
    assert names == {"Alice Smith", "Bob Jones"}


@pytest.mark.asyncio
async def test_export_study_all_interviews_csv(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting all interviews for a study as CSV."""
    study = study_with_interviews["study"]
    
    response = await authenticated_client.get(
        f"/studies/{study.id}/export?format=csv"
    )
    
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    
    # Parse CSV content
    csv_content = response.content.decode("utf-8")
    csv_reader = csv.DictReader(io.StringIO(csv_content))
    rows = list(csv_reader)
    
    assert len(rows) == 2
    
    # Check both interviews are present
    names = {row["interviewee_name"] for row in rows}
    assert names == {"Alice Smith", "Bob Jones"}
    
    # Verify all expected columns are present
    expected_columns = {
        "study_title", "interview_id", "interviewee_name", "interviewee_email",
        "demographics", "started_at", "completed_at", "agent_turns",
        "message_count", "summary", "sentiment", "keywords", "quotes", "conversation"
    }
    assert set(rows[0].keys()) == expected_columns


@pytest.mark.asyncio
async def test_export_invalid_format(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test that invalid export format returns error."""
    study = study_with_interviews["study"]
    interview = study_with_interviews["interviews"][0]
    
    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/{interview.id}/export?format=xml"
    )
    
    assert response.status_code == 422  # Validation error


@pytest.mark.asyncio
async def test_export_interview_not_found(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting non-existent interview returns 404."""
    study = study_with_interviews["study"]
    
    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/99999/export?format=json"
    )
    
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_export_interview_wrong_study(
    authenticated_client: AsyncClient, test_user, test_db, study_with_interviews
):
    """Test that interview from different study cannot be exported."""
    user = study_with_interviews["user"]
    interview = study_with_interviews["interviews"][0]
    
    # Create a different study
    db = test_db()
    try:
        other_study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Other Study",
            description="Different study",
            consent_text="Test",
        )
    
        response = await authenticated_client.get(
            f"/studies/{other_study.id}/interviews/{interview.id}/export?format=json"
        )
        
        assert response.status_code == 404
    finally:
        db.close()


@pytest.mark.asyncio
async def test_export_unauthorized_user(
    client: AsyncClient, study_with_interviews
):
    """Test that unauthorized users cannot export data."""
    study = study_with_interviews["study"]
    interview = study_with_interviews["interviews"][0]
    
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
        f"/studies/{study.id}/interviews/{interview.id}/export?format=json"
    )
    
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_export_empty_study(authenticated_client: AsyncClient, test_user, test_db):
    """Test exporting a study with no interviews."""
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
            f"/studies/{study.id}/export?format=json"
        )
        
        assert response.status_code == 200
        
        data = json.loads(response.content)
        assert data["interview_count"] == 0
        assert len(data["interviews"]) == 0
    finally:
        db.close()


@pytest.mark.asyncio
async def test_export_csv_handles_special_characters(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test that CSV export properly handles special characters and quotes."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Test, Study, With, Commas",
            description="Test",
            consent_text="Test",
        )
        
        invite = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
        interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
        
        interview_crud.create_interviewee(
            db,
            interview_id=interview.id,
            name='John "Johnny" O\'Brien',
            email="john@example.com",
        )
        
        interview_crud.create_message(
            db, interview_id=interview.id, role="user", content='Message with "quotes" and, commas'
        )
        
        interview_crud.complete_interview(db, interview.id)
        
        response = await authenticated_client.get(
            f"/studies/{study.id}/export?format=csv"
        )
        
        assert response.status_code == 200
        
        # Parse CSV and verify it handles special characters correctly
        csv_content = response.content.decode("utf-8")
        csv_reader = csv.DictReader(io.StringIO(csv_content))
        rows = list(csv_reader)
        
        assert len(rows) == 1
        assert rows[0]["interviewee_name"] == 'John "Johnny" O\'Brien'
        assert "quotes" in rows[0]["conversation"]
    finally:
        db.close()


@pytest.mark.asyncio
async def test_export_filename_sanitization(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test that export filenames are properly sanitized."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Study/With\\Special:Characters",
            description="Test",
            consent_text="Test",
        )
        
        response = await authenticated_client.get(
            f"/studies/{study.id}/export?format=json"
        )
        
        assert response.status_code == 200
        
        # Check filename is sanitized (no special characters)
        disposition = response.headers["content-disposition"]
        assert "/" not in disposition
        assert "\\" not in disposition
        assert ":" not in disposition
        assert "Study_With_Special_Characters" in disposition or "study_" in disposition.lower()
    finally:
        db.close()


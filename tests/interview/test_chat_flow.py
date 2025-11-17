"""Tests for chat interview flow."""

from unittest.mock import MagicMock, patch

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
    """Create a database session for tests."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def mock_ai_agent():
    """Mock AI agent to avoid API calls during tests."""
    with patch("app.routers.interview.AIInterviewAgent") as mock:
        agent_instance = MagicMock()
        agent_instance.get_initial_message.return_value = (
            "Hello! Let's begin the interview. What are your thoughts on this topic?"
        )
        agent_instance.get_ai_response.return_value = (
            "That's interesting. Can you tell me more about that?"
        )
        mock.return_value = agent_instance
        yield agent_instance


@pytest.mark.asyncio
async def test_chat_page_loads_with_initial_message(
    client: AsyncClient, db: Session, mock_ai_agent
):
    """Test chat page loads and creates initial AI message."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
        max_agent_turns=5,
    )

    for i, question_text in enumerate(["Question 1?", "Question 2?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    response = await client.get(f"/interview/{invite.invite_code}/chat")

    assert response.status_code == 200
    assert "Test Study" in response.text
    assert "Hello" in response.text or "welcome" in response.text.lower()

    messages = interview_crud.get_messages_by_interview(db, interview.id)
    assert len(messages) == 1
    assert messages[0].role == "assistant"
    assert "Hello" in messages[0].content


@pytest.mark.asyncio
async def test_chat_page_redirects_if_no_consent(client: AsyncClient, db: Session):
    """Test chat page redirects if interview doesn't exist."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)

    response = await client.get(f"/interview/{invite.invite_code}/chat", follow_redirects=False)

    assert response.status_code == 303
    assert f"/interview/{invite.invite_code}/consent" in response.headers["location"]


@pytest.mark.asyncio
async def test_chat_page_redirects_if_no_intake(client: AsyncClient, db: Session):
    """Test chat page redirects if interviewee doesn't exist."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
    _ = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    response = await client.get(f"/interview/{invite.invite_code}/chat", follow_redirects=False)

    assert response.status_code == 303
    assert f"/interview/{invite.invite_code}/intake" in response.headers["location"]


@pytest.mark.asyncio
async def test_send_message_creates_user_and_ai_messages(
    client: AsyncClient, db: Session, mock_ai_agent
):
    """Test sending a message creates both user and AI messages."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
        max_agent_turns=5,
    )

    for i, question_text in enumerate(["Question 1?", "Question 2?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "I think this is very interesting and important."},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "message" in data
    assert data["turns_remaining"] == 4

    messages = interview_crud.get_messages_by_interview(db, interview.id)
    assert len(messages) == 2
    assert messages[0].role == "user"
    assert messages[0].content == "I think this is very interesting and important."
    assert messages[1].role == "assistant"

    db.refresh(interview)
    assert interview.agent_turns == 1


@pytest.mark.asyncio
async def test_send_message_increments_turn_counter(
    client: AsyncClient, db: Session, mock_ai_agent
):
    """Test that turn counter is incremented after each message."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
        max_agent_turns=3,
    )

    for i, question_text in enumerate(["Question 1?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    assert interview.agent_turns == 0

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "First response"},
    )

    db.refresh(interview)
    assert interview.agent_turns == 1

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "Second response"},
    )

    db.refresh(interview)
    assert interview.agent_turns == 2


@pytest.mark.asyncio
async def test_interview_completes_at_turn_limit(client: AsyncClient, db: Session, mock_ai_agent):
    """Test that interview completes when turn limit is reached."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
        max_agent_turns=2,
    )

    for i, question_text in enumerate(["Question 1?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "First response"},
    )

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "Second response"},
    )

    data = response.json()
    assert data["status"] == "completed"
    assert "redirect" in data
    assert "/complete" in data["redirect"]

    db.refresh(interview)
    assert interview.completed_at is not None
    assert interview.agent_turns == 2


@pytest.mark.asyncio
async def test_send_empty_message_returns_error(client: AsyncClient, db: Session, mock_ai_agent):
    """Test that empty messages are rejected."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "   "},
    )

    data = response.json()
    assert "error" in data
    assert data["error"] == "Message cannot be empty"


@pytest.mark.asyncio
async def test_send_message_to_completed_interview_returns_error(client: AsyncClient, db: Session):
    """Test that messages cannot be sent to completed interviews."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    interview_crud.complete_interview(db, interview.id)

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "This should fail"},
    )

    data = response.json()
    assert "error" in data
    assert data["error"] == "Interview already completed"


@pytest.mark.asyncio
async def test_long_message_is_truncated(client: AsyncClient, db: Session, mock_ai_agent):
    """Test that messages longer than 2000 chars are truncated."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    for i, question_text in enumerate(["Question 1?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    long_message = "A" * 2500

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": long_message},
    )

    assert response.status_code == 200

    messages = interview_crud.get_messages_by_interview(db, interview.id)
    user_message = [m for m in messages if m.role == "user"][0]
    assert len(user_message.content) == 2000


@pytest.mark.asyncio
async def test_chat_page_redirects_to_complete_if_already_done(client: AsyncClient, db: Session):
    """Test that completed interviews redirect to thank you page."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    interview_crud.complete_interview(db, interview.id)

    response = await client.get(f"/interview/{invite.invite_code}/chat", follow_redirects=False)

    assert response.status_code == 303
    assert f"/interview/{invite.invite_code}/complete" in response.headers["location"]


@pytest.mark.asyncio
async def test_complete_page_displays_thank_you(client: AsyncClient, db: Session):
    """Test that completion page displays correctly."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="John Doe",
        email="john@example.com",
    )

    interview_crud.complete_interview(db, interview.id)

    response = await client.get(f"/interview/{invite.invite_code}/complete")

    assert response.status_code == 200
    assert "Thank You" in response.text or "thank" in response.text.lower()
    assert "John Doe" in response.text
    assert "Test Study" in response.text


@pytest.mark.asyncio
async def test_ai_agent_receives_conversation_history(
    client: AsyncClient, db: Session, mock_ai_agent
):
    """Test that AI agent receives full conversation history."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    for i, question_text in enumerate(["Question 1?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    _ = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "First message"},
    )

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "Second message"},
    )

    assert mock_ai_agent.get_ai_response.called
    call_args = mock_ai_agent.get_ai_response.call_args
    conversation_history = call_args.kwargs["conversation_history"]

    assert len(conversation_history) >= 2
    assert any(msg["content"] == "First message" for msg in conversation_history)

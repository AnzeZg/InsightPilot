"""Unit tests for interview CRUD operations."""

from datetime import datetime

import pytest

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
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


@pytest.fixture
def test_invite(db_session, test_study):
    """Create a test invite."""
    return invite_crud.create_invite(db_session, test_study.id)


@pytest.fixture
def test_interview(db_session, test_study, test_invite):
    """Create a test interview."""
    return interview_crud.create_interview(db_session, test_study.id, test_invite.id)


# Interview CRUD Tests


def test_create_interview(db_session, test_study, test_invite):
    """Test creating an interview."""
    interview = interview_crud.create_interview(db_session, test_study.id, test_invite.id)

    assert interview.id is not None
    assert interview.study_id == test_study.id
    assert interview.invite_id == test_invite.id
    assert interview.agent_turns == 0
    assert interview.started_at is not None
    assert interview.completed_at is None


def test_get_interview_by_id(db_session, test_interview):
    """Test getting an interview by ID."""
    retrieved = interview_crud.get_interview_by_id(db_session, test_interview.id)

    assert retrieved is not None
    assert retrieved.id == test_interview.id
    assert retrieved.study_id == test_interview.study_id


def test_get_interview_by_id_not_found(db_session):
    """Test getting non-existent interview returns None."""
    result = interview_crud.get_interview_by_id(db_session, 99999)
    assert result is None


def test_get_interview_by_id_with_messages(db_session, test_interview):
    """Test getting an interview with messages loaded."""
    # Create messages
    interview_crud.create_message(db_session, test_interview.id, "user", "Hello")
    interview_crud.create_message(db_session, test_interview.id, "assistant", "Hi")

    interview = interview_crud.get_interview_by_id(
        db_session, test_interview.id, load_messages=True
    )

    assert interview is not None
    assert len(interview.messages) == 2


def test_get_interview_by_id_load_all(db_session, test_interview):
    """Test getting an interview with all related data."""
    # Create related data
    interview_crud.create_message(db_session, test_interview.id, "user", "Hello")
    interview_crud.create_interviewee(db_session, test_interview.id, "John Doe", "john@example.com")
    interview_crud.create_insight(
        db_session, test_interview.id, "Summary", "positive", ["key1"], ["quote1"]
    )

    interview = interview_crud.get_interview_by_id(db_session, test_interview.id, load_all=True)

    assert interview is not None
    assert len(interview.messages) == 1
    assert interview.interviewee is not None
    assert interview.insight is not None


def test_get_interviews_by_study(db_session, test_study):
    """Test getting all interviews for a study."""
    invite1 = invite_crud.create_invite(db_session, test_study.id)
    invite2 = invite_crud.create_invite(db_session, test_study.id)

    interview1 = interview_crud.create_interview(db_session, test_study.id, invite1.id)
    interview2 = interview_crud.create_interview(db_session, test_study.id, invite2.id)

    interviews = interview_crud.get_interviews_by_study(db_session, test_study.id)

    assert len(interviews) == 2
    interview_ids = [i.id for i in interviews]
    assert interview1.id in interview_ids
    assert interview2.id in interview_ids

    # Should be ordered by started_at desc (newest first)
    assert interviews[0].id == interview2.id
    assert interviews[1].id == interview1.id


def test_get_interviews_by_study_with_relations(db_session, test_study, test_invite):
    """Test getting interviews with related data loaded."""
    interview = interview_crud.create_interview(db_session, test_study.id, test_invite.id)
    interview_crud.create_interviewee(db_session, interview.id, "Jane", "jane@example.com")

    interviews = interview_crud.get_interviews_by_study(
        db_session, test_study.id, load_relations=True
    )

    assert len(interviews) == 1
    assert interviews[0].interviewee is not None


def test_get_interviews_by_study_empty(db_session, test_study):
    """Test getting interviews when none exist."""
    interviews = interview_crud.get_interviews_by_study(db_session, test_study.id)
    assert interviews == []


def test_interviews_isolated_by_study(db_session, test_user):
    """Test that interviews are isolated by study."""
    study1 = study_crud.create_study(db_session, test_user.id, "Study 1", "D", "C")
    study2 = study_crud.create_study(db_session, test_user.id, "Study 2", "D", "C")

    invite1 = invite_crud.create_invite(db_session, study1.id)
    invite2 = invite_crud.create_invite(db_session, study2.id)

    interview1 = interview_crud.create_interview(db_session, study1.id, invite1.id)
    interview2 = interview_crud.create_interview(db_session, study2.id, invite2.id)

    study1_interviews = interview_crud.get_interviews_by_study(db_session, study1.id)
    assert len(study1_interviews) == 1
    assert study1_interviews[0].id == interview1.id

    study2_interviews = interview_crud.get_interviews_by_study(db_session, study2.id)
    assert len(study2_interviews) == 1
    assert study2_interviews[0].id == interview2.id


def test_get_interview_by_invite(db_session, test_study, test_invite):
    """Test getting an interview by invite ID."""
    created = interview_crud.create_interview(db_session, test_study.id, test_invite.id)

    retrieved = interview_crud.get_interview_by_invite(db_session, test_invite.id)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.invite_id == test_invite.id


def test_get_interview_by_invite_not_found(db_session):
    """Test getting interview by non-existent invite returns None."""
    result = interview_crud.get_interview_by_invite(db_session, 99999)
    assert result is None


def test_complete_interview(db_session, test_interview):
    """Test marking an interview as completed."""
    completed = interview_crud.complete_interview(db_session, test_interview.id)

    assert completed is not None
    assert completed.id == test_interview.id
    assert completed.completed_at is not None
    assert isinstance(completed.completed_at, datetime)


def test_complete_interview_not_found(db_session):
    """Test completing non-existent interview returns None."""
    result = interview_crud.complete_interview(db_session, 99999)
    assert result is None


def test_increment_agent_turns(db_session, test_interview):
    """Test incrementing agent turn counter."""
    assert test_interview.agent_turns == 0

    updated = interview_crud.increment_agent_turns(db_session, test_interview.id)
    assert updated.agent_turns == 1

    updated = interview_crud.increment_agent_turns(db_session, test_interview.id)
    assert updated.agent_turns == 2


def test_increment_agent_turns_not_found(db_session):
    """Test incrementing turns for non-existent interview returns None."""
    result = interview_crud.increment_agent_turns(db_session, 99999)
    assert result is None


# Interviewee CRUD Tests


def test_create_interviewee(db_session, test_interview):
    """Test creating an interviewee record."""
    interviewee = interview_crud.create_interviewee(
        db_session,
        test_interview.id,
        "John Doe",
        "john@example.com",
        {"age": 30, "country": "USA"},
    )

    assert interviewee.id is not None
    assert interviewee.interview_id == test_interview.id
    assert interviewee.name == "John Doe"
    assert interviewee.email == "john@example.com"
    assert interviewee.demographics_json == {"age": 30, "country": "USA"}
    assert interviewee.consent_at is not None


def test_create_interviewee_no_demographics(db_session, test_interview):
    """Test creating an interviewee without demographics."""
    interviewee = interview_crud.create_interviewee(
        db_session, test_interview.id, "Jane Doe", "jane@example.com"
    )

    assert interviewee.demographics_json is None


def test_get_interviewee_by_interview(db_session, test_interview):
    """Test getting an interviewee by interview ID."""
    created = interview_crud.create_interviewee(
        db_session, test_interview.id, "John", "john@example.com"
    )

    retrieved = interview_crud.get_interviewee_by_interview(db_session, test_interview.id)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.name == "John"


def test_get_interviewee_by_interview_not_found(db_session, test_interview):
    """Test getting non-existent interviewee returns None."""
    result = interview_crud.get_interviewee_by_interview(db_session, test_interview.id)
    assert result is None


# Message CRUD Tests


def test_create_message(db_session, test_interview):
    """Test creating a message."""
    message = interview_crud.create_message(
        db_session, test_interview.id, "user", "Hello, how are you?"
    )

    assert message.id is not None
    assert message.interview_id == test_interview.id
    assert message.role == "user"
    assert message.content == "Hello, how are you?"
    assert message.created_at is not None


def test_create_message_assistant(db_session, test_interview):
    """Test creating an assistant message."""
    message = interview_crud.create_message(
        db_session, test_interview.id, "assistant", "I'm doing well, thank you!"
    )

    assert message.role == "assistant"
    assert message.content == "I'm doing well, thank you!"


def test_get_message_count(db_session, test_interview):
    """Test getting message count."""
    assert interview_crud.get_message_count(db_session, test_interview.id) == 0

    interview_crud.create_message(db_session, test_interview.id, "user", "Message 1")
    assert interview_crud.get_message_count(db_session, test_interview.id) == 1

    interview_crud.create_message(db_session, test_interview.id, "assistant", "Message 2")
    assert interview_crud.get_message_count(db_session, test_interview.id) == 2


def test_get_messages_by_interview(db_session, test_interview):
    """Test getting all messages for an interview."""
    msg1 = interview_crud.create_message(db_session, test_interview.id, "user", "First")
    msg2 = interview_crud.create_message(db_session, test_interview.id, "assistant", "Second")
    msg3 = interview_crud.create_message(db_session, test_interview.id, "user", "Third")

    messages = interview_crud.get_messages_by_interview(db_session, test_interview.id)

    assert len(messages) == 3
    # Should be ordered by created_at (chronological)
    assert messages[0].id == msg1.id
    assert messages[1].id == msg2.id
    assert messages[2].id == msg3.id


def test_get_messages_by_interview_with_limit(db_session, test_interview):
    """Test getting messages with limit."""
    for i in range(5):
        interview_crud.create_message(db_session, test_interview.id, "user", f"Message {i}")

    messages = interview_crud.get_messages_by_interview(db_session, test_interview.id, limit=3)

    assert len(messages) == 3


def test_get_messages_by_interview_empty(db_session, test_interview):
    """Test getting messages when none exist."""
    messages = interview_crud.get_messages_by_interview(db_session, test_interview.id)
    assert messages == []


def test_get_recent_messages(db_session, test_interview):
    """Test getting recent messages."""
    # Create 10 messages
    for i in range(10):
        interview_crud.create_message(db_session, test_interview.id, "user", f"Message {i}")

    # Get 5 most recent
    recent = interview_crud.get_recent_messages(db_session, test_interview.id, count=5)

    assert len(recent) == 5
    # Should be in chronological order (oldest to newest of the recent ones)
    assert "Message 5" in recent[0].content
    assert "Message 9" in recent[4].content


def test_get_recent_messages_default_count(db_session, test_interview):
    """Test getting recent messages with default count."""
    for i in range(10):
        interview_crud.create_message(db_session, test_interview.id, "user", f"Message {i}")

    recent = interview_crud.get_recent_messages(db_session, test_interview.id)

    assert len(recent) == 8  # Default count


def test_get_recent_messages_fewer_than_requested(db_session, test_interview):
    """Test getting recent messages when fewer exist than requested."""
    interview_crud.create_message(db_session, test_interview.id, "user", "Message 1")
    interview_crud.create_message(db_session, test_interview.id, "user", "Message 2")

    recent = interview_crud.get_recent_messages(db_session, test_interview.id, count=5)

    assert len(recent) == 2


# Insight CRUD Tests


def test_create_insight(db_session, test_interview):
    """Test creating an insight."""
    insight = interview_crud.create_insight(
        db_session,
        test_interview.id,
        "User is satisfied with the product",
        "positive",
        ["satisfaction", "product", "quality"],
        ["I love this product", "It works great"],
    )

    assert insight.id is not None
    assert insight.interview_id == test_interview.id
    assert insight.summary == "User is satisfied with the product"
    assert insight.sentiment == "positive"
    assert insight.keywords_json == ["satisfaction", "product", "quality"]
    assert insight.quotes_json == ["I love this product", "It works great"]
    assert insight.created_at is not None


def test_get_insight_by_interview(db_session, test_interview):
    """Test getting an insight by interview ID."""
    created = interview_crud.create_insight(
        db_session, test_interview.id, "Summary", "neutral", [], []
    )

    retrieved = interview_crud.get_insight_by_interview(db_session, test_interview.id)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.summary == "Summary"


def test_get_insight_by_interview_not_found(db_session, test_interview):
    """Test getting non-existent insight returns None."""
    result = interview_crud.get_insight_by_interview(db_session, test_interview.id)
    assert result is None


def test_update_insight_summary(db_session, test_interview):
    """Test updating insight summary."""
    insight = interview_crud.create_insight(
        db_session, test_interview.id, "Old summary", "positive", [], []
    )

    updated = interview_crud.update_insight(db_session, insight.id, summary="New summary")

    assert updated is not None
    assert updated.id == insight.id
    assert updated.summary == "New summary"
    assert updated.sentiment == "positive"  # Unchanged


def test_update_insight_multiple_fields(db_session, test_interview):
    """Test updating multiple insight fields."""
    insight = interview_crud.create_insight(
        db_session, test_interview.id, "Summary", "positive", ["key1"], ["quote1"]
    )

    updated = interview_crud.update_insight(
        db_session,
        insight.id,
        summary="Updated summary",
        sentiment="negative",
        keywords_json=["key2", "key3"],
        quotes_json=["quote2"],
    )

    assert updated.summary == "Updated summary"
    assert updated.sentiment == "negative"
    assert updated.keywords_json == ["key2", "key3"]
    assert updated.quotes_json == ["quote2"]


def test_update_insight_not_found(db_session):
    """Test updating non-existent insight returns None."""
    result = interview_crud.update_insight(db_session, 99999, summary="New")
    assert result is None


def test_update_insight_no_changes(db_session, test_interview):
    """Test updating insight with no changes."""
    insight = interview_crud.create_insight(
        db_session, test_interview.id, "Summary", "positive", [], []
    )

    updated = interview_crud.update_insight(db_session, insight.id)

    assert updated is not None
    assert updated.id == insight.id
    assert updated.summary == "Summary"


def test_complete_interview_workflow(db_session, test_study, test_invite):
    """Test a complete interview workflow."""
    # Create interview
    interview = interview_crud.create_interview(db_session, test_study.id, test_invite.id)
    assert interview.agent_turns == 0

    # Add interviewee
    interviewee = interview_crud.create_interviewee(
        db_session, interview.id, "Alice", "alice@example.com"
    )
    assert interviewee.interview_id == interview.id

    # Add messages
    interview_crud.create_message(db_session, interview.id, "user", "Hello")
    interview_crud.increment_agent_turns(db_session, interview.id)
    interview_crud.create_message(db_session, interview.id, "assistant", "Hi there")
    interview_crud.increment_agent_turns(db_session, interview.id)

    # Get message count
    count = interview_crud.get_message_count(db_session, interview.id)
    assert count == 2

    # Complete interview
    completed = interview_crud.complete_interview(db_session, interview.id)
    assert completed.completed_at is not None
    assert completed.agent_turns == 2

    # Generate insights
    insight = interview_crud.create_insight(
        db_session, interview.id, "Great feedback", "positive", ["happy"], ["love it"]
    )
    assert insight.interview_id == interview.id

    # Retrieve full interview
    full = interview_crud.get_interview_by_id(db_session, interview.id, load_all=True)
    assert full.interviewee.name == "Alice"
    assert len(full.messages) == 2
    assert full.insight.summary == "Great feedback"

"""Tests for the insight generator service."""

from unittest.mock import MagicMock, patch

import pytest
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus
from app.services.insight_generator import InsightGenerator


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client."""
    with patch("app.services.openai_factory.create_openai_client") as mock_factory:
        mock_client = MagicMock()
        mock_factory.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices[
            0
        ].message.content = """{
            "summary": "The participant discussed their experience with the product interface.",
            "sentiment": "positive",
            "keywords": ["user interface", "design", "experience"],
            "themes": ["product usability", "customer satisfaction"],
            "notable_quotes": [
                "I really love the new design.",
                "The interface is very intuitive.",
                "Best product I've used in years."
            ],
            "engagement_level": "high",
            "key_insights": [
                "User highly values intuitive design",
                "Positive sentiment toward new features"
            ]
        }"""

        mock_client.chat.completions.create.return_value = mock_response

        yield mock_client


@pytest.fixture
def db(test_db):
    """Get database session from test_db fixture."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def sample_interview(db: Session):
    """Create a sample interview with messages."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Product Research",
        description="Understanding user experience",
        consent_text="Test consent",
        max_agent_turns=5,
    )

    study_crud.create_study_question(db, study_id=study.id, text="What do you think?", sort_order=0)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    _ = interview_crud.create_interviewee(
        db, interview_id=interview.id, name="Test User", email="test@example.com"
    )

    interview_crud.create_message(
        db, interview_id=interview.id, role="assistant", content="Hello! What brings you here?"
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="user",
        content="I really love the new design. The interface is very intuitive and easy to use.",
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
        content="The navigation is smooth and the features are exactly what I needed. Best product I've used in years.",
    )

    return interview


@pytest.mark.asyncio
async def test_generate_insights_success(db: Session, sample_interview, mock_openai_client):
    """Test successful insight generation."""
    generator = InsightGenerator()

    insights = generator.generate_insights(db, sample_interview.id)

    assert insights["summary"] is not None
    assert insights["sentiment"] in ["positive", "neutral", "negative"]
    assert isinstance(insights["keywords"], list)
    assert isinstance(insights["themes"], list)
    assert isinstance(insights["notable_quotes"], list)
    assert insights["engagement_level"] in ["high", "medium", "low"]
    assert isinstance(insights["key_insights"], list)

    mock_openai_client.chat.completions.create.assert_called_once()
    call_args = mock_openai_client.chat.completions.create.call_args
    assert call_args.kwargs["model"] == "gpt-4o-mini"
    assert call_args.kwargs["temperature"] == 0.3
    assert call_args.kwargs["response_format"] == {"type": "json_object"}


@pytest.mark.asyncio
async def test_generate_insights_validates_output(db: Session, sample_interview):
    """Test that insights are validated and normalized."""
    with patch("app.services.insight_generator.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices[
            0
        ].message.content = """{
            "summary": "Test summary",
            "sentiment": "INVALID_SENTIMENT",
            "keywords": ["test"],
            "themes": [],
            "notable_quotes": [],
            "engagement_level": "INVALID_LEVEL",
            "key_insights": []
        }"""

        mock_client.chat.completions.create.return_value = mock_response

        generator = InsightGenerator()
        insights = generator.generate_insights(db, sample_interview.id)

        assert insights["sentiment"] == "neutral"
        assert insights["engagement_level"] == "medium"


@pytest.mark.asyncio
async def test_generate_insights_empty_interview(db: Session):
    """Test insight generation with no messages."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test",
        consent_text="Test",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    generator = InsightGenerator()
    insights = generator.generate_insights(db, interview.id)

    assert insights["summary"] == "No conversation recorded"
    assert insights["sentiment"] == "neutral"
    assert insights["keywords"] == []
    assert insights["notable_quotes"] == []
    assert insights["engagement_level"] == "low"


@pytest.mark.asyncio
async def test_generate_insights_api_failure_fallback(db: Session, sample_interview):
    """Test fallback extraction when API fails."""
    with patch("app.services.insight_generator.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_client.chat.completions.create.side_effect = Exception("API Error")

        generator = InsightGenerator()
        insights = generator.generate_insights(db, sample_interview.id)

        assert insights["summary"] is not None
        assert insights["sentiment"] == "neutral"
        assert len(insights["notable_quotes"]) > 0


@pytest.mark.asyncio
async def test_generate_insights_invalid_json_fallback(db: Session, sample_interview):
    """Test fallback when LLM returns invalid JSON."""
    with patch("app.services.insight_generator.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices[0].message.content = "This is not valid JSON"

        mock_client.chat.completions.create.return_value = mock_response

        generator = InsightGenerator()
        insights = generator.generate_insights(db, sample_interview.id)

        assert insights["sentiment"] == "neutral"
        assert isinstance(insights["notable_quotes"], list)


@pytest.mark.asyncio
async def test_format_conversation(db: Session, sample_interview):
    """Test conversation formatting."""
    generator = InsightGenerator()

    messages = interview_crud.get_messages_by_interview(db, sample_interview.id)
    conversation = generator._format_conversation(messages)

    assert "AI Interviewer:" in conversation
    assert "Participant:" in conversation
    assert "Hello! What brings you here?" in conversation
    assert "I really love the new design" in conversation


@pytest.mark.asyncio
async def test_validate_insights_limits_output_size():
    """Test that validation limits output sizes."""
    generator = InsightGenerator()

    large_insights = {
        "summary": "x" * 2000,
        "sentiment": "positive",
        "keywords": [f"keyword{i}" for i in range(100)],
        "themes": [f"theme{i}" for i in range(50)],
        "notable_quotes": [f"quote{i}" for i in range(20)],
        "engagement_level": "high",
        "key_insights": [f"insight{i}" for i in range(50)],
    }

    validated = generator._validate_insights(large_insights)

    assert len(validated["summary"]) <= 1000
    assert len(validated["keywords"]) <= 20
    assert len(validated["themes"]) <= 10
    assert len(validated["notable_quotes"]) <= 5
    assert len(validated["key_insights"]) <= 10


@pytest.mark.asyncio
async def test_fallback_extraction_with_meaningful_responses(db: Session, sample_interview):
    """Test fallback extraction selects meaningful responses."""
    generator = InsightGenerator()

    messages = interview_crud.get_messages_by_interview(db, sample_interview.id)
    insights = generator._fallback_extraction(messages)

    assert len(insights["notable_quotes"]) > 0
    for quote in insights["notable_quotes"]:
        assert len(quote) > 50


@pytest.mark.asyncio
async def test_fallback_extraction_no_user_messages(db: Session):
    """Test fallback extraction with only agent messages."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test",
        consent_text="Test",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    interview_crud.create_message(db, interview_id=interview.id, role="assistant", content="Hello!")

    generator = InsightGenerator()
    messages = interview_crud.get_messages_by_interview(db, interview.id)
    insights = generator._fallback_extraction(messages)

    assert "No" in insights["summary"] and "recorded" in insights["summary"]
    assert insights["notable_quotes"] == []

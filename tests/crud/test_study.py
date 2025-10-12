"""Unit tests for study CRUD operations."""

import pytest

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


# Study CRUD Tests


def test_create_study(db_session, test_user):
    """Test creating a study."""
    study = study_crud.create_study(
        db_session,
        owner_user_id=test_user.id,
        title="Product Research",
        description="Understanding user needs",
        consent_text="I consent to participate",
        max_agent_turns=15,
    )
    
    assert study.id is not None
    assert study.owner_user_id == test_user.id
    assert study.title == "Product Research"
    assert study.description == "Understanding user needs"
    assert study.consent_text == "I consent to participate"
    assert study.max_agent_turns == 15
    assert study.created_at is not None


def test_create_study_default_max_turns(db_session, test_user):
    """Test that default max_agent_turns is set."""
    study = study_crud.create_study(
        db_session,
        owner_user_id=test_user.id,
        title="Test",
        description="Test",
        consent_text="Test",
    )
    
    assert study.max_agent_turns == 9  # Default value


def test_get_study_by_id(db_session, test_study):
    """Test getting a study by ID."""
    retrieved = study_crud.get_study_by_id(db_session, test_study.id)
    
    assert retrieved is not None
    assert retrieved.id == test_study.id
    assert retrieved.title == test_study.title


def test_get_study_by_id_not_found(db_session):
    """Test getting non-existent study returns None."""
    result = study_crud.get_study_by_id(db_session, 99999)
    assert result is None


def test_get_study_by_id_with_questions(db_session, test_study):
    """Test getting a study with questions loaded."""
    # Add questions
    study_crud.create_study_question(db_session, test_study.id, "Question 1", 0)
    study_crud.create_study_question(db_session, test_study.id, "Question 2", 1)
    
    # Get study with questions
    study = study_crud.get_study_by_id(db_session, test_study.id, load_questions=True)
    
    assert study is not None
    assert len(study.questions) == 2


def test_get_study_by_id_without_questions(db_session, test_study):
    """Test getting a study without loading questions."""
    study_crud.create_study_question(db_session, test_study.id, "Question 1", 0)
    
    study = study_crud.get_study_by_id(db_session, test_study.id, load_questions=False)
    
    assert study is not None
    # Questions should not be loaded (lazy loaded)


def test_get_studies_by_user(db_session, test_user):
    """Test getting all studies for a user."""
    study1 = study_crud.create_study(
        db_session, test_user.id, "Study 1", "Desc 1", "Consent 1"
    )
    study2 = study_crud.create_study(
        db_session, test_user.id, "Study 2", "Desc 2", "Consent 2"
    )
    
    studies = study_crud.get_studies_by_user(db_session, test_user.id)
    
    assert len(studies) == 2
    study_ids = [s.id for s in studies]
    assert study1.id in study_ids
    assert study2.id in study_ids
    
    # Should be ordered by created_at desc (newest first)
    assert studies[0].id == study2.id
    assert studies[1].id == study1.id


def test_get_studies_by_user_pagination(db_session, test_user):
    """Test pagination when getting studies."""
    for i in range(5):
        study_crud.create_study(
            db_session, test_user.id, f"Study {i}", f"Desc {i}", "Consent"
        )
    
    # Test skip
    studies_skip = study_crud.get_studies_by_user(db_session, test_user.id, skip=2)
    assert len(studies_skip) == 3
    
    # Test limit
    studies_limit = study_crud.get_studies_by_user(db_session, test_user.id, limit=2)
    assert len(studies_limit) == 2


def test_get_studies_by_user_empty(db_session, test_user):
    """Test getting studies when none exist."""
    studies = study_crud.get_studies_by_user(db_session, test_user.id)
    assert studies == []


def test_get_studies_isolation(db_session):
    """Test that studies are isolated by user."""
    user1 = user_crud.create_user(db_session, "user1@example.com", "hash1")
    user2 = user_crud.create_user(db_session, "user2@example.com", "hash2")
    
    study1 = study_crud.create_study(db_session, user1.id, "Study 1", "Desc", "Consent")
    study2 = study_crud.create_study(db_session, user2.id, "Study 2", "Desc", "Consent")
    
    user1_studies = study_crud.get_studies_by_user(db_session, user1.id)
    assert len(user1_studies) == 1
    assert user1_studies[0].id == study1.id
    
    user2_studies = study_crud.get_studies_by_user(db_session, user2.id)
    assert len(user2_studies) == 1
    assert user2_studies[0].id == study2.id


def test_update_study_title(db_session, test_study):
    """Test updating study title."""
    updated = study_crud.update_study(db_session, test_study.id, title="New Title")
    
    assert updated is not None
    assert updated.id == test_study.id
    assert updated.title == "New Title"
    assert updated.description == test_study.description  # Unchanged


def test_update_study_multiple_fields(db_session, test_study):
    """Test updating multiple study fields."""
    updated = study_crud.update_study(
        db_session,
        test_study.id,
        title="New Title",
        description="New Description",
        max_agent_turns=20,
    )
    
    assert updated.title == "New Title"
    assert updated.description == "New Description"
    assert updated.max_agent_turns == 20
    assert updated.consent_text == test_study.consent_text  # Unchanged


def test_update_study_not_found(db_session):
    """Test updating non-existent study returns None."""
    result = study_crud.update_study(db_session, 99999, title="New Title")
    assert result is None


def test_update_study_no_changes(db_session, test_study):
    """Test updating study with no changes."""
    updated = study_crud.update_study(db_session, test_study.id)
    
    assert updated is not None
    assert updated.id == test_study.id
    assert updated.title == test_study.title


def test_delete_study(db_session, test_study):
    """Test deleting a study."""
    result = study_crud.delete_study(db_session, test_study.id)
    assert result is True
    
    # Verify it's gone
    retrieved = study_crud.get_study_by_id(db_session, test_study.id)
    assert retrieved is None


def test_delete_study_not_found(db_session):
    """Test deleting non-existent study returns False."""
    result = study_crud.delete_study(db_session, 99999)
    assert result is False


# StudyQuestion CRUD Tests


def test_create_study_question(db_session, test_study):
    """Test creating a study question."""
    question = study_crud.create_study_question(
        db_session, test_study.id, "What is your opinion?", 0
    )
    
    assert question.id is not None
    assert question.study_id == test_study.id
    assert question.text == "What is your opinion?"
    assert question.sort_order == 0


def test_get_study_questions(db_session, test_study):
    """Test getting all questions for a study."""
    q1 = study_crud.create_study_question(db_session, test_study.id, "Question 1", 1)
    q2 = study_crud.create_study_question(db_session, test_study.id, "Question 2", 0)
    q3 = study_crud.create_study_question(db_session, test_study.id, "Question 3", 2)
    
    questions = study_crud.get_study_questions(db_session, test_study.id)
    
    assert len(questions) == 3
    # Should be ordered by sort_order
    assert questions[0].id == q2.id  # sort_order 0
    assert questions[1].id == q1.id  # sort_order 1
    assert questions[2].id == q3.id  # sort_order 2


def test_get_study_questions_empty(db_session, test_study):
    """Test getting questions when none exist."""
    questions = study_crud.get_study_questions(db_session, test_study.id)
    assert questions == []


def test_update_question_text(db_session, test_study):
    """Test updating question text."""
    question = study_crud.create_study_question(
        db_session, test_study.id, "Original text", 0
    )
    
    updated = study_crud.update_question_text(db_session, question.id, "Updated text")
    
    assert updated is not None
    assert updated.id == question.id
    assert updated.text == "Updated text"
    assert updated.sort_order == 0  # Unchanged


def test_update_question_text_not_found(db_session):
    """Test updating non-existent question returns None."""
    result = study_crud.update_question_text(db_session, 99999, "New text")
    assert result is None


def test_reorder_questions(db_session, test_study):
    """Test reordering questions."""
    q1 = study_crud.create_study_question(db_session, test_study.id, "Q1", 0)
    q2 = study_crud.create_study_question(db_session, test_study.id, "Q2", 1)
    q3 = study_crud.create_study_question(db_session, test_study.id, "Q3", 2)
    
    # Reorder: swap q1 and q3
    updates = [(q1.id, 2), (q3.id, 0)]
    result = study_crud.reorder_questions(db_session, updates)
    
    assert result is True
    
    # Verify new order
    questions = study_crud.get_study_questions(db_session, test_study.id)
    assert questions[0].id == q3.id  # Now at position 0
    assert questions[1].id == q2.id  # Still at position 1
    assert questions[2].id == q1.id  # Now at position 2


def test_reorder_questions_empty_list(db_session):
    """Test reordering with empty list."""
    result = study_crud.reorder_questions(db_session, [])
    assert result is True


def test_delete_study_question(db_session, test_study):
    """Test deleting a study question."""
    question = study_crud.create_study_question(db_session, test_study.id, "Question", 0)
    
    result = study_crud.delete_study_question(db_session, question.id)
    assert result is True
    
    # Verify it's gone
    questions = study_crud.get_study_questions(db_session, test_study.id)
    assert len(questions) == 0


def test_delete_study_question_not_found(db_session):
    """Test deleting non-existent question returns False."""
    result = study_crud.delete_study_question(db_session, 99999)
    assert result is False


def test_questions_isolated_by_study(db_session, test_user):
    """Test that questions are isolated by study."""
    study1 = study_crud.create_study(db_session, test_user.id, "Study 1", "D", "C")
    study2 = study_crud.create_study(db_session, test_user.id, "Study 2", "D", "C")
    
    study_crud.create_study_question(db_session, study1.id, "Q1 for Study 1", 0)
    study_crud.create_study_question(db_session, study2.id, "Q1 for Study 2", 0)
    
    study1_questions = study_crud.get_study_questions(db_session, study1.id)
    assert len(study1_questions) == 1
    assert "Study 1" in study1_questions[0].text
    
    study2_questions = study_crud.get_study_questions(db_session, study2.id)
    assert len(study2_questions) == 1
    assert "Study 2" in study2_questions[0].text


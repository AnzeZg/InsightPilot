"""CRUD operations for Study and StudyQuestion models."""

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.study import Study, StudyQuestion


# Study CRUD


def create_study(
    db: Session,
    owner_user_id: int,
    title: str,
    description: str,
    consent_text: str,
    max_agent_turns: int = 9,
) -> Study:
    """Create a new study."""
    study = Study(
        owner_user_id=owner_user_id,
        title=title,
        description=description,
        consent_text=consent_text,
        max_agent_turns=max_agent_turns,
    )
    db.add(study)
    db.commit()
    db.refresh(study)
    return study


def get_study_by_id(db: Session, study_id: int, load_questions: bool = True) -> Study | None:
    """Get study by ID with optional question loading."""
    stmt = select(Study).where(Study.id == study_id)
    if load_questions:
        stmt = stmt.options(selectinload(Study.questions))
    return db.scalar(stmt)


def get_studies_by_user(
    db: Session, user_id: int, skip: int = 0, limit: int = 100
) -> list[Study]:
    """Get all studies for a user."""
    stmt = (
        select(Study)
        .where(Study.owner_user_id == user_id)
        .order_by(Study.created_at.desc())
        .offset(skip)
        .limit(limit)
    )
    return list(db.scalars(stmt).all())


def update_study(
    db: Session,
    study_id: int,
    title: str | None = None,
    description: str | None = None,
    consent_text: str | None = None,
    max_agent_turns: int | None = None,
) -> Study | None:
    """Update study details."""
    study = db.get(Study, study_id)
    if study:
        if title is not None:
            study.title = title
        if description is not None:
            study.description = description
        if consent_text is not None:
            study.consent_text = consent_text
        if max_agent_turns is not None:
            study.max_agent_turns = max_agent_turns
        db.commit()
        db.refresh(study)
    return study


def delete_study(db: Session, study_id: int) -> bool:
    """Delete a study and cascade to related entities."""
    study = db.get(Study, study_id)
    if study:
        db.delete(study)
        db.commit()
        return True
    return False


# StudyQuestion CRUD


def create_study_question(db: Session, study_id: int, text: str, sort_order: int) -> StudyQuestion:
    """Create a study question."""
    question = StudyQuestion(study_id=study_id, text=text, sort_order=sort_order)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


def get_study_questions(db: Session, study_id: int) -> list[StudyQuestion]:
    """Get all questions for a study, ordered."""
    stmt = (
        select(StudyQuestion)
        .where(StudyQuestion.study_id == study_id)
        .order_by(StudyQuestion.sort_order)
    )
    return list(db.scalars(stmt).all())


def update_question_text(db: Session, question_id: int, text: str) -> StudyQuestion | None:
    """Update question text."""
    question = db.get(StudyQuestion, question_id)
    if question:
        question.text = text
        db.commit()
        db.refresh(question)
    return question


def reorder_questions(db: Session, question_updates: list[tuple[int, int]]) -> bool:
    """Bulk update question sort orders. Input: [(question_id, new_sort_order), ...]"""
    for question_id, new_order in question_updates:
        question = db.get(StudyQuestion, question_id)
        if question:
            question.sort_order = new_order
    db.commit()
    return True


def delete_study_question(db: Session, question_id: int) -> bool:
    """Delete a study question."""
    question = db.get(StudyQuestion, question_id)
    if question:
        db.delete(question)
        db.commit()
        return True
    return False


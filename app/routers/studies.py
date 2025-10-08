"""Studies routes for researchers."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.db.session import get_db
from app.models.user import User
from app.schemas.invite import InviteCreate, InviteResponse
from app.schemas.study import (
    QuestionBatchReorder,
    QuestionCreate,
    QuestionResponse,
    StudyCreate,
    StudyResponse,
    StudyUpdate,
)

router = APIRouter(prefix="/studies", tags=["studies"])


def verify_study_owner(study_id: int, user: User, db: Session):
    """Verify that the current user owns the study."""
    study = study_crud.get_study_by_id(db, study_id, load_questions=False)
    if not study:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Study not found",
        )
    if study.owner_user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Study not found",
        )
    return study


@router.post("/", response_model=StudyResponse, status_code=status.HTTP_201_CREATED)
def create_study(
    study_data: StudyCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new study."""
    study = study_crud.create_study(
        db,
        owner_user_id=current_user.id,
        title=study_data.title,
        description=study_data.description,
        consent_text=study_data.consent_text,
        max_agent_turns=study_data.max_agent_turns,
    )
    return study


@router.get("/", response_model=list[StudyResponse])
def list_studies(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List all studies for the current user."""
    studies = study_crud.get_studies_by_user(db, current_user.id, skip=skip, limit=limit)
    return studies


@router.get("/{study_id}", response_model=StudyResponse)
def get_study(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get a specific study with questions."""
    study = verify_study_owner(study_id, current_user, db)
    # Load with questions
    study_with_questions = study_crud.get_study_by_id(db, study_id, load_questions=True)
    return study_with_questions


@router.patch("/{study_id}", response_model=StudyResponse)
def update_study(
    study_id: int,
    study_data: StudyUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update a study."""
    verify_study_owner(study_id, current_user, db)
    
    updated_study = study_crud.update_study(
        db,
        study_id,
        title=study_data.title,
        description=study_data.description,
        consent_text=study_data.consent_text,
        max_agent_turns=study_data.max_agent_turns,
    )
    return updated_study


@router.delete("/{study_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_study(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a study."""
    verify_study_owner(study_id, current_user, db)
    study_crud.delete_study(db, study_id)
    return None


# Questions endpoints


@router.post("/{study_id}/questions", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
def create_question(
    study_id: int,
    question_data: QuestionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Add a question to a study."""
    verify_study_owner(study_id, current_user, db)
    
    question = study_crud.create_study_question(
        db,
        study_id=study_id,
        text=question_data.text,
        sort_order=question_data.sort_order,
    )
    return question


@router.get("/{study_id}/questions", response_model=list[QuestionResponse])
def list_questions(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all questions for a study."""
    verify_study_owner(study_id, current_user, db)
    questions = study_crud.get_study_questions(db, study_id)
    return questions


@router.post("/{study_id}/questions/reorder", status_code=status.HTTP_204_NO_CONTENT)
def reorder_questions(
    study_id: int,
    reorder_data: QuestionBatchReorder,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Reorder questions in a study."""
    verify_study_owner(study_id, current_user, db)
    
    # Verify all questions belong to this study
    existing_questions = study_crud.get_study_questions(db, study_id)
    existing_ids = {q.id for q in existing_questions}
    
    for update in reorder_data.updates:
        if update.question_id not in existing_ids:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Question {update.question_id} not found in study",
            )
    
    # Apply reordering
    updates = [(u.question_id, u.sort_order) for u in reorder_data.updates]
    study_crud.reorder_questions(db, updates)
    return None


@router.delete("/{study_id}/questions/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(
    study_id: int,
    question_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a question from a study."""
    verify_study_owner(study_id, current_user, db)
    
    # Verify question belongs to study
    question = db.get(study_crud.StudyQuestion, question_id)
    if not question or question.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found",
        )
    
    study_crud.delete_study_question(db, question_id)
    return None


# Invites endpoints


@router.post("/{study_id}/invites", response_model=InviteResponse, status_code=status.HTTP_201_CREATED)
def create_invite(
    study_id: int,
    invite_data: InviteCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create an invite for a study."""
    verify_study_owner(study_id, current_user, db)
    
    invite = invite_crud.create_invite(
        db,
        study_id=study_id,
        interviewee_email=invite_data.interviewee_email,
        expires_at=invite_data.expires_at,
    )
    return invite


@router.get("/{study_id}/invites", response_model=list[InviteResponse])
def list_invites(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all invites for a study."""
    verify_study_owner(study_id, current_user, db)
    invites = invite_crud.get_invites_by_study(db, study_id)
    return invites


@router.delete("/{study_id}/invites/{invite_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invite(
    study_id: int,
    invite_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete an invite."""
    verify_study_owner(study_id, current_user, db)
    
    # Verify invite belongs to study
    invite = invite_crud.get_invite_by_id(db, invite_id)
    if not invite or invite.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invite not found",
        )
    
    invite_crud.delete_invite(db, invite_id)
    return None



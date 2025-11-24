"""Studies routes for researchers."""

import csv
import io
import json
from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.db.session import get_db
from app.models.user import User
from app.schemas.interview import (
    InterviewDetailResponse,
    InterviewListItem,
    StudyAnalytics,
)
from app.schemas.invite import InviteCreate, InviteResponse
from app.schemas.study import (
    QuestionBatchReorder,
    QuestionCreate,
    QuestionResponse,
    StudyCreate,
    StudyResponse,
    StudyUpdate,
)
from app.services.analytics_service import StudyAnalyticsService
from app.utils.formatters import format_datetime, format_json_field

router = APIRouter(prefix="/studies", tags=["studies"])


def verify_study_owner(study_id: int, user: User, db: Session):
    """Verify that the current user owns the study (wrapper for backward compatibility)."""
    return study_crud.verify_study_ownership(db, study_id, user.id)


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
    verify_study_owner(study_id, current_user, db)
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


@router.post(
    "/{study_id}/questions", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED
)
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

    existing_questions = study_crud.get_study_questions(db, study_id)
    existing_ids = {q.id for q in existing_questions}

    for update in reorder_data.updates:
        if update.question_id not in existing_ids:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Question {update.question_id} not found in study",
            )

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

    question = db.get(study_crud.StudyQuestion, question_id)
    if not question or question.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found",
        )

    study_crud.delete_study_question(db, question_id)
    return None


@router.post(
    "/{study_id}/invites", response_model=InviteResponse, status_code=status.HTTP_201_CREATED
)
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

    invite = invite_crud.get_invite_by_id(db, invite_id)
    if not invite or invite.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invite not found",
        )

    invite_crud.delete_invite(db, invite_id)
    return None


@router.get("/{study_id}/interviews", response_model=list[InterviewListItem])
def list_interviews(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Get all interviews for a study with summary information.

    Returns interviews with:
    - Interviewee details
    - Completion status
    - Insights summary
    - Message count
    """
    verify_study_owner(study_id, current_user, db)

    interviews = interview_crud.get_interviews_by_study(db, study_id, load_relations=True)

    result = []
    for interview in interviews:
        message_count = interview_crud.get_message_count(db, interview.id)

        interview_data = InterviewListItem(
            id=interview.id,
            study_id=interview.study_id,
            started_at=interview.started_at,
            completed_at=interview.completed_at,
            agent_turns=interview.agent_turns,
            interviewee=interview.interviewee,
            insight=interview.insight,
            message_count=message_count,
        )
        result.append(interview_data)

    return result


@router.get("/{study_id}/interviews/{interview_id}", response_model=InterviewDetailResponse)
def get_interview_transcript(
    study_id: int,
    interview_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Get detailed interview transcript with full conversation.

    Returns:
    - All messages in chronological order
    - Interviewee information
    - Generated insights
    - Interview metadata
    """
    verify_study_owner(study_id, current_user, db)

    interview = interview_crud.get_interview_by_id(db, interview_id, load_all=True)

    if not interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    if interview.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    return InterviewDetailResponse(
        id=interview.id,
        study_id=interview.study_id,
        started_at=interview.started_at,
        completed_at=interview.completed_at,
        agent_turns=interview.agent_turns,
        interviewee=interview.interviewee,
        messages=interview.messages,
        insight=interview.insight,
    )


def _export_interview_to_dict(interview, study_title: str) -> dict:
    """Convert interview to dictionary for export."""
    interviewee = interview.interviewee
    insight = interview.insight

    conversation = []
    for msg in interview.messages:
        conversation.append(f"[{msg.role.upper()}]: {msg.content}")
    conversation_text = "\n\n".join(conversation)

    return {
        "study_title": study_title,
        "interview_id": interview.id,
        "interviewee_name": interviewee.name if interviewee else "",
        "interviewee_email": interviewee.email if interviewee else "",
        "demographics": format_json_field(interviewee.demographics_json if interviewee else None),
        "started_at": format_datetime(interview.started_at),
        "completed_at": format_datetime(interview.completed_at),
        "agent_turns": interview.agent_turns,
        "message_count": len(interview.messages),
        "summary": insight.summary if insight else "",
        "sentiment": insight.sentiment if insight else "",
        "keywords": format_json_field(insight.keywords_json if insight else None),
        "quotes": format_json_field(insight.quotes_json if insight else None),
        "conversation": conversation_text,
    }


def _generate_csv_export(interviews, study_title: str) -> str:
    """Generate CSV export from interviews."""
    output = io.StringIO()

    if not interviews:
        return ""

    fieldnames = [
        "study_title",
        "interview_id",
        "interviewee_name",
        "interviewee_email",
        "demographics",
        "started_at",
        "completed_at",
        "agent_turns",
        "message_count",
        "summary",
        "sentiment",
        "keywords",
        "quotes",
        "conversation",
    ]

    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for interview in interviews:
        row = _export_interview_to_dict(interview, study_title)
        writer.writerow(row)

    return output.getvalue()


def _generate_json_export(interviews, study_title: str, study_description: str) -> dict:
    """Generate JSON export from interviews."""
    interviews_data = []

    for interview in interviews:
        interviewee = interview.interviewee
        insight = interview.insight

        interview_data = {
            "id": interview.id,
            "started_at": interview.started_at.isoformat() if interview.started_at else None,
            "completed_at": interview.completed_at.isoformat() if interview.completed_at else None,
            "agent_turns": interview.agent_turns,
            "interviewee": {
                "name": interviewee.name if interviewee else None,
                "email": interviewee.email if interviewee else None,
                "demographics": interviewee.demographics_json if interviewee else None,
            },
            "messages": [
                {
                    "role": msg.role,
                    "content": msg.content,
                    "created_at": msg.created_at.isoformat() if msg.created_at else None,
                }
                for msg in interview.messages
            ],
            "insight": (
                {
                    "summary": insight.summary if insight else None,
                    "sentiment": insight.sentiment if insight else None,
                    "keywords": insight.keywords_json if insight else None,
                    "quotes": insight.quotes_json if insight else None,
                }
                if insight
                else None
            ),
        }
        interviews_data.append(interview_data)

    return {
        "study": {
            "title": study_title,
            "description": study_description,
        },
        "export_date": datetime.now(UTC).isoformat(),
        "interview_count": len(interviews),
        "interviews": interviews_data,
    }


@router.get("/{study_id}/interviews/{interview_id}/export")
def export_interview(
    study_id: int,
    interview_id: int,
    format: str = Query("json", pattern="^(json|csv)$"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Export a single interview in JSON or CSV format.

    - **format**: Export format (json or csv)
    """
    study = verify_study_owner(study_id, current_user, db)

    interview = interview_crud.get_interview_by_id(db, interview_id, load_all=True)

    if not interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    if interview.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    filename = f"interview_{interview_id}_{timestamp}.{format}"

    if format == "csv":
        csv_data = _generate_csv_export([interview], study.title)
        return StreamingResponse(
            iter([csv_data]),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )
    else:
        json_data = _generate_json_export([interview], study.title, study.description)
        return StreamingResponse(
            iter([json.dumps(json_data, indent=2)]),
            media_type="application/json",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )


@router.get("/{study_id}/export")
def export_study_interviews(
    study_id: int,
    format: str = Query("json", pattern="^(json|csv)$"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Export all interviews for a study in JSON or CSV format.

    - **format**: Export format (json or csv)
    """
    study = verify_study_owner(study_id, current_user, db)

    interviews = interview_crud.get_interviews_by_study(db, study_id, load_relations=True)

    for interview in interviews:
        interview.messages = interview_crud.get_messages_by_interview(db, interview.id)

    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    safe_title = "".join(c if c.isalnum() else "_" for c in study.title)[:50]
    filename = f"study_{safe_title}_{timestamp}.{format}"

    if format == "csv":
        csv_data = _generate_csv_export(interviews, study.title)
        return StreamingResponse(
            iter([csv_data]),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )
    else:
        json_data = _generate_json_export(interviews, study.title, study.description)
        return StreamingResponse(
            iter([json.dumps(json_data, indent=2)]),
            media_type="application/json",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )


@router.get("/{study_id}/analytics", response_model=StudyAnalytics)
def get_study_analytics(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Get aggregated analytics for a study.

    Returns comprehensive analytics including sentiment, keywords,
    metrics, demographics, timeline, and sample quotes.
    """
    study = verify_study_owner(study_id, current_user, db)

    analytics_service = StudyAnalyticsService(db)
    return analytics_service.generate_analytics(study_id, study)

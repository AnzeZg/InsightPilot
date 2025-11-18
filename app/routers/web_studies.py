"""Web routes for studies (HTML rendering)."""

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.db.session import get_db
from app.models.user import User

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/app", tags=["web"])


def verify_study_owner(study_id: int, user: User, db: Session):
    """Verify that the current user owns the study (wrapper for backward compatibility)."""
    return study_crud.verify_study_ownership(db, study_id, user.id)


@router.get("/studies", response_class=HTMLResponse)
def list_studies_page(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the studies list page."""
    studies = study_crud.get_studies_by_user(db, current_user.id)
    return templates.TemplateResponse("studies/list.html", {"request": request, "studies": studies})


@router.post("/studies/", response_class=RedirectResponse)
def create_study_form(
    title: str = Form(...),
    description: str = Form(...),
    consent_text: str = Form(...),
    max_agent_turns: int = Form(9),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new study from form data."""
    study = study_crud.create_study(
        db,
        owner_user_id=current_user.id,
        title=title,
        description=description,
        consent_text=consent_text,
        max_agent_turns=max_agent_turns,
    )
    return RedirectResponse(url=f"/app/studies/{study.id}", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/studies/{study_id}", response_class=HTMLResponse)
def get_study_page(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the study detail page."""
    study = verify_study_owner(study_id, current_user, db)
    questions = study_crud.get_study_questions(db, study_id)
    invites = invite_crud.get_invites_by_study(db, study_id)

    return templates.TemplateResponse(
        "studies/detail.html",
        {
            "request": request,
            "study": study,
            "questions": questions,
            "invites": invites,
            "study_id": study_id,
        },
    )


@router.post("/studies/{study_id}", response_class=RedirectResponse)
def update_study_form(
    study_id: int,
    method: str = Form(None),
    title: str = Form(None),
    description: str = Form(None),
    consent_text: str = Form(None),
    max_agent_turns: int = Form(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update or delete a study from form data."""
    verify_study_owner(study_id, current_user, db)

    if method == "DELETE":
        study_crud.delete_study(db, study_id)
        return RedirectResponse(url="/app/studies", status_code=status.HTTP_303_SEE_OTHER)

    elif method == "PATCH":
        study_crud.update_study(
            db,
            study_id,
            title=title,
            description=description,
            consent_text=consent_text,
            max_agent_turns=max_agent_turns,
        )
        return RedirectResponse(
            url=f"/app/studies/{study_id}", status_code=status.HTTP_303_SEE_OTHER
        )

    return RedirectResponse(url=f"/app/studies/{study_id}", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/studies/{study_id}/questions", response_class=HTMLResponse)
def add_question_htmx(
    request: Request,
    study_id: int,
    text: str = Form(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Add a question and return the updated questions partial."""
    verify_study_owner(study_id, current_user, db)

    # Calculate next sort_order (max existing + 1, or 0 if no questions)
    existing_questions = study_crud.get_study_questions(db, study_id)
    next_sort_order = max([q.sort_order for q in existing_questions], default=-1) + 1

    study_crud.create_study_question(db, study_id, text, next_sort_order)
    questions = study_crud.get_study_questions(db, study_id)

    return templates.TemplateResponse(
        "studies/_questions.html",
        {"request": request, "questions": questions, "study_id": study_id},
    )


@router.delete("/studies/{study_id}/questions/{question_id}", response_class=HTMLResponse)
def delete_question_htmx(
    request: Request,
    study_id: int,
    question_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a question and return the updated questions partial."""
    verify_study_owner(study_id, current_user, db)
    study_crud.delete_study_question(db, question_id)
    questions = study_crud.get_study_questions(db, study_id)

    return templates.TemplateResponse(
        "studies/_questions.html",
        {"request": request, "questions": questions, "study_id": study_id},
    )


@router.post("/studies/{study_id}/questions/reorder", response_class=HTMLResponse)
async def reorder_questions_htmx(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Reorder questions and return the updated questions partial."""
    verify_study_owner(study_id, current_user, db)

    # Parse JSON body
    body = await request.json()
    questions_data = body.get("questions", [])

    # Convert to list of tuples for reorder_questions
    question_updates = [(q["question_id"], q["sort_order"]) for q in questions_data]
    study_crud.reorder_questions(db, question_updates)

    questions = study_crud.get_study_questions(db, study_id)

    return templates.TemplateResponse(
        "studies/_questions.html",
        {"request": request, "questions": questions, "study_id": study_id},
    )


@router.post("/studies/{study_id}/invites", response_class=HTMLResponse)
def create_invite_htmx(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create an invite and return the updated invites partial."""
    verify_study_owner(study_id, current_user, db)
    invite_crud.create_invite(db, study_id)
    invites = invite_crud.get_invites_by_study(db, study_id)

    return templates.TemplateResponse(
        "studies/_invites.html",
        {"request": request, "invites": invites},
    )


@router.delete("/studies/{study_id}/invites/{invite_id}", response_class=HTMLResponse)
def delete_invite_htmx(
    request: Request,
    study_id: int,
    invite_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete an invite and return the updated invites partial."""
    verify_study_owner(study_id, current_user, db)
    invite_crud.delete_invite(db, invite_id)
    invites = invite_crud.get_invites_by_study(db, study_id)

    return templates.TemplateResponse(
        "studies/_invites.html",
        {"request": request, "invites": invites},
    )


@router.get("/studies/{study_id}/interviews", response_class=HTMLResponse)
def list_interviews_page(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the interviews list page for a study."""
    study = verify_study_owner(study_id, current_user, db)

    interviews = interview_crud.get_interviews_by_study(db, study_id, load_relations=True)

    interview_list = []
    for interview in interviews:
        message_count = interview_crud.get_message_count(db, interview.id)
        interview_list.append(
            {
                "id": interview.id,
                "study_id": interview.study_id,
                "started_at": interview.started_at,
                "completed_at": interview.completed_at,
                "agent_turns": interview.agent_turns,
                "interviewee": interview.interviewee,
                "insight": interview.insight,
                "message_count": message_count,
            }
        )

    return templates.TemplateResponse(
        "studies/interviews.html",
        {
            "request": request,
            "study": study,
            "interviews": interview_list,
        },
    )


@router.get("/studies/{study_id}/interviews/{interview_id}", response_class=HTMLResponse)
def view_transcript_page(
    request: Request,
    study_id: int,
    interview_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the interview transcript page."""
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

    return templates.TemplateResponse(
        "studies/transcript.html",
        {
            "request": request,
            "study": study,
            "interview": interview,
            "interviewee": interview.interviewee,
            "messages": interview.messages,
            "insight": interview.insight,
        },
    )


@router.get("/studies/{study_id}/analytics", response_class=HTMLResponse)
def analytics_page(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the analytics page for a study."""
    study = verify_study_owner(study_id, current_user, db)

    return templates.TemplateResponse(
        "studies/analytics.html",
        {
            "request": request,
            "study": study,
        },
    )

"""Public-facing interview routes (no authentication required)."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr, ValidationError
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.db.session import get_db
from app.models.invite import InviteStatus
from app.schemas.interview import IntakeForm

router = APIRouter(prefix="/interview", tags=["interview"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/{invite_code}", response_class=HTMLResponse)
async def landing_page(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Landing page for interview invite.
    
    - Validates invite exists and is not expired/completed
    - Shows study information
    - Updates invite status to 'opened' on first view
    - Provides CTA to continue to consent
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)
    
    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )
    
    if invite.status == InviteStatus.COMPLETED.value:
        return templates.TemplateResponse(
            request=request,
            name="interview/completed.html",
        )
    
    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return templates.TemplateResponse(
            request=request,
            name="interview/expired.html",
        )
    
    if invite.status == InviteStatus.CREATED.value:
        invite_crud.update_invite_status(db, invite.id, InviteStatus.OPENED)
        db.refresh(invite)
    
    study = invite.study
    
    return templates.TemplateResponse(
        request=request,
        name="interview/landing.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
        },
    )


@router.get("/{invite_code}/consent", response_class=HTMLResponse)
async def consent_page(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Consent page for interview.
    
    - Shows study consent text
    - Provides checkbox to agree
    - Validates invite is still valid
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)
    
    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )
    
    if invite.status == InviteStatus.COMPLETED.value:
        return templates.TemplateResponse(
            request=request,
            name="interview/completed.html",
        )

    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return templates.TemplateResponse(
            request=request,
            name="interview/expired.html",
        )

    study = invite.study
    
    return templates.TemplateResponse(
        request=request,
        name="interview/consent.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
        },
    )


@router.post("/{invite_code}/consent")
async def submit_consent(
    invite_code: str,
    agreed: bool = Form(...),
    db: Session = Depends(get_db),
):
    """
    Process consent form submission.
    
    - Validates invite is still valid
    - Creates interview record
    - Updates invite status to 'completed'
    - Redirects to intake form
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)
    
    if not invite:
        return RedirectResponse(
            url=f"/interview/{invite_code}",
            status_code=303,
        )
    
    if invite.status == InviteStatus.COMPLETED.value:
        return RedirectResponse(
            url=f"/interview/{invite_code}",
            status_code=303,
        )
        
    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return RedirectResponse(
            url=f"/interview/{invite_code}",
            status_code=303,
        )
    
    if not agreed:
        return RedirectResponse(
            url=f"/interview/{invite_code}/consent",
            status_code=303,
        )
    
    existing_interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not existing_interview:
        interview_crud.create_interview(
            db,
            study_id=invite.study_id,
            invite_id=invite.id,
        )
        invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
    
    return RedirectResponse(
        url=f"/interview/{invite_code}/intake",
        status_code=303,
    )


@router.get("/{invite_code}/intake", response_class=HTMLResponse)
async def intake_page(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Intake form page.
    
    - Collects interviewee information (name, email, demographics)
    - Validates that consent has been given (interview exists)
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)
    
    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )
    
    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return templates.TemplateResponse(
            request=request,
            name="interview/expired.html",
        )
    
    interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not interview:
        return RedirectResponse(
            url=f"/interview/{invite_code}/consent",
            status_code=303,
        )
    
    existing_interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)
    if existing_interviewee:
        return templates.TemplateResponse(
            request=request,
            name="interview/completed.html",
        )
    
    study = invite.study
    
    return templates.TemplateResponse(
        request=request,
        name="interview/intake.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
        },
    )


@router.post("/{invite_code}/intake")
async def submit_intake(
    request: Request,
    invite_code: str,
    name: str = Form(...),
    email: EmailStr = Form(...),
    age_range: str = Form(None),
    location: str = Form(None),
    occupation: str = Form(None),
    db: Session = Depends(get_db),
):
    """
    Process intake form submission.
    
    - Validates form data
    - Creates interviewee record
    - Redirects to chat interface (Day 4)
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)
    
    if not invite:
        return RedirectResponse(
            url=f"/interview/{invite_code}",
            status_code=303,
        )
    
    interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not interview:
        return RedirectResponse(
            url=f"/interview/{invite_code}/consent",
            status_code=303,
        )
    
    existing_interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)
    if existing_interviewee:
        return RedirectResponse(
            url=f"/interview/{invite_code}/chat",
            status_code=303,
        )
    
    demographics = {}
    if age_range:
        demographics["age_range"] = age_range
    if location:
        demographics["location"] = location
    if occupation:
        demographics["occupation"] = occupation
    
    try:
        interview_crud.create_interviewee(
            db,
            interview_id=interview.id,
            name=name.strip(),
            email=email.lower().strip(),
            demographics_json=demographics if demographics else None,
        )
    except Exception as e:
        study = invite.study
        return templates.TemplateResponse(
            request=request,
            name="interview/intake.html",
            context={
                "invite_code": invite_code,
                "invite": invite,
                "study": study,
                "error": "An error occurred while saving your information. Please try again.",
                "form_data": {"name": name, "email": email},
            },
        )
    
    return RedirectResponse(
        url=f"/interview/{invite_code}/chat",
        status_code=303,
    )


@router.get("/{invite_code}/chat", response_class=HTMLResponse)
async def chat_page(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Chat interface placeholder (Day 4).
    
    Shows a placeholder page until the actual chat is implemented.
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)
    
    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )
    
    interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not interview:
        return RedirectResponse(
            url=f"/interview/{invite_code}/consent",
            status_code=303,
        )
    
    interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)
    if not interviewee:
        return RedirectResponse(
            url=f"/interview/{invite_code}/intake",
            status_code=303,
        )
    
    study = invite.study
    
    return templates.TemplateResponse(
        request=request,
        name="interview/chat_placeholder.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
            "interviewee": interviewee,
        },
    )


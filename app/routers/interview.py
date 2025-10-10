"""Public-facing interview routes (no authentication required)."""

import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr, ValidationError
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.db.session import get_db
from app.models.invite import InviteStatus
from app.schemas.interview import IntakeForm
from app.services.ai_agent import AIInterviewAgent
from app.services.insight_generator import InsightGenerator

logger = logging.getLogger(__name__)

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
    Chat interface for conducting the AI interview.
    
    - Loads existing messages
    - Verifies interviewee completed intake
    - Checks if interview is completed
    - Initiates conversation if no messages exist
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
    
    if interview.completed_at:
        return RedirectResponse(
            url=f"/interview/{invite_code}/complete",
            status_code=303,
        )
    
    messages = interview_crud.get_messages_by_interview(db, interview.id)
    
    if not messages:
        try:
            agent = AIInterviewAgent()
            initial_message = agent.get_initial_message(
                study_title=study.title,
                study_description=study.description,
                study_questions=[q.text for q in study.questions],
                interviewee_name=interviewee.name,
            )
            
            interview_crud.create_message(
                db,
                interview_id=interview.id,
                role="assistant",
                content=initial_message,
            )
            
            messages = interview_crud.get_messages_by_interview(db, interview.id)
            
        except ValueError as e:
            return templates.TemplateResponse(
                request=request,
                name="interview/chat_placeholder.html",
                context={
                    "invite_code": invite_code,
                    "study": study,
                    "interviewee": interviewee,
                    "error": str(e),
                },
            )
        except Exception as e:
            return templates.TemplateResponse(
                request=request,
                name="interview/chat_placeholder.html",
                context={
                    "invite_code": invite_code,
                    "study": study,
                    "interviewee": interviewee,
                    "error": f"Failed to initialize AI agent: {str(e)}",
                },
            )
    
    turns_remaining = study.max_agent_turns - interview.agent_turns
    
    return templates.TemplateResponse(
        request=request,
        name="interview/chat.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
            "interviewee": interviewee,
            "interview": interview,
            "messages": messages,
            "turns_remaining": turns_remaining,
            "max_turns": study.max_agent_turns,
        },
    )


@router.post("/{invite_code}/chat/message")
async def send_message(
    request: Request,
    invite_code: str,
    message: str = Form(...),
    db: Session = Depends(get_db),
):
    """
    Handle user message submission and generate AI response.
    
    - Saves user message
    - Triggers AI agent response
    - Saves AI response
    - Increments turn counter
    - Checks completion conditions
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)
    
    if not invite:
        return JSONResponse(
            status_code=404,
            content={"error": "Invite not found"}
        )
    
    interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not interview:
        return JSONResponse(
            status_code=404,
            content={"error": "Interview not found"}
        )
    
    if interview.completed_at:
        return JSONResponse(
            status_code=400,
            content={"error": "Interview already completed"}
        )
    
    interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)
    study = invite.study
    
    if not message.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Message cannot be empty"}
        )
    
    if len(message) > 2000:
        message = message[:2000]
    
    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="user",
        content=message.strip(),
    )
    
    if interview.agent_turns >= study.max_agent_turns:
        interview_crud.complete_interview(db, interview.id)
        
        return {
            "status": "completed",
            "message": "Interview completed. Thank you for your participation!",
            "redirect": f"/interview/{invite_code}/complete"
        }
    
    conversation_history = interview_crud.get_messages_by_interview(db, interview.id)
    history_for_ai = [
        {"role": msg.role, "content": msg.content}
        for msg in conversation_history
    ]
    
    try:
        agent = AIInterviewAgent()
        ai_response = agent.get_ai_response(
            study_title=study.title,
            study_description=study.description,
            study_questions=[q.text for q in study.questions],
            conversation_history=history_for_ai,
            current_turn=interview.agent_turns,
            max_turns=study.max_agent_turns,
        )
        
        interview_crud.create_message(
            db,
            interview_id=interview.id,
            role="assistant",
            content=ai_response,
        )
        
        interview_crud.increment_agent_turns(db, interview.id)
        
        db.refresh(interview)
        
        is_completed = interview.agent_turns >= study.max_agent_turns
        if is_completed:
            interview_crud.complete_interview(db, interview.id)
            
            try:
                generator = InsightGenerator()
                insights = generator.generate_insights(db, interview.id)
                
                combined_keywords = insights.get("keywords", []) + insights.get("themes", [])
                
                interview_crud.create_insight(
                    db,
                    interview_id=interview.id,
                    summary=insights.get("summary", "Interview completed"),
                    sentiment=insights.get("sentiment", "neutral"),
                    keywords_json=combined_keywords,
                    quotes_json=insights.get("notable_quotes", []),
                )
                logger.info(f"Generated insights for interview {interview.id}")
            except Exception as e:
                logger.error(f"Failed to generate insights for interview {interview.id}: {e}")
        
        return {
            "status": "completed" if is_completed else "success",
            "message": ai_response,
            "turns_remaining": study.max_agent_turns - interview.agent_turns,
            "redirect": f"/interview/{invite_code}/complete" if is_completed else None
        }
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": f"Failed to generate response: {str(e)}"
            }
        )


@router.get("/{invite_code}/complete", response_class=HTMLResponse)
async def interview_complete(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Thank you page after interview completion.
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
    
    study = invite.study
    interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)
    
    return templates.TemplateResponse(
        request=request,
        name="interview/thank_you.html",
        context={
            "invite_code": invite_code,
            "study": study,
            "interviewee": interviewee,
            "interview": interview,
        },
    )


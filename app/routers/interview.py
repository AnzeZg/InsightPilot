"""Public-facing interview routes (no authentication required)."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.crud import invite as invite_crud
from app.db.session import get_db
from app.models.invite import InviteStatus

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
    # Get invite by code
    invite = invite_crud.get_invite_by_code(db, invite_code)
    
    # Handle not found
    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )
    
    # Check if already completed
    if invite.status == InviteStatus.COMPLETED.value:
        return templates.TemplateResponse(
            request=request,
            name="interview/completed.html",
        )
    
    # Check if expired
    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return templates.TemplateResponse(
            request=request,
            name="interview/expired.html",
        )
    
    # Update status to 'opened' if still in 'created' state
    if invite.status == InviteStatus.CREATED.value:
        invite_crud.update_invite_status(db, invite.id, InviteStatus.OPENED)
        # Refresh to get updated status
        db.refresh(invite)
    
    # Load study information
    study = invite.study
    
    # Render landing page
    return templates.TemplateResponse(
        request=request,
        name="interview/landing.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
        },
    )


"""Web routes for authentication (HTML rendering)."""

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(tags=["web-auth"])


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    """Render the login page."""
    success = request.query_params.get("success")
    return templates.TemplateResponse(
        "auth/login.html",
        {
            "request": request,
            "success": success,
        },
    )


@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    """Render the registration page."""
    return templates.TemplateResponse(
        "auth/register.html",
        {"request": request},
    )


@router.get("/account", response_class=HTMLResponse)
def account_page(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the user account page."""
    return templates.TemplateResponse(
        "auth/account.html",
        {
            "request": request,
            "user": current_user,
        },
    )

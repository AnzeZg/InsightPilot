"""Development-only authentication routes for testing."""

from urllib.parse import quote_plus

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from passlib.hash import argon2
from sqlalchemy.orm import Session

from app.auth.sessions import clear_session, set_session
from app.crud import session as session_crud
from app.crud import user as user_crud
from app.db.session import get_db
from app.settings import settings

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(prefix="/auth/dev", tags=["auth-dev"])


@router.post("/register")
def dev_register(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(None),
    db: Session = Depends(get_db),
):
    """
    DEV ONLY: Create a test user.
    
    Only available in development mode.
    """
    if settings.is_production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found",
        )
    
    # Check if this is a browser request (for HTML response)
    accept = request.headers.get("accept", "")
    wants_html = "text/html" in accept
    
    # Validate password confirmation (if provided from form)
    if confirm_password and password != confirm_password:
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/register.html",
                context={
                    "error": "Passwords do not match",
                    "email": email,
                },
                status_code=400,
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match",
        )
    
    # Validate password length
    if len(password) < 8:
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/register.html",
                context={
                    "error": "Password must be at least 8 characters long",
                    "email": email,
                },
                status_code=400,
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 8 characters long",
        )
    
    # Check if user exists
    existing_user = user_crud.get_user_by_email(db, email)
    if existing_user:
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/register.html",
                context={
                    "error": "Email already registered. Please login instead.",
                    "email": email,
                },
                status_code=400,
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    
    # Create user
    password_hash = argon2.hash(password)
    user = user_crud.create_user(db, email=email, password_hash=password_hash)
    
    # For HTML requests, redirect to login
    if wants_html:
        return RedirectResponse(
            url=f"/login?success={quote_plus('Account created successfully! Please login.')}",
            status_code=status.HTTP_303_SEE_OTHER,
        )
    
    # For API requests, return JSON with 201 status
    from fastapi.responses import JSONResponse
    return JSONResponse(
        content={
            "id": user.id,
            "email": user.email,
            "created_at": user.created_at.isoformat(),
        },
        status_code=status.HTTP_201_CREATED,
    )


@router.post("/login")
def dev_login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    """
    DEV ONLY: Login and get session cookie.
    
    Only available in development mode.
    """
    if settings.is_production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found",
        )
    
    # Check if this is a browser request (for HTML response)
    accept = request.headers.get("accept", "")
    wants_html = "text/html" in accept
    
    # Get user
    user = user_crud.get_user_by_email(db, email)
    if not user:
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/login.html",
                context={
                    "error": "Invalid email or password",
                    "email": email,
                },
                status_code=401,
            )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    # Verify password
    if not argon2.verify(password, user.password_hash):
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/login.html",
                context={
                    "error": "Invalid email or password",
                    "email": email,
                },
                status_code=401,
            )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    session = session_crud.create_session(db, user.id)
    
    # For HTML requests, set cookie and redirect
    if wants_html:
        next_url = request.query_params.get("next", "/app/studies")
        response = RedirectResponse(url=next_url, status_code=status.HTTP_303_SEE_OTHER)
        set_session(response, session.id)
        return response
    
    # For API requests, set cookie and redirect to studies
    response = RedirectResponse(url="/app/studies", status_code=status.HTTP_303_SEE_OTHER)
    set_session(response, session.id)
    return response


@router.post("/logout")
def dev_logout():
    """DEV ONLY: Logout (clear session cookie)."""
    if settings.is_production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found",
        )
    
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    clear_session(response)
    return response


@router.get("/quick-auth")
def dev_quick_auth(db: Session = Depends(get_db)):
    """
    DEV ONLY: Create test user and return session cookie in one step.
    
    Creates user test@example.com / password123 and logs them in.
    Useful for quick testing.
    """
    if settings.is_production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found",
        )
    
    email = "test@example.com"
    password = "password123"
    
    # Check if user exists, create if not
    user = user_crud.get_user_by_email(db, email)
    if not user:
        password_hash = argon2.hash(password)
        user = user_crud.create_user(db, email=email, password_hash=password_hash)
    
    # Create session
    session = session_crud.create_session(db, user.id)
    
    # Set cookie and redirect to studies
    response = RedirectResponse(url="/app/studies", status_code=status.HTTP_303_SEE_OTHER)
    set_session(response, session.id)
    
    return response


"""Development-only authentication routes for testing."""

from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.responses import RedirectResponse
from passlib.hash import argon2
from sqlalchemy.orm import Session

from app.auth.sessions import clear_session, set_session
from app.crud import session as session_crud
from app.crud import user as user_crud
from app.db.session import get_db
from app.settings import settings

router = APIRouter(prefix="/auth/dev", tags=["auth-dev"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
def dev_register(
    email: str = Form(...),
    password: str = Form(...),
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
    
    # Check if user exists
    existing_user = user_crud.get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    
    # Create user
    password_hash = argon2.hash(password)
    user = user_crud.create_user(db, email=email, password_hash=password_hash)
    
    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at,
    }


@router.post("/login")
def dev_login(
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
    
    # Get user
    user = user_crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    # Verify password
    if not argon2.verify(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    # Create session
    session = session_crud.create_session(db, user.id)
    
    # Set cookie
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
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
    response = RedirectResponse(url="/studies", status_code=status.HTTP_303_SEE_OTHER)
    set_session(response, session.id)
    
    return response


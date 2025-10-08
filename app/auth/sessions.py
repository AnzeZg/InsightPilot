"""Session cookie utilities."""

import time

from itsdangerous import URLSafeSerializer
from starlette.requests import Request
from starlette.responses import Response

from app.settings import settings

serializer = URLSafeSerializer(settings.secret_key, salt="session")
SESSION_COOKIE = settings.session_cookie_name


def set_session(response: Response, session_id: str, max_age: int = 60 * 60 * 24 * 7) -> None:
    """
    Set session cookie on response.

    Args:
        response: Starlette response object
        session_id: Session ID to store
        max_age: Cookie expiry in seconds (default: 7 days)
    """
    token = serializer.dumps({"sid": session_id, "ts": int(time.time())})
    response.set_cookie(
        SESSION_COOKIE,
        token,
        httponly=True,
        samesite="lax",
        secure=settings.is_production,
        max_age=max_age,
    )


def get_session(request: Request) -> str | None:
    """
    Extract session ID from cookie.

    Args:
        request: Starlette request object

    Returns:
        Session ID if valid cookie exists, None otherwise
    """
    token = request.cookies.get(SESSION_COOKIE)
    if not token:
        return None
    try:
        data = serializer.loads(token)
        return data.get("sid")
    except Exception:
        return None


def clear_session(response: Response) -> None:
    """
    Clear session cookie.

    Args:
        response: Starlette response object
    """
    response.delete_cookie(SESSION_COOKIE)



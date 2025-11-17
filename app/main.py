"""Main FastAPI application entry point."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.middleware import RequestIDMiddleware
from app.routers import auth_dev, health, interview, studies, web, web_auth, web_studies
from app.settings import settings
from app.utils.logging import configure_logging

configure_logging(log_level="INFO" if settings.is_production else "DEBUG")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager for startup and shutdown events."""
    logger.info(f"InsightPilot starting in {settings.app_env} mode")
    logger.info(f"Docs available at: {app.docs_url if settings.is_development else 'disabled'}")
    yield
    logger.info("InsightPilot shutting down")


app = FastAPI(
    title="InsightPilot",
    description="AI-driven market research interview platform",
    version="0.1.0",
    docs_url="/docs" if settings.is_development else None,
    redoc_url="/redoc" if settings.is_development else None,
    lifespan=lifespan,
)

app.add_middleware(RequestIDMiddleware)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(health.router)
app.include_router(web.router)
app.include_router(web_auth.router)
app.include_router(interview.router)  # Public interview routes (no auth required)
app.include_router(studies.router)
app.include_router(web_studies.router)

if settings.is_development:
    app.include_router(auth_dev.router)

templates = Jinja2Templates(directory="app/templates")


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handle HTTP exceptions, especially 401 Unauthorized.

    Redirect to login page for 401 errors on web pages.
    """
    accept = request.headers.get("accept", "")
    wants_html = "text/html" in accept

    if exc.status_code == status.HTTP_401_UNAUTHORIZED and wants_html:
        next_url = str(request.url.path)
        if request.url.query:
            next_url += f"?{request.url.query}"
        return RedirectResponse(
            url=f"/login?next={next_url}",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    # For API requests, return JSON (let FastAPI handle it)
    if not wants_html:
        from fastapi.responses import JSONResponse

        return JSONResponse(
            content={"detail": exc.detail},
            status_code=exc.status_code,
        )

    return templates.TemplateResponse(
        request=request,
        name="error.html",
        context={
            "request_id": getattr(request.state, "request_id", "unknown"),
            "error": exc.detail,
            "status_code": exc.status_code,
        },
        status_code=exc.status_code,
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception) -> HTMLResponse:
    """
    Global exception handler for unhandled errors.

    Args:
        request: FastAPI request object
        exc: The exception that was raised

    Returns:
        HTMLResponse: Friendly error page
    """
    request_id = getattr(request.state, "request_id", "unknown")
    logger.exception(f"Unhandled exception | request_id={request_id} | error={exc}")

    return templates.TemplateResponse(
        "error.html",
        {"request": request, "request_id": request_id, "error": str(exc)},
        status_code=500,
    )

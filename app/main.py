"""Main FastAPI application entry point."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.middleware import RequestIDMiddleware
from app.routers import health, web
from app.settings import settings
from app.utils.logging import configure_logging

# Configure logging before creating the app
configure_logging(log_level="INFO" if settings.is_production else "DEBUG")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager for startup and shutdown events."""
    # Startup
    logger.info(f"InsightPilot starting in {settings.app_env} mode")
    logger.info(f"Docs available at: {app.docs_url if settings.is_development else 'disabled'}")
    yield
    # Shutdown
    logger.info("InsightPilot shutting down")


# Create FastAPI app
app = FastAPI(
    title="InsightPilot",
    description="AI-driven market research interview platform",
    version="0.1.0",
    docs_url="/docs" if settings.is_development else None,
    redoc_url="/redoc" if settings.is_development else None,
    lifespan=lifespan,
)

# Add middleware
app.add_middleware(RequestIDMiddleware)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(health.router)
app.include_router(web.router)

# Templates for error pages
templates = Jinja2Templates(directory="app/templates")


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


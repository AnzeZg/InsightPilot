"""Web routes for HTML pages."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(tags=["web"])


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Render the home/landing page.

    Args:
        request: FastAPI request object

    Returns:
        HTMLResponse: Rendered index template
    """
    return templates.TemplateResponse("index.html", {"request": request})

"""Health check endpoint."""

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/healthz")
async def health_check():
    """
    Health check endpoint for monitoring and load balancers.

    Returns:
        dict: Simple OK status
    """
    return {"ok": True, "service": "insightpilot"}


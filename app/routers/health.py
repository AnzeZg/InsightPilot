"""Health check endpoints for monitoring and orchestration."""

import os
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(tags=["health"])


@router.get("/healthz")
async def health_check(db: Session = Depends(get_db)):
    """
    Comprehensive health check endpoint for monitoring and load balancers.

    Checks:
    - Application is running
    - Database connectivity
    - Database query latency

    Returns:
        dict: Health status with component details
    """
    start_time = datetime.now()

    # Check database connectivity
    db_healthy = True
    db_latency_ms = -1
    db_error = None

    try:
        # Simple query to test DB connection
        db.execute(text("SELECT 1"))
        db_latency_ms = (datetime.now() - start_time).total_seconds() * 1000
    except Exception as e:
        db_healthy = False
        db_error = str(e)

    # Determine overall status
    overall_status = "healthy" if db_healthy else "unhealthy"

    response = {
        "status": overall_status,
        "service": "insightpilot",
        "version": "0.1.0",
        "environment": os.getenv("APP_ENV", "unknown"),
        "timestamp": datetime.now().isoformat(),
        "checks": {
            "database": {
                "status": "healthy" if db_healthy else "unhealthy",
                "latency_ms": round(db_latency_ms, 2),
                "error": db_error,
            },
        },
    }

    # Return 503 if unhealthy
    if overall_status == "unhealthy":
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=response,
        )

    return response

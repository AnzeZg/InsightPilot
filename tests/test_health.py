"""Tests for health check endpoint."""

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_health_check():
    """Test that the health endpoint returns 200 OK."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/healthz")

    assert response.status_code == 200
    data = response.json()
    assert data["ok"] is True
    assert data["service"] == "insightpilot"


@pytest.mark.asyncio
async def test_health_check_has_request_id():
    """Test that health endpoint includes request ID in response headers."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/healthz")

    assert "x-request-id" in response.headers
    assert len(response.headers["x-request-id"]) > 0


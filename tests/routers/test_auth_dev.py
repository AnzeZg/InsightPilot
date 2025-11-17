"""Tests for dev authentication routes."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_dev_register_success(client: AsyncClient):
    """Test successful user registration."""
    response = await client.post(
        "/auth/dev/register",
        data={"email": "newuser@example.com", "password": "securepass123"},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert "id" in data
    assert "created_at" in data
    assert "password" not in data  # Should not return password


@pytest.mark.asyncio
async def test_dev_register_duplicate_email(client: AsyncClient):
    """Test registration with duplicate email fails."""
    email = "duplicate@example.com"
    password = "password123"

    # First registration
    response1 = await client.post(
        "/auth/dev/register",
        data={"email": email, "password": password},
    )
    assert response1.status_code == 201

    # Second registration with same email
    response2 = await client.post(
        "/auth/dev/register",
        data={"email": email, "password": password},
    )
    assert response2.status_code == 400
    assert "already registered" in response2.json()["detail"].lower()


@pytest.mark.asyncio
async def test_dev_login_success(client: AsyncClient, test_user):
    """Test successful login."""
    response = await client.post(
        "/auth/dev/login",
        data={"email": test_user["email"], "password": test_user["password"]},
        follow_redirects=False,
    )

    assert response.status_code == 303  # Redirect
    assert response.headers["location"] == "/app/studies"
    assert "set-cookie" in response.headers


@pytest.mark.asyncio
async def test_dev_login_invalid_email(client: AsyncClient):
    """Test login with non-existent email fails."""
    response = await client.post(
        "/auth/dev/login",
        data={"email": "nonexistent@example.com", "password": "anything"},
        follow_redirects=False,
    )

    assert response.status_code == 401
    assert "invalid credentials" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_dev_login_invalid_password(client: AsyncClient, test_user):
    """Test login with wrong password fails."""
    response = await client.post(
        "/auth/dev/login",
        data={"email": test_user["email"], "password": "wrongpassword"},
        follow_redirects=False,
    )

    assert response.status_code == 401
    assert "invalid credentials" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_dev_logout(client: AsyncClient):
    """Test logout clears session cookie."""
    response = await client.post(
        "/auth/dev/logout",
        follow_redirects=False,
    )

    assert response.status_code == 303  # Redirect
    # Cookie should be cleared (expires in past or max-age=0)


@pytest.mark.asyncio
async def test_dev_quick_auth(client: AsyncClient):
    """Test quick auth creates user and session."""
    response = await client.get(
        "/auth/dev/quick-auth",
        follow_redirects=False,
    )

    assert response.status_code == 303
    assert response.headers["location"] == "/app/studies"
    assert "set-cookie" in response.headers


@pytest.mark.asyncio
async def test_dev_quick_auth_idempotent(client: AsyncClient):
    """Test quick auth works multiple times (doesn't fail on existing user)."""
    # First call
    response1 = await client.get("/auth/dev/quick-auth", follow_redirects=False)
    assert response1.status_code == 303

    # Second call should also work
    response2 = await client.get("/auth/dev/quick-auth", follow_redirects=False)
    assert response2.status_code == 303

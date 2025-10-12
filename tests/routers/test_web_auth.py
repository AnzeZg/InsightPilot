"""Tests for web authentication routes (HTML rendering)."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_login_page_renders(client: AsyncClient):
    """Test that login page renders successfully."""
    response = await client.get(
        "/login",
        headers={"Accept": "text/html"},
    )
    
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert b"Sign in to your account" in response.content
    assert b'action="/auth/dev/login"' in response.content


@pytest.mark.asyncio
async def test_register_page_renders(client: AsyncClient):
    """Test that register page renders successfully."""
    response = await client.get(
        "/register",
        headers={"Accept": "text/html"},
    )
    
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert b"Create your account" in response.content
    assert b'action="/auth/dev/register"' in response.content


@pytest.mark.asyncio
async def test_login_page_with_success_message(client: AsyncClient):
    """Test that login page displays success message from query param."""
    response = await client.get(
        "/login?success=Account%20created!",
        headers={"Accept": "text/html"},
    )
    
    assert response.status_code == 200
    assert b"Account created!" in response.content


@pytest.mark.asyncio
async def test_register_with_browser_returns_html(client: AsyncClient):
    """Test that registration from browser returns HTML on error."""
    response = await client.post(
        "/auth/dev/register",
        data={"email": "test@example.com", "password": "short"},  # Too short
        headers={"Accept": "text/html"},
        follow_redirects=False,
    )
    
    assert response.status_code == 400
    assert "text/html" in response.headers["content-type"]
    assert b"Password must be at least 8 characters" in response.content


@pytest.mark.asyncio
async def test_register_with_api_returns_json(client: AsyncClient):
    """Test that registration from API returns JSON on error."""
    response = await client.post(
        "/auth/dev/register",
        data={"email": "test@example.com", "password": "short"},  # Too short
        headers={"Accept": "application/json"},
        follow_redirects=False,
    )
    
    assert response.status_code == 400
    assert "application/json" in response.headers["content-type"]
    data = response.json()
    assert "password" in data["detail"].lower()


@pytest.mark.asyncio
async def test_register_password_mismatch_html(client: AsyncClient):
    """Test password confirmation mismatch shows error in HTML."""
    response = await client.post(
        "/auth/dev/register",
        data={
            "email": "test@example.com",
            "password": "password123",
            "confirm_password": "different123",
        },
        headers={"Accept": "text/html"},
        follow_redirects=False,
    )
    
    assert response.status_code == 400
    assert b"Passwords do not match" in response.content


@pytest.mark.asyncio
async def test_register_success_redirects_to_login(client: AsyncClient):
    """Test successful registration redirects to login page."""
    response = await client.post(
        "/auth/dev/register",
        data={"email": "newuser@example.com", "password": "securepass123"},
        headers={"Accept": "text/html"},
        follow_redirects=False,
    )
    
    assert response.status_code == 303
    assert "/login" in response.headers["location"]
    assert "success=" in response.headers["location"]


@pytest.mark.asyncio
async def test_register_duplicate_email_html(client: AsyncClient):
    """Test duplicate email registration shows error in HTML."""
    email = "duplicate@example.com"
    
    # First registration (API)
    await client.post(
        "/auth/dev/register",
        data={"email": email, "password": "password123"},
        headers={"Accept": "application/json"},
    )
    
    # Second registration (Browser)
    response = await client.post(
        "/auth/dev/register",
        data={"email": email, "password": "password123"},
        headers={"Accept": "text/html"},
        follow_redirects=False,
    )
    
    assert response.status_code == 400
    assert b"Email already registered" in response.content


@pytest.mark.asyncio
async def test_login_with_browser_shows_error_html(client: AsyncClient):
    """Test login with invalid credentials shows error in HTML."""
    response = await client.post(
        "/auth/dev/login",
        data={"email": "nonexistent@example.com", "password": "anything"},
        headers={"Accept": "text/html"},
        follow_redirects=False,
    )
    
    assert response.status_code == 401
    assert "text/html" in response.headers["content-type"]
    assert b"Invalid email or password" in response.content


@pytest.mark.asyncio
async def test_login_with_api_returns_json_error(client: AsyncClient):
    """Test login with invalid credentials returns JSON error for API."""
    response = await client.post(
        "/auth/dev/login",
        data={"email": "nonexistent@example.com", "password": "anything"},
        headers={"Accept": "application/json"},
        follow_redirects=False,
    )
    
    assert response.status_code == 401
    assert "application/json" in response.headers["content-type"]
    data = response.json()
    assert "invalid credentials" in data["detail"].lower()


@pytest.mark.asyncio
async def test_login_with_next_parameter(client: AsyncClient, test_user):
    """Test login redirects to 'next' parameter after successful login."""
    response = await client.post(
        "/auth/dev/login?next=/app/studies/123",
        data={"email": test_user["email"], "password": test_user["password"]},
        headers={"Accept": "text/html"},
        follow_redirects=False,
    )
    
    assert response.status_code == 303
    assert response.headers["location"] == "/app/studies/123"
    assert "set-cookie" in response.headers


@pytest.mark.asyncio
async def test_401_redirects_to_login_for_browser(authenticated_client: AsyncClient):
    """Test that 401 errors redirect browsers to login page."""
    # First, logout to clear session
    await authenticated_client.post("/auth/dev/logout", follow_redirects=False)
    
    # Try to access protected page as a browser
    response = await authenticated_client.get(
        "/app/studies",
        headers={"Accept": "text/html"},
        follow_redirects=False,
    )
    
    assert response.status_code == 303
    assert "/login" in response.headers["location"]
    assert "next=" in response.headers["location"]


@pytest.mark.asyncio
async def test_login_preserves_email_on_error(client: AsyncClient):
    """Test that login form preserves email field on error."""
    email = "user@example.com"
    response = await client.post(
        "/auth/dev/login",
        data={"email": email, "password": "wrongpassword"},
        headers={"Accept": "text/html"},
        follow_redirects=False,
    )
    
    assert response.status_code == 401
    # Email should be preserved in the form
    assert email.encode() in response.content


@pytest.mark.asyncio
async def test_register_preserves_email_on_error(client: AsyncClient):
    """Test that register form preserves email field on error."""
    email = "user@example.com"
    response = await client.post(
        "/auth/dev/register",
        data={"email": email, "password": "short"},  # Too short
        headers={"Accept": "text/html"},
        follow_redirects=False,
    )
    
    assert response.status_code == 400
    # Email should be preserved in the form
    assert email.encode() in response.content


@pytest.mark.asyncio
async def test_index_page_has_login_links(client: AsyncClient):
    """Test that home page links to login and register."""
    response = await client.get("/", headers={"Accept": "text/html"})
    
    assert response.status_code == 200
    assert b'href="/register"' in response.content
    assert b'href="/login"' in response.content


@pytest.mark.asyncio
async def test_content_negotiation_defaults_to_api(client: AsyncClient):
    """Test that without Accept header, API behavior is default."""
    # Register without Accept header should return JSON
    response = await client.post(
        "/auth/dev/register",
        data={"email": "apitest@example.com", "password": "securepass123"},
        follow_redirects=False,
    )
    
    assert response.status_code == 201
    assert "application/json" in response.headers["content-type"]


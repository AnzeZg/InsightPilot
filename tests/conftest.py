"""Shared test fixtures."""

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.models import *  # noqa: F401,F403


@pytest.fixture
def test_db():
    """Create a fresh in-memory database for each test."""
    # Use in-memory SQLite for tests
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create session factory
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    yield TestingSessionLocal
    
    # Cleanup
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(test_db):
    """Create test client with dependency override."""
    def override_get_db():
        db = test_db()
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    
    yield AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
    
    app.dependency_overrides.clear()


@pytest.fixture
async def test_user(client: AsyncClient):
    """Create a test user and return credentials."""
    response = await client.post(
        "/auth/dev/register",
        data={"email": "test@example.com", "password": "testpass123"},
    )
    assert response.status_code == 201
    return {"email": "test@example.com", "password": "testpass123"}


@pytest.fixture
async def authenticated_client(client: AsyncClient, test_user):
    """Create an authenticated client with session cookie."""
    response = await client.post(
        "/auth/dev/login",
        data={"email": test_user["email"], "password": test_user["password"]},
        follow_redirects=False,
    )
    assert response.status_code == 303
    # Cookie should be set automatically
    return client


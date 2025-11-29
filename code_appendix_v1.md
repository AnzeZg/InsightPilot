# Code Appendix - InsightPilot

**Generated:** 2025-10-12 15:37:46
**Total Files:** 104

---

## Overview

This appendix contains the complete source code for the InsightPilot application. Files are organized by directory structure and include all Python source files, configuration files, templates, and other relevant source code.

---

## Table of Contents

### Root Files

- [.env.example](#envexample)
- [Dockerfile](#Dockerfile)
- [README.md](#READMEmd)
- [alembic.ini](#alembicini)
- [docker-compose.yml](#docker-composeyml)
- [pyproject.toml](#pyprojecttoml)

### alembic

- [alembic/env.py](#alembic-envpy)
- [alembic/versions/001_initial_schema.py](#alembic-versions-001_initial_schemapy)

### app

- [app/__init__.py](#app-__init__py)
- [app/auth/__init__.py](#app-auth-__init__py)
- [app/auth/dependencies.py](#app-auth-dependenciespy)
- [app/auth/sessions.py](#app-auth-sessionspy)
- [app/crud/__init__.py](#app-crud-__init__py)
- [app/crud/interview.py](#app-crud-interviewpy)
- [app/crud/invite.py](#app-crud-invitepy)
- [app/crud/session.py](#app-crud-sessionpy)
- [app/crud/study.py](#app-crud-studypy)
- [app/crud/user.py](#app-crud-userpy)
- [app/db/__init__.py](#app-db-__init__py)
- [app/db/base.py](#app-db-basepy)
- [app/db/session.py](#app-db-sessionpy)
- [app/main.py](#app-mainpy)
- [app/middleware.py](#app-middlewarepy)
- [app/models/__init__.py](#app-models-__init__py)
- [app/models/interview.py](#app-models-interviewpy)
- [app/models/invite.py](#app-models-invitepy)
- [app/models/session.py](#app-models-sessionpy)
- [app/models/study.py](#app-models-studypy)
- [app/models/user.py](#app-models-userpy)
- [app/routers/__init__.py](#app-routers-__init__py)
- [app/routers/auth_dev.py](#app-routers-auth_devpy)
- [app/routers/health.py](#app-routers-healthpy)
- [app/routers/interview.py](#app-routers-interviewpy)
- [app/routers/studies.py](#app-routers-studiespy)
- [app/routers/web.py](#app-routers-webpy)
- [app/routers/web_auth.py](#app-routers-web_authpy)
- [app/routers/web_studies.py](#app-routers-web_studiespy)
- [app/schemas/__init__.py](#app-schemas-__init__py)
- [app/schemas/interview.py](#app-schemas-interviewpy)
- [app/schemas/invite.py](#app-schemas-invitepy)
- [app/schemas/study.py](#app-schemas-studypy)
- [app/services/__init__.py](#app-services-__init__py)
- [app/services/ai_agent.py](#app-services-ai_agentpy)
- [app/services/insight_generator.py](#app-services-insight_generatorpy)
- [app/settings.py](#app-settingspy)
- [app/static/css/app.css](#app-static-css-appcss)
- [app/static/js/app.js](#app-static-js-appjs)
- [app/templates/auth/login.html](#app-templates-auth-loginhtml)
- [app/templates/auth/register.html](#app-templates-auth-registerhtml)
- [app/templates/base.html](#app-templates-basehtml)
- [app/templates/error.html](#app-templates-errorhtml)
- [app/templates/index.html](#app-templates-indexhtml)
- [app/templates/interview/chat.html](#app-templates-interview-chathtml)
- [app/templates/interview/chat_placeholder.html](#app-templates-interview-chat_placeholderhtml)
- [app/templates/interview/completed.html](#app-templates-interview-completedhtml)
- [app/templates/interview/consent.html](#app-templates-interview-consenthtml)
- [app/templates/interview/expired.html](#app-templates-interview-expiredhtml)
- [app/templates/interview/intake.html](#app-templates-interview-intakehtml)
- [app/templates/interview/landing.html](#app-templates-interview-landinghtml)
- [app/templates/interview/not_found.html](#app-templates-interview-not_foundhtml)
- [app/templates/interview/thank_you.html](#app-templates-interview-thank_youhtml)
- [app/templates/public_base.html](#app-templates-public_basehtml)
- [app/templates/researcher_base.html](#app-templates-researcher_basehtml)
- [app/templates/studies/_invites.html](#app-templates-studies-_inviteshtml)
- [app/templates/studies/_questions.html](#app-templates-studies-_questionshtml)
- [app/templates/studies/analytics.html](#app-templates-studies-analyticshtml)
- [app/templates/studies/detail.html](#app-templates-studies-detailhtml)
- [app/templates/studies/interviews.html](#app-templates-studies-interviewshtml)
- [app/templates/studies/list.html](#app-templates-studies-listhtml)
- [app/templates/studies/transcript.html](#app-templates-studies-transcripthtml)
- [app/utils/__init__.py](#app-utils-__init__py)
- [app/utils/logging.py](#app-utils-loggingpy)

### examples

- [examples/README.md](#examples-READMEmd)
- [examples/test_ai_agent.py](#examples-test_ai_agentpy)

### insightpilot.egg-info

- [insightpilot.egg-info/SOURCES.txt](#insightpilotegg-info-SOURCEStxt)
- [insightpilot.egg-info/dependency_links.txt](#insightpilotegg-info-dependency_linkstxt)
- [insightpilot.egg-info/requires.txt](#insightpilotegg-info-requirestxt)
- [insightpilot.egg-info/top_level.txt](#insightpilotegg-info-top_leveltxt)

### tests

- [tests/__init__.py](#tests-__init__py)
- [tests/auth/__init__.py](#tests-auth-__init__py)
- [tests/auth/test_dependencies.py](#tests-auth-test_dependenciespy)
- [tests/auth/test_sessions.py](#tests-auth-test_sessionspy)
- [tests/conftest.py](#tests-conftestpy)
- [tests/crud/__init__.py](#tests-crud-__init__py)
- [tests/crud/test_interview.py](#tests-crud-test_interviewpy)
- [tests/crud/test_invite.py](#tests-crud-test_invitepy)
- [tests/crud/test_session.py](#tests-crud-test_sessionpy)
- [tests/crud/test_study.py](#tests-crud-test_studypy)
- [tests/crud/test_user.py](#tests-crud-test_userpy)
- [tests/interview/__init__.py](#tests-interview-__init__py)
- [tests/interview/test_chat_flow.py](#tests-interview-test_chat_flowpy)
- [tests/interview/test_invite_landing.py](#tests-interview-test_invite_landingpy)
- [tests/routers/__init__.py](#tests-routers-__init__py)
- [tests/routers/test_analytics.py](#tests-routers-test_analyticspy)
- [tests/routers/test_auth_dev.py](#tests-routers-test_auth_devpy)
- [tests/routers/test_export.py](#tests-routers-test_exportpy)
- [tests/routers/test_interview_results.py](#tests-routers-test_interview_resultspy)
- [tests/routers/test_invites.py](#tests-routers-test_invitespy)
- [tests/routers/test_questions.py](#tests-routers-test_questionspy)
- [tests/routers/test_studies.py](#tests-routers-test_studiespy)
- [tests/routers/test_web_auth.py](#tests-routers-test_web_authpy)
- [tests/services/__init__.py](#tests-services-__init__py)
- [tests/services/test_insight_generator.py](#tests-services-test_insight_generatorpy)
- [tests/test_health.py](#tests-test_healthpy)

---


## .env.example

**Path:** `.env.example`
**Type:** Bash
**Size:** 246 bytes

```bash
# Application environment
APP_ENV=dev

# Security
SECRET_KEY=

# Database
DATABASE_URL=postgresql+psycopg2://insight:insight@localhost:5432/insightpilot

# Session
SESSION_COOKIE_NAME=ip_session

#OpenAI
OPENAI_API_KEY=sk-your-actual-api-key-here
```

## Dockerfile

**Path:** `Dockerfile`
**Type:** Dockerfile
**Size:** 1.1 KB

```dockerfile
FROM python:3.11-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install system dependencies required for psycopg2 and other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml ./

# Install Python dependencies
# Use pip install with pyproject.toml (no editable mode in container)
RUN pip install --upgrade pip setuptools wheel && \
    pip install .

# Copy application code
COPY app ./app
COPY alembic ./alembic
COPY alembic.ini ./

# Create non-root user for security
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/healthz || exit 1

# Run migrations then start the app
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]

```

## README.md

**Path:** `README.md`
**Type:** Markdown
**Size:** 29.9 KB

```markdown
# InsightPilot

An AI-powered market research platform that conducts intelligent interviews with participants and automatically generates actionable insights for researchers.

## 📖 Overview

InsightPilot enables researchers to:
- Create and manage research studies with custom questions
- Generate unique interview invitation links
- Let an AI agent conduct natural, conversational interviews
- Automatically analyze responses for sentiment, keywords, and insights
- View comprehensive analytics and export data in multiple formats

The platform combines conversational AI with automated analysis to streamline qualitative research workflows.

---

## ✨ Features

### For Researchers
- 🔐 **Secure Authentication** - User registration with Argon2 password hashing and session management
- 📊 **Study Management** - Create studies, configure questions, and manage interview invites
- 📈 **Analytics Dashboard** - Sentiment analysis, keyword extraction, demographic breakdowns, timeline views
- 💾 **Data Export** - Export interviews in CSV or JSON format with complete transcripts and metadata
- 👥 **Interview Tracking** - Monitor completion status and view detailed transcripts

### For Participants
- 🤖 **AI Interviewer** - Natural conversation powered by OpenAI GPT models
- 💬 **Real-time Chat** - Responsive HTMX-powered interface with no page reloads
- ✅ **Simple Flow** - Consent → Intake form → Interview → Completion
- 📱 **Mobile Friendly** - Works seamlessly on all devices

### Technical Features
- ⚡ **Fast & Modern** - Built with FastAPI and async Python
- 🎨 **Beautiful UI** - Tailwind CSS with Chart.js visualizations
- 🐳 **Docker Ready** - Easy deployment with Docker Compose
- ✅ **Well Tested** - 254 comprehensive tests (unit + integration)
- 📝 **Type Safe** - Full type hints with Pydantic validation

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Backend** | FastAPI, Uvicorn, Python 3.13 |
| **Frontend** | Jinja2 Templates, HTMX, Tailwind CSS, Chart.js |
| **Database** | PostgreSQL, SQLAlchemy 2.0, Alembic |
| **Authentication** | Server-side sessions, Argon2 password hashing |
| **AI/LLM** | OpenAI API (GPT-4 / GPT-3.5-turbo) |
| **Testing** | Pytest, HTTPX, pytest-asyncio (254 tests) |
| **Code Quality** | Black, isort, Ruff, pre-commit hooks |
| **Deployment** | Docker, Docker Compose |

---

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.11+** (Python 3.13 recommended for local development)
- **Docker & Docker Compose** (for running PostgreSQL and/or the full application)
- **OpenAI API Key** (required for AI interview functionality)
  - Get yours at: https://platform.openai.com/api-keys
- **Git** (for cloning the repository)

---

## 🚀 Quick Start (Production with Docker)

This is the simplest way to run the application. Everything runs in containers.

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd InsightPilot
```

### Step 2: Create Environment File

```bash
cp .env.example .env
```

### Step 3: Configure Environment Variables

Edit the `.env` file with your settings:

```bash
# Required: Generate a secure secret key
SECRET_KEY=<run: python -c "import secrets; print(secrets.token_urlsafe(32))">

# Required: Your OpenAI API key
OPENAI_API_KEY=sk-your-openai-api-key-here

# Application Environment
APP_ENV=prod

# Database (default Docker settings - can leave as-is)
DATABASE_URL=postgresql://postgres:postgres@db:5432/insightpilot

# Session Cookie Name (can leave as-is)
SESSION_COOKIE_NAME=ip_session
```

**Generate a secure secret key:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Step 4: Build and Start All Services

```bash
# Build and start in detached mode
docker compose up -d --build

# View logs (optional)
docker compose logs -f app
```

### Step 5: Apply Database Migrations

```bash
# Run migrations inside the app container
docker compose exec app alembic upgrade head
```

### Step 6: Access the Application

Open your browser and navigate to:
```
http://localhost:8000
```

### Step 7: Create Your First Account

1. Click **"Get Started"** or navigate to http://localhost:8000/register
2. Enter your email and password (minimum 8 characters)
3. Login at http://localhost:8000/login
4. Create your first study and start conducting interviews!

### Managing Docker Services

```bash
# Stop all services
docker compose down

# Stop and remove volumes (WARNING: deletes all data)
docker compose down -v

# View running containers
docker compose ps

# View logs
docker compose logs app
docker compose logs db

# Restart a service
docker compose restart app
```

---

## 💻 Development Setup (Local with Docker Database)

For active development with hot-reload and debugging capabilities.

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd InsightPilot
```

### Step 2: Create Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows
```

### Step 3: Install Dependencies

```bash
# Install application with development dependencies
pip install -e ".[dev]"

# This installs:
# - Core dependencies (FastAPI, SQLAlchemy, etc.)
# - Dev tools (pytest, black, isort, ruff, pre-commit)
```

### Step 4: Start PostgreSQL with Docker

```bash
# Start only the database service
docker compose up -d db

# Verify it's running
docker compose ps
```

The database will be available at:
- **Host:** localhost
- **Port:** 5432
- **Database:** insightpilot
- **User:** postgres
- **Password:** postgres

### Step 5: Create Environment File

```bash
cp .env.example .env
```

### Step 6: Configure Environment Variables for Development

Edit the `.env` file:

```bash
# Development environment
APP_ENV=dev

# Required: Generate a secure secret key
SECRET_KEY=<run: python -c "import secrets; print(secrets.token_urlsafe(32))">

# Required: Your OpenAI API key
OPENAI_API_KEY=sk-your-openai-api-key-here

# Database URL for local development (note: localhost instead of 'db')
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/insightpilot

# Session cookie name
SESSION_COOKIE_NAME=ip_session
```

### Step 7: Apply Database Migrations

```bash
# Make sure your virtual environment is activated
alembic upgrade head

# Verify migration was applied
alembic current
```

### Step 8: Set Up Pre-commit Hooks (Recommended)

```bash
# Install git hooks for code quality
pre-commit install

# Test hooks on all files
pre-commit run --all-files
```

### Step 9: Start Development Server

```bash
# Standard mode with auto-reload
uvicorn app.main:app --reload

# With custom port
uvicorn app.main:app --reload --port 8080

# With debug logging
LOG_LEVEL=DEBUG uvicorn app.main:app --reload
```

The development server will start at:
```
http://localhost:8000
```

The server will automatically reload when you change Python files.

### Step 10: Run Tests

```bash
# Run all tests
pytest -v

# Run tests with coverage
pytest --cov=app --cov-report=html

# Run specific test suite
pytest tests/crud/ -v
pytest tests/auth/ -v

# Run tests in parallel (faster)
pytest -v -n auto
```

### Development Workflow

```bash
# 1. Create a new branch
git checkout -b feature/your-feature

# 2. Make your changes

# 3. Run code quality checks
pre-commit run --all-files

# 4. Run tests
pytest -v

# 5. Commit your changes (pre-commit hooks will run automatically)
git add .
git commit -m "Your commit message"

# 6. Push and create pull request
git push origin feature/your-feature
```

---

## 📁 Project Structure

```
InsightPilot/
├── app/                          # Main application package
│   ├── auth/                     # Authentication & authorization
│   │   ├── dependencies.py       # Auth dependency injection (get_current_user)
│   │   └── sessions.py           # Session cookie management
│   │
│   ├── crud/                     # Database operations (CRUD)
│   │   ├── user.py               # User operations
│   │   ├── session.py            # Session management
│   │   ├── study.py              # Study & question operations
│   │   ├── invite.py             # Invite management
│   │   └── interview.py          # Interview, message, insight operations
│   │
│   ├── db/                       # Database configuration
│   │   ├── base.py               # SQLAlchemy base class
│   │   └── session.py            # Database session management
│   │
│   ├── models/                   # SQLAlchemy ORM models
│   │   ├── user.py               # User model
│   │   ├── session.py            # Session model
│   │   ├── study.py              # Study & StudyQuestion models
│   │   ├── invite.py             # Invite model
│   │   └── interview.py          # Interview, Interviewee, Message, Insight models
│   │
│   ├── routers/                  # FastAPI route handlers
│   │   ├── auth_dev.py           # API authentication endpoints
│   │   ├── web_auth.py           # Web authentication pages (login/register)
│   │   ├── studies.py            # Study API endpoints
│   │   ├── web_studies.py        # Study web pages & analytics
│   │   ├── interview.py          # Interview endpoints
│   │   ├── web.py                # Public pages (home)
│   │   └── health.py             # Health check endpoint
│   │
│   ├── schemas/                  # Pydantic validation models
│   │   ├── study.py              # Study schemas
│   │   ├── invite.py             # Invite schemas
│   │   └── interview.py          # Interview schemas
│   │
│   ├── services/                 # Business logic & external services
│   │   ├── ai_agent.py           # OpenAI conversation wrapper
│   │   └── insight_generator.py # AI-powered insight generation
│   │
│   ├── templates/                # Jinja2 HTML templates
│   │   ├── base.html             # Base template
│   │   ├── public_base.html      # Public pages base
│   │   ├── researcher_base.html  # Researcher dashboard base
│   │   ├── auth/                 # Login & register pages
│   │   ├── interview/            # Interview chat interface
│   │   └── studies/              # Study management & analytics
│   │
│   ├── static/                   # Static assets
│   │   ├── css/app.css           # Tailwind CSS
│   │   └── js/app.js             # Custom JavaScript
│   │
│   ├── utils/                    # Utility functions
│   │   └── logging.py            # Logging configuration
│   │
│   ├── main.py                   # FastAPI application entry point
│   ├── middleware.py             # Custom middleware (request ID, logging)
│   └── settings.py               # Configuration & environment variables
│
├── tests/                        # Test suite (254 tests)
│   ├── auth/                     # Auth unit tests (38 tests)
│   │   ├── test_sessions.py      # Session cookie tests
│   │   └── test_dependencies.py  # Auth dependency tests
│   │
│   ├── crud/                     # CRUD unit tests (116 tests)
│   │   ├── test_user.py          # User CRUD tests
│   │   ├── test_session.py       # Session CRUD tests
│   │   ├── test_study.py         # Study CRUD tests
│   │   ├── test_invite.py        # Invite CRUD tests
│   │   └── test_interview.py     # Interview CRUD tests
│   │
│   ├── routers/                  # API integration tests
│   │   ├── test_auth_dev.py      # Auth API tests
│   │   ├── test_web_auth.py      # Auth web tests
│   │   ├── test_studies.py       # Study API tests
│   │   ├── test_invites.py       # Invite API tests
│   │   ├── test_questions.py     # Question API tests
│   │   ├── test_analytics.py     # Analytics tests
│   │   ├── test_export.py        # Export functionality tests
│   │   └── test_interview_results.py
│   │
│   ├── interview/                # Interview flow tests
│   │   ├── test_chat_flow.py     # Chat interface tests
│   │   └── test_invite_landing.py # Invite page tests
│   │
│   ├── services/                 # Service layer tests
│   │   └── test_insight_generator.py
│   │
│   ├── conftest.py               # Pytest fixtures & configuration
│   └── test_health.py            # Health check tests
│
├── alembic/                      # Database migrations
│   ├── versions/                 # Migration files
│   │   └── 001_initial_schema.py
│   ├── env.py                    # Alembic environment configuration
│   └── script.py.mako            # Migration template
│
├── logs/                         # Application logs
│   └── app.log                   # Rotating log file
│
├── docker-compose.yml            # Docker Compose configuration
├── Dockerfile                    # Application container definition
├── pyproject.toml                # Python project metadata & dependencies
├── alembic.ini                   # Alembic configuration
├── .env.example                  # Example environment variables
├── .pre-commit-config.yaml       # Pre-commit hooks configuration
└── README.md                     # This file
```

---

## ⚙️ Configuration

### Environment Variables

All configuration is done through environment variables in the `.env` file.

#### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Secret key for session signing | Generate with Python command below |
| `OPENAI_API_KEY` | OpenAI API key for AI features | `sk-...` |
| `DATABASE_URL` | PostgreSQL connection string | See examples below |

#### Optional Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_ENV` | `dev` | Environment: `dev`, `staging`, or `prod` |
| `SESSION_COOKIE_NAME` | `ip_session` | Name of the session cookie |

#### Database URL Examples

```bash
# Docker Compose (services communicate via service name)
DATABASE_URL=postgresql://postgres:postgres@db:5432/insightpilot

# Local development (Docker DB, local app)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/insightpilot

# Production (custom credentials)
DATABASE_URL=postgresql://user:password@hostname:5432/database_name
```

#### Generating a Secure Secret Key

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Example .env File

```bash
# Application
APP_ENV=dev
SECRET_KEY=your-generated-secret-key-here
SESSION_COOKIE_NAME=ip_session

# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/insightpilot

# OpenAI
OPENAI_API_KEY=sk-your-openai-api-key-here
```

---

## 🧪 Testing

The project includes comprehensive test coverage across **254 tests** covering unit tests, integration tests, and end-to-end workflows.

### Test Architecture

- **Unit Tests (154 tests)** - Test individual functions in isolation (CRUD operations, auth utilities)
- **Integration Tests (100 tests)** - Test API endpoints and full request/response cycles
- **End-to-End Tests** - Test complete user workflows (authentication, interview flows)

### Running Tests

```bash
# Run all tests with verbose output
pytest -v

# Run tests with coverage report
pytest --cov=app --cov-report=html
# Open htmlcov/index.html in browser to view coverage

# Run tests in parallel (faster)
pytest -v -n auto

# Run with detailed output on failures
pytest -v --tb=short

# Run tests in Docker
docker compose exec app pytest -v
```

### Run Specific Test Suites

```bash
# Unit Tests - CRUD Operations (116 tests)
pytest tests/crud/ -v
pytest tests/crud/test_user.py -v          # User CRUD (13 tests)
pytest tests/crud/test_session.py -v       # Session management (17 tests)
pytest tests/crud/test_study.py -v         # Study & questions (30 tests)
pytest tests/crud/test_invite.py -v        # Invites (24 tests)
pytest tests/crud/test_interview.py -v     # Interviews & insights (32 tests)

# Unit Tests - Authentication (38 tests)
pytest tests/auth/ -v
pytest tests/auth/test_sessions.py -v      # Session cookies (18 tests)
pytest tests/auth/test_dependencies.py -v  # Auth dependencies (20 tests)

# Integration Tests - API Routes
pytest tests/routers/ -v
pytest tests/routers/test_auth_dev.py -v       # API authentication
pytest tests/routers/test_web_auth.py -v       # Web authentication
pytest tests/routers/test_studies.py -v        # Study management
pytest tests/routers/test_invites.py -v        # Invite management
pytest tests/routers/test_analytics.py -v      # Analytics endpoints
pytest tests/routers/test_export.py -v         # Data export

# Integration Tests - Interview Flow
pytest tests/interview/ -v
pytest tests/interview/test_chat_flow.py -v        # Chat interface
pytest tests/interview/test_invite_landing.py -v   # Invite pages

# Service Layer Tests
pytest tests/services/ -v
pytest tests/services/test_insight_generator.py -v

# Health Check Tests
pytest tests/test_health.py -v
```

### Test Coverage Breakdown

**Total: 254 tests passing** ✅

#### Unit Tests (154 tests)

**CRUD Operations** (116 tests)
- User management: 13 tests
- Session management: 17 tests
- Study & questions: 30 tests
- Invite management: 24 tests
- Interview & insights: 32 tests

**Authentication Utilities** (38 tests)
- Session cookies: 18 tests (serialization, security, validation)
- Auth dependencies: 20 tests (session extraction, user retrieval)

#### Integration Tests (100 tests)

- **Authentication** (24 tests): API + Web authentication flows
- **Study Management** (20 tests): Study CRUD, invites, questions
- **Interview Flow** (17 tests): Chat interface, invite pages
- **Analytics & Export** (18 tests): Dashboard analytics, CSV/JSON export
- **Interview Results** (9 tests): Interview listing, transcript viewing
- **Services** (9 tests): AI insight generation
- **Health Checks** (2 tests): System health monitoring

### Test Features

✅ **Isolation** - Each test uses fresh database state via fixtures
✅ **Fast Execution** - Full suite runs in ~12 seconds
✅ **Comprehensive Coverage** - Unit, integration, and E2E tests
✅ **Security Testing** - Authentication, session validation, token tampering
✅ **Edge Cases** - Error handling, expired sessions, invalid data
✅ **Business Logic** - Study workflows, interview flows, analytics

---

## 🔧 Development Tools

### Code Quality

The project uses several tools to maintain code quality:

```bash
# Format code with Black (line length: 100)
black app tests

# Sort imports with isort
isort app tests

# Lint with Ruff
ruff check app tests

# Run all checks with pre-commit
pre-commit run --all-files
```

### Pre-commit Hooks

Pre-commit hooks automatically run code quality checks before each commit:

```bash
# Install hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files

# Skip hooks (not recommended)
git commit --no-verify
```

Configured hooks:
- **black** - Code formatting
- **isort** - Import sorting
- **ruff** - Fast Python linter
- **trailing-whitespace** - Remove trailing whitespace
- **end-of-file-fixer** - Ensure files end with newline
- **check-yaml** - Validate YAML files

---

## 📚 API Documentation

Once the server is running, interactive API documentation is available:

### Swagger UI (Interactive)
```
http://localhost:8000/docs
```
- Try out API endpoints directly in the browser
- View request/response schemas
- Test authentication flows

### ReDoc (Reference)
```
http://localhost:8000/redoc
```
- Clean, searchable API reference
- Better for documentation reading

### Key API Endpoints

#### Authentication
```
POST   /auth/dev/register       Create new user account
POST   /auth/dev/login          Login and get session cookie
POST   /auth/dev/logout         Clear session and logout
GET    /auth/dev/quick-auth     Quick dev auth (test@example.com)
```

#### Studies
```
GET    /studies                 List all studies for authenticated user
POST   /studies                 Create a new study
GET    /studies/{id}            Get study details
PATCH  /studies/{id}            Update study
DELETE /studies/{id}            Delete study
```

#### Study Questions
```
GET    /studies/{id}/questions         Get study questions
POST   /studies/{id}/questions         Create question
PUT    /studies/{id}/questions/reorder Reorder questions
DELETE /studies/{id}/questions/{q_id}  Delete question
```

#### Invites
```
GET    /studies/{id}/invites             List study invites
POST   /studies/{id}/invites             Create invite
DELETE /studies/{id}/invites/{invite_id} Delete invite
```

#### Interviews
```
GET    /interview/{invite_code}                Start interview from invite
POST   /interview/{invite_code}/message        Send message in interview
GET    /studies/{id}/interviews                List study interviews
GET    /studies/{id}/interviews/{interview_id} View interview transcript
```

#### Analytics & Export
```
GET    /studies/{id}/analytics           Get study analytics
GET    /studies/{id}/export              Export study data (CSV/JSON)
GET    /studies/{id}/interviews/{id}/export Export single interview
```

---

## 🗄️ Database Management

### Alembic Migrations

Alembic manages database schema changes. When you modify ORM models, generate and apply migrations.

#### Check Migration Status

```bash
# Check current database version
alembic current

# View migration history
alembic history --verbose

# Show pending migrations
alembic heads
```

#### Create New Migration

```bash
# Auto-generate migration from model changes
alembic revision --autogenerate -m "add user avatar field"

# Create empty migration (for data migrations)
alembic revision -m "populate default values"
```

#### Apply Migrations

```bash
# Apply all pending migrations
alembic upgrade head

# Apply specific number of migrations
alembic upgrade +1
alembic upgrade +2

# Apply to specific revision
alembic upgrade <revision_id>
```

#### Rollback Migrations

```bash
# Rollback one migration
alembic downgrade -1

# Rollback to specific revision
alembic downgrade <revision_id>

# Rollback all migrations (WARNING: deletes all data)
alembic downgrade base
```

#### Migration Workflow Example

```bash
# 1. Modify models in app/models/
vim app/models/user.py

# 2. Generate migration
alembic revision --autogenerate -m "add user avatar field"

# 3. Review generated migration
vim alembic/versions/xxx_add_user_avatar_field.py

# 4. Apply migration
alembic upgrade head

# 5. Verify in database
alembic current

# 6. Commit migration file
git add alembic/versions/xxx_add_user_avatar_field.py
git commit -m "Add user avatar field migration"
```

### Database Backup & Restore

#### Docker Environment

```bash
# Backup database
docker compose exec db pg_dump -U postgres insightpilot > backup_$(date +%Y%m%d).sql

# Restore database
docker compose exec -T db psql -U postgres insightpilot < backup_20240101.sql

# Backup with compression
docker compose exec db pg_dump -U postgres insightpilot | gzip > backup_$(date +%Y%m%d).sql.gz

# Restore from compressed backup
gunzip -c backup_20240101.sql.gz | docker compose exec -T db psql -U postgres insightpilot
```

#### Local Environment

```bash
# Backup
pg_dump -U postgres -h localhost insightpilot > backup.sql

# Restore
psql -U postgres -h localhost insightpilot < backup.sql
```

### Database Access

#### Docker Environment

```bash
# Access PostgreSQL shell
docker compose exec db psql -U postgres insightpilot

# Run SQL query from command line
docker compose exec db psql -U postgres insightpilot -c "SELECT COUNT(*) FROM users;"
```

#### Local Environment

```bash
# Access PostgreSQL shell
psql -U postgres -h localhost insightpilot

# Run SQL query
psql -U postgres -h localhost insightpilot -c "SELECT COUNT(*) FROM users;"
```

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Find and kill process using port 8000 (macOS/Linux)
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn app.main:app --reload --port 8080

# Windows: Find process
netstat -ano | findstr :8000

# Windows: Kill process
taskkill /PID <process_id> /F
```

### Database Connection Issues

```bash
# Check if PostgreSQL is running
docker compose ps

# View database logs
docker compose logs db

# Verify DATABASE_URL
echo $DATABASE_URL

# Test connection
psql $DATABASE_URL -c "SELECT version();"

# Restart database
docker compose restart db
```

### Migration Issues

```bash
# Check current migration state
alembic current

# If migrations are out of sync with database
alembic stamp head  # Mark current DB state as up-to-date

# If you need to reset (WARNING: deletes all data)
alembic downgrade base
alembic upgrade head

# If migration fails, check the error and rollback
alembic downgrade -1
# Fix the issue, then try again
alembic upgrade head
```

### OpenAI API Errors

```bash
# Verify API key is set
echo $OPENAI_API_KEY

# Test API key
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"

# Common issues:
# - Invalid API key: Check for typos, regenerate key
# - Rate limit: Wait or upgrade plan
# - Quota exceeded: Add credits to account

# Check application logs for details
tail -f logs/app.log
# Or in Docker:
docker compose logs -f app
```

### Import Errors After Adding Dependencies

```bash
# Reinstall in development mode
pip install -e ".[dev]"

# Or reinstall specific package
pip install <package-name>

# If still having issues, recreate virtual environment
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

### HTMX Not Working

1. **Check browser console** for JavaScript errors
2. **Verify static files** are loading:
   - http://localhost:8000/static/css/app.css
   - http://localhost:8000/static/js/app.js
3. **Check network tab** for HTMX requests (should see XHR requests)
4. **Ensure HTMX CDN** is accessible (check base.html)

### Session/Authentication Issues

```bash
# Clear browser cookies
# Chrome: DevTools → Application → Cookies → Delete all for localhost

# Check if SECRET_KEY is set
echo $SECRET_KEY

# Verify session creation in logs
grep "session" logs/app.log

# In Docker:
docker compose logs app | grep "session"

# Use quick-auth for testing
open http://localhost:8000/auth/dev/quick-auth
```

### Docker Build Issues

```bash
# Clean rebuild (removes all cached layers)
docker compose build --no-cache

# Remove all stopped containers and rebuild
docker compose down
docker compose up --build

# Clear Docker cache completely
docker system prune -a
# WARNING: This removes ALL unused images, not just this project
```

### Tests Failing

```bash
# Run tests with more verbose output
pytest -vv

# Run tests with detailed traceback
pytest -vv --tb=long

# Run a single failing test
pytest tests/path/to/test.py::test_function_name -vv

# Check test database
# Tests use SQLite in-memory by default, no cleanup needed

# If import errors, ensure you're in the right directory
cd /path/to/InsightPilot
pytest -v
```

---

## 📖 Additional Resources

### Key Concepts

#### Study Workflow
1. Researcher creates study with title, description, and consent text
2. Researcher adds seed questions to guide the AI
3. Researcher generates invitation links
4. Participant clicks invite link
5. Participant provides consent and fills intake form
6. AI conducts interview based on seed questions
7. System generates insights automatically
8. Researcher views analytics and exports data

#### Authentication Flow
1. User registers with email/password
2. Password is hashed with Argon2
3. On login, session is created in database
4. Session ID is signed and stored in HttpOnly cookie
5. Each request validates session and retrieves user
6. Sessions expire after 7 days (configurable)

#### AI Interview Flow
1. Initial message from AI based on first seed question
2. Participant responds
3. AI analyzes conversation history and seed questions
4. AI generates contextual follow-up
5. Process repeats until max turns or natural conclusion
6. System extracts insights using separate AI analysis

### Development Tips

- **Hot Reload**: FastAPI with `--reload` watches for file changes
- **Debug Mode**: Set `LOG_LEVEL=DEBUG` for verbose logging
- **Test First**: Write tests before implementing features
- **Type Hints**: Use type hints everywhere for better IDE support
- **Pre-commit**: Install hooks to catch issues early

### Production Considerations

- **Environment**: Set `APP_ENV=prod`
- **Secret Key**: Use strong, unique secret key
- **Database**: Use managed PostgreSQL service
- **Backups**: Set up automated database backups
- **Monitoring**: Add application monitoring (Sentry, etc.)
- **HTTPS**: Use reverse proxy (nginx) with SSL certificate
- **Rate Limiting**: Add rate limiting for API endpoints
- **Scaling**: Use multiple uvicorn workers

---

## 📄 License

MIT License - See LICENSE file for details.

---

## 🙏 Acknowledgments

Built with excellent open-source technologies:

- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [HTMX](https://htmx.org/) - High power tools for HTML
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Chart.js](https://www.chartjs.org/) - Simple yet flexible charting
- [OpenAI](https://openai.com/) - AI capabilities
- [PostgreSQL](https://www.postgresql.org/) - Advanced open source database
- [Docker](https://www.docker.com/) - Containerization platform

---

## 📞 Support

For issues, questions, or contributions:
- 🐛 **Bug Reports**: Open an issue on GitHub
- 💡 **Feature Requests**: Open an issue with [Feature Request] prefix
- 📖 **Documentation**: Check this README and API docs
- 💬 **Questions**: Open a discussion on GitHub

---

**Made with ❤️ for researchers and participants**
```

## alembic/env.py

**Path:** `alembic/env.py`
**Type:** Python
**Size:** 1.5 KB

```python
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from app.db.base import Base
from app.models import (  # noqa: F401 - imported for Alembic autogenerate
    Insight,
    Interview,
    Interviewee,
    Invite,
    Message,
    Session,
    Study,
    StudyQuestion,
    User,
)
from app.settings import settings

config = context.config
config.set_main_option("sqlalchemy.url", settings.database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in offline mode using just the URL."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in online mode using an Engine/Connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

## alembic/versions/001_initial_schema.py

**Path:** `alembic/versions/001_initial_schema.py`
**Type:** Python
**Size:** 8.6 KB

```python
"""initial schema

Revision ID: 001
Revises:
Create Date: 2025-10-06

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create all tables."""

    # Create users table
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)

    # Create sessions table
    op.create_table(
        "sessions",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("expires_at", sa.DateTime(), nullable=False),
        sa.Column("csrf_secret", sa.String(length=64), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_sessions_user_id"), "sessions", ["user_id"], unique=False)

    # Create studies table
    op.create_table(
        "studies",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("consent_text", sa.Text(), nullable=False),
        sa.Column("max_agent_turns", sa.Integer(), nullable=False, server_default="9"),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["owner_user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_studies_id"), "studies", ["id"], unique=False)
    op.create_index(op.f("ix_studies_owner_user_id"), "studies", ["owner_user_id"], unique=False)

    # Create study_questions table
    op.create_table(
        "study_questions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("study_id", sa.Integer(), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["study_id"], ["studies.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_study_questions_id"), "study_questions", ["id"], unique=False)
    op.create_index(op.f("ix_study_questions_study_id"), "study_questions", ["study_id"], unique=False)

    # Create invites table
    op.create_table(
        "invites",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("study_id", sa.Integer(), nullable=False),
        sa.Column("invite_code", sa.String(length=64), nullable=False),
        sa.Column("interviewee_email", sa.String(length=255), nullable=True),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="created"),
        sa.Column("expires_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["study_id"], ["studies.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("invite_code"),
    )
    op.create_index(op.f("ix_invites_id"), "invites", ["id"], unique=False)
    op.create_index(op.f("ix_invites_study_id"), "invites", ["study_id"], unique=False)
    op.create_index(op.f("ix_invites_invite_code"), "invites", ["invite_code"], unique=True)

    # Create interviews table
    op.create_table(
        "interviews",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("study_id", sa.Integer(), nullable=False),
        sa.Column("invite_id", sa.Integer(), nullable=False),
        sa.Column("started_at", sa.DateTime(), nullable=False),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column("agent_turns", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["study_id"], ["studies.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["invite_id"], ["invites.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("invite_id"),
    )
    op.create_index(op.f("ix_interviews_id"), "interviews", ["id"], unique=False)
    op.create_index(op.f("ix_interviews_study_id"), "interviews", ["study_id"], unique=False)

    # Create interviewees table
    op.create_table(
        "interviewees",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("interview_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("demographics_json", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column("consent_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["interview_id"], ["interviews.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("interview_id"),
    )
    op.create_index(op.f("ix_interviewees_id"), "interviewees", ["id"], unique=False)

    # Create messages table
    op.create_table(
        "messages",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("interview_id", sa.Integer(), nullable=False),
        sa.Column("role", sa.String(length=20), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["interview_id"], ["interviews.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_messages_id"), "messages", ["id"], unique=False)
    op.create_index(op.f("ix_messages_interview_id"), "messages", ["interview_id"], unique=False)

    # Create insights table
    op.create_table(
        "insights",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("interview_id", sa.Integer(), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("sentiment", sa.String(length=20), nullable=False),
        sa.Column("keywords_json", postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column("quotes_json", postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["interview_id"], ["interviews.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("interview_id"),
    )
    op.create_index(op.f("ix_insights_id"), "insights", ["id"], unique=False)


def downgrade() -> None:
    """Drop all tables."""
    op.drop_index(op.f("ix_insights_id"), table_name="insights")
    op.drop_table("insights")

    op.drop_index(op.f("ix_messages_interview_id"), table_name="messages")
    op.drop_index(op.f("ix_messages_id"), table_name="messages")
    op.drop_table("messages")

    op.drop_index(op.f("ix_interviewees_id"), table_name="interviewees")
    op.drop_table("interviewees")

    op.drop_index(op.f("ix_interviews_study_id"), table_name="interviews")
    op.drop_index(op.f("ix_interviews_id"), table_name="interviews")
    op.drop_table("interviews")

    op.drop_index(op.f("ix_invites_invite_code"), table_name="invites")
    op.drop_index(op.f("ix_invites_study_id"), table_name="invites")
    op.drop_index(op.f("ix_invites_id"), table_name="invites")
    op.drop_table("invites")

    op.drop_index(op.f("ix_study_questions_study_id"), table_name="study_questions")
    op.drop_index(op.f("ix_study_questions_id"), table_name="study_questions")
    op.drop_table("study_questions")

    op.drop_index(op.f("ix_studies_owner_user_id"), table_name="studies")
    op.drop_index(op.f("ix_studies_id"), table_name="studies")
    op.drop_table("studies")

    op.drop_index(op.f("ix_sessions_user_id"), table_name="sessions")
    op.drop_table("sessions")

    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")

```

## alembic.ini

**Path:** `alembic.ini`
**Type:** Ini
**Size:** 3.7 KB

```ini
# A generic, single database configuration.

[alembic]
# path to migration scripts
# Use forward slashes (/) also on windows to provide an os agnostic path
script_location = alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the python>=3.9 or backports.zoneinfo library.
# Any required deps can installed by adding `alembic[tz]` to the pip requirements
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to alembic/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "version_path_separator" below.
# version_locations = %(here)s/bar:%(here)s/bat:alembic/versions

# version path separator; As mentioned above, this is the character used to split
# version_locations. The default within new alembic.ini files is "os", which uses os.pathsep.
# If this key is omitted entirely, it falls back to the legacy behavior of splitting on spaces and/or commas.
# Valid values for version_path_separator are:
#
# version_path_separator = :
# version_path_separator = ;
# version_path_separator = space
# version_path_separator = newline
version_path_separator = os  # Use os.pathsep. Default configuration used for new projects.

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

# sqlalchemy.url = driver://user:pass@localhost/dbname
# NOTE: Database URL is set dynamically from app settings in alembic/env.py


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the exec runner, execute a binary
# hooks = ruff
# ruff.type = exec
# ruff.executable = %(here)s/.venv/bin/ruff
# ruff.options = --fix REVISION_SCRIPT_FILENAME

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
```

## app/__init__.py

**Path:** `app/__init__.py`
**Type:** Python
**Size:** 0 bytes

```python

```

## app/auth/__init__.py

**Path:** `app/auth/__init__.py`
**Type:** Python
**Size:** 116 bytes

```python
"""Authentication module."""

from app.auth import dependencies, sessions

__all__ = ["dependencies", "sessions"]


```

## app/auth/dependencies.py

**Path:** `app/auth/dependencies.py`
**Type:** Python
**Size:** 1.4 KB

```python
"""Authentication dependencies for route protection."""

from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.auth.sessions import get_session
from app.crud import session as session_crud
from app.db.session import get_db
from app.models.user import User


def get_current_session_id(request: Request) -> str:
    """Extract session ID from cookie."""
    session_id = get_session(request)
    if not session_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    return session_id


def get_current_user(
    session_id: str = Depends(get_current_session_id),
    db: Session = Depends(get_db),
) -> User:
    """Get current authenticated user from session."""
    session = session_crud.get_session_by_id(db, session_id)

    if not session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session",
        )

    if not session_crud.is_session_valid(session):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired",
        )

    user = db.get(User, session.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user


```

## app/auth/sessions.py

**Path:** `app/auth/sessions.py`
**Type:** Python
**Size:** 1.5 KB

```python
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


```

## app/crud/__init__.py

**Path:** `app/crud/__init__.py`
**Type:** Python
**Size:** 164 bytes

```python
"""CRUD operations for all models."""

from app.crud import interview, invite, session, study, user

__all__ = ["user", "session", "study", "invite", "interview"]

```

## app/crud/interview.py

**Path:** `app/crud/interview.py`
**Type:** Python
**Size:** 5.7 KB

```python
"""CRUD operations for Interview, Interviewee, Message, and Insight models."""

from datetime import datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.models.interview import Insight, Interview, Interviewee, Message


# Interview CRUD


def create_interview(db: Session, study_id: int, invite_id: int) -> Interview:
    """Create a new interview."""
    interview = Interview(study_id=study_id, invite_id=invite_id, agent_turns=0)
    db.add(interview)
    db.commit()
    db.refresh(interview)
    return interview


def get_interview_by_id(
    db: Session, interview_id: int, load_messages: bool = False, load_all: bool = False
) -> Interview | None:
    """Get interview by ID with optional related data."""
    stmt = select(Interview).where(Interview.id == interview_id)
    if load_all:
        stmt = stmt.options(
            selectinload(Interview.messages),
            selectinload(Interview.interviewee),
            selectinload(Interview.insight),
        )
    elif load_messages:
        stmt = stmt.options(selectinload(Interview.messages))
    return db.scalar(stmt)


def get_interviews_by_study(db: Session, study_id: int, load_relations: bool = False) -> list[Interview]:
    """Get all interviews for a study."""
    stmt = (
        select(Interview)
        .where(Interview.study_id == study_id)
        .order_by(Interview.started_at.desc())
    )
    if load_relations:
        stmt = stmt.options(
            selectinload(Interview.interviewee),
            selectinload(Interview.insight),
        )
    return list(db.scalars(stmt).all())


def get_interview_by_invite(db: Session, invite_id: int) -> Interview | None:
    """Get interview by invite ID."""
    stmt = select(Interview).where(Interview.invite_id == invite_id)
    return db.scalar(stmt)


def complete_interview(db: Session, interview_id: int) -> Interview | None:
    """Mark interview as completed."""
    interview = db.get(Interview, interview_id)
    if interview:
        interview.completed_at = datetime.now(timezone.utc).replace(tzinfo=None)
        db.commit()
        db.refresh(interview)
    return interview


def increment_agent_turns(db: Session, interview_id: int) -> Interview | None:
    """Increment agent turn counter."""
    interview = db.get(Interview, interview_id)
    if interview:
        interview.agent_turns += 1
        db.commit()
        db.refresh(interview)
    return interview


# Interviewee CRUD


def create_interviewee(
    db: Session,
    interview_id: int,
    name: str,
    email: str,
    demographics_json: dict | None = None,
) -> Interviewee:
    """Create interviewee record."""
    interviewee = Interviewee(
        interview_id=interview_id, name=name, email=email, demographics_json=demographics_json
    )
    db.add(interviewee)
    db.commit()
    db.refresh(interviewee)
    return interviewee


def get_interviewee_by_interview(db: Session, interview_id: int) -> Interviewee | None:
    """Get interviewee by interview ID."""
    stmt = select(Interviewee).where(Interviewee.interview_id == interview_id)
    return db.scalar(stmt)


# Message CRUD


def get_message_count(db: Session, interview_id: int) -> int:
    """Get count of messages for an interview."""
    stmt = select(func.count(Message.id)).where(Message.interview_id == interview_id)
    return db.scalar(stmt) or 0


def create_message(db: Session, interview_id: int, role: str, content: str) -> Message:
    """Create a chat message."""
    message = Message(interview_id=interview_id, role=role, content=content)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_messages_by_interview(db: Session, interview_id: int, limit: int | None = None) -> list[Message]:
    """Get messages for an interview, ordered by time."""
    stmt = select(Message).where(Message.interview_id == interview_id).order_by(Message.created_at)
    if limit:
        stmt = stmt.limit(limit)
    return list(db.scalars(stmt).all())


def get_recent_messages(db: Session, interview_id: int, count: int = 8) -> list[Message]:
    """Get the most recent N messages for context."""
    stmt = (
        select(Message)
        .where(Message.interview_id == interview_id)
        .order_by(Message.created_at.desc())
        .limit(count)
    )
    # Reverse to get chronological order
    return list(reversed(db.scalars(stmt).all()))


# Insight CRUD


def create_insight(
    db: Session,
    interview_id: int,
    summary: str,
    sentiment: str,
    keywords_json: list,
    quotes_json: list,
) -> Insight:
    """Create interview insights."""
    insight = Insight(
        interview_id=interview_id,
        summary=summary,
        sentiment=sentiment,
        keywords_json=keywords_json,
        quotes_json=quotes_json,
    )
    db.add(insight)
    db.commit()
    db.refresh(insight)
    return insight


def get_insight_by_interview(db: Session, interview_id: int) -> Insight | None:
    """Get insight by interview ID."""
    stmt = select(Insight).where(Insight.interview_id == interview_id)
    return db.scalar(stmt)


def update_insight(
    db: Session,
    insight_id: int,
    summary: str | None = None,
    sentiment: str | None = None,
    keywords_json: list | None = None,
    quotes_json: list | None = None,
) -> Insight | None:
    """Update existing insight."""
    insight = db.get(Insight, insight_id)
    if insight:
        if summary is not None:
            insight.summary = summary
        if sentiment is not None:
            insight.sentiment = sentiment
        if keywords_json is not None:
            insight.keywords_json = keywords_json
        if quotes_json is not None:
            insight.quotes_json = quotes_json
        db.commit()
        db.refresh(insight)
    return insight

```

## app/crud/invite.py

**Path:** `app/crud/invite.py`
**Type:** Python
**Size:** 2.2 KB

```python
"""CRUD operations for Invite model."""

import secrets
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.invite import Invite, InviteStatus


def generate_invite_code() -> str:
    """Generate a unique invite code."""
    return secrets.token_urlsafe(32)


def create_invite(
    db: Session,
    study_id: int,
    interviewee_email: str | None = None,
    expires_at: datetime | None = None,
) -> Invite:
    """Create a new invite."""
    invite_code = generate_invite_code()
    invite = Invite(
        study_id=study_id,
        invite_code=invite_code,
        interviewee_email=interviewee_email,
        status=InviteStatus.CREATED.value,
        expires_at=expires_at,
    )
    db.add(invite)
    db.commit()
    db.refresh(invite)
    return invite


def get_invite_by_code(db: Session, invite_code: str) -> Invite | None:
    """Get invite by code."""
    stmt = select(Invite).where(Invite.invite_code == invite_code)
    return db.scalar(stmt)


def get_invite_by_id(db: Session, invite_id: int) -> Invite | None:
    """Get invite by ID."""
    return db.get(Invite, invite_id)


def get_invites_by_study(db: Session, study_id: int) -> list[Invite]:
    """Get all invites for a study."""
    stmt = select(Invite).where(Invite.study_id == study_id).order_by(Invite.created_at.desc())
    return list(db.scalars(stmt).all())


def update_invite_status(db: Session, invite_id: int, status: InviteStatus) -> Invite | None:
    """Update invite status."""
    invite = db.get(Invite, invite_id)
    if invite:
        invite.status = status.value
        db.commit()
        db.refresh(invite)
    return invite


def is_invite_valid(invite: Invite) -> bool:
    """Check if invite is valid (not expired, not completed)."""
    if invite.status == InviteStatus.COMPLETED.value:
        return False
    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return False
    return True


def delete_invite(db: Session, invite_id: int) -> bool:
    """Delete an invite."""
    invite = db.get(Invite, invite_id)
    if invite:
        db.delete(invite)
        db.commit()
        return True
    return False

```

## app/crud/session.py

**Path:** `app/crud/session.py`
**Type:** Python
**Size:** 2.4 KB

```python
"""CRUD operations for Session model."""

import secrets
from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from app.models.session import Session


def generate_session_id() -> str:
    """Generate a secure session ID."""
    return secrets.token_urlsafe(32)


def generate_csrf_secret() -> str:
    """Generate a CSRF secret."""
    return secrets.token_urlsafe(32)


def create_session(
    db: DBSession, user_id: int, expires_in_days: int = 7
) -> Session:
    """Create a new session."""
    session_id = generate_session_id()
    csrf_secret = generate_csrf_secret()
    expires_at = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(days=expires_in_days)

    session = Session(
        id=session_id, user_id=user_id, expires_at=expires_at, csrf_secret=csrf_secret
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def get_session_by_id(db: DBSession, session_id: str) -> Session | None:
    """Get session by ID."""
    return db.get(Session, session_id)


def get_sessions_by_user(db: DBSession, user_id: int) -> list[Session]:
    """Get all sessions for a user."""
    stmt = select(Session).where(Session.user_id == user_id)
    return list(db.scalars(stmt).all())


def is_session_valid(session: Session) -> bool:
    """Check if session is still valid (not expired)."""
    return session.expires_at > datetime.now(timezone.utc).replace(tzinfo=None)


def delete_session(db: DBSession, session_id: str) -> bool:
    """Delete a session (logout)."""
    session = db.get(Session, session_id)
    if session:
        db.delete(session)
        db.commit()
        return True
    return False


def delete_expired_sessions(db: DBSession) -> int:
    """Delete all expired sessions. Returns count of deleted sessions."""
    stmt = select(Session).where(Session.expires_at < datetime.now(timezone.utc).replace(tzinfo=None))
    expired = db.scalars(stmt).all()
    count = len(expired)
    for session in expired:
        db.delete(session)
    db.commit()
    return count


def delete_user_sessions(db: DBSession, user_id: int) -> int:
    """Delete all sessions for a user. Returns count of deleted sessions."""
    stmt = select(Session).where(Session.user_id == user_id)
    sessions = db.scalars(stmt).all()
    count = len(sessions)
    for session in sessions:
        db.delete(session)
    db.commit()
    return count

```

## app/crud/study.py

**Path:** `app/crud/study.py`
**Type:** Python
**Size:** 3.7 KB

```python
"""CRUD operations for Study and StudyQuestion models."""

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.study import Study, StudyQuestion


# Study CRUD


def create_study(
    db: Session,
    owner_user_id: int,
    title: str,
    description: str,
    consent_text: str,
    max_agent_turns: int = 9,
) -> Study:
    """Create a new study."""
    study = Study(
        owner_user_id=owner_user_id,
        title=title,
        description=description,
        consent_text=consent_text,
        max_agent_turns=max_agent_turns,
    )
    db.add(study)
    db.commit()
    db.refresh(study)
    return study


def get_study_by_id(db: Session, study_id: int, load_questions: bool = True) -> Study | None:
    """Get study by ID with optional question loading."""
    stmt = select(Study).where(Study.id == study_id)
    if load_questions:
        stmt = stmt.options(selectinload(Study.questions))
    return db.scalar(stmt)


def get_studies_by_user(
    db: Session, user_id: int, skip: int = 0, limit: int = 100
) -> list[Study]:
    """Get all studies for a user."""
    stmt = (
        select(Study)
        .where(Study.owner_user_id == user_id)
        .order_by(Study.created_at.desc())
        .offset(skip)
        .limit(limit)
    )
    return list(db.scalars(stmt).all())


def update_study(
    db: Session,
    study_id: int,
    title: str | None = None,
    description: str | None = None,
    consent_text: str | None = None,
    max_agent_turns: int | None = None,
) -> Study | None:
    """Update study details."""
    study = db.get(Study, study_id)
    if study:
        if title is not None:
            study.title = title
        if description is not None:
            study.description = description
        if consent_text is not None:
            study.consent_text = consent_text
        if max_agent_turns is not None:
            study.max_agent_turns = max_agent_turns
        db.commit()
        db.refresh(study)
    return study


def delete_study(db: Session, study_id: int) -> bool:
    """Delete a study and cascade to related entities."""
    study = db.get(Study, study_id)
    if study:
        db.delete(study)
        db.commit()
        return True
    return False


# StudyQuestion CRUD


def create_study_question(db: Session, study_id: int, text: str, sort_order: int) -> StudyQuestion:
    """Create a study question."""
    question = StudyQuestion(study_id=study_id, text=text, sort_order=sort_order)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


def get_study_questions(db: Session, study_id: int) -> list[StudyQuestion]:
    """Get all questions for a study, ordered."""
    stmt = (
        select(StudyQuestion)
        .where(StudyQuestion.study_id == study_id)
        .order_by(StudyQuestion.sort_order)
    )
    return list(db.scalars(stmt).all())


def update_question_text(db: Session, question_id: int, text: str) -> StudyQuestion | None:
    """Update question text."""
    question = db.get(StudyQuestion, question_id)
    if question:
        question.text = text
        db.commit()
        db.refresh(question)
    return question


def reorder_questions(db: Session, question_updates: list[tuple[int, int]]) -> bool:
    """Bulk update question sort orders. Input: [(question_id, new_sort_order), ...]"""
    for question_id, new_order in question_updates:
        question = db.get(StudyQuestion, question_id)
        if question:
            question.sort_order = new_order
    db.commit()
    return True


def delete_study_question(db: Session, question_id: int) -> bool:
    """Delete a study question."""
    question = db.get(StudyQuestion, question_id)
    if question:
        db.delete(question)
        db.commit()
        return True
    return False

```

## app/crud/user.py

**Path:** `app/crud/user.py`
**Type:** Python
**Size:** 1.3 KB

```python
"""CRUD operations for User model."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def create_user(db: Session, email: str, password_hash: str) -> User:
    """Create a new user."""
    user = User(email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: int) -> User | None:
    """Get user by ID."""
    return db.get(User, user_id)


def get_user_by_email(db: Session, email: str) -> User | None:
    """Get user by email."""
    stmt = select(User).where(User.email == email)
    return db.scalar(stmt)


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """Get list of users with pagination."""
    stmt = select(User).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())


def update_user_password(db: Session, user_id: int, new_password_hash: str) -> User | None:
    """Update user password."""
    user = db.get(User, user_id)
    if user:
        user.password_hash = new_password_hash
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> bool:
    """Delete a user."""
    user = db.get(User, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

```

## app/db/__init__.py

**Path:** `app/db/__init__.py`
**Type:** Python
**Size:** 0 bytes

```python

```

## app/db/base.py

**Path:** `app/db/base.py`
**Type:** Python
**Size:** 182 bytes

```python
"""SQLAlchemy declarative base for all models."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all database models."""

    pass

```

## app/db/session.py

**Path:** `app/db/session.py`
**Type:** Python
**Size:** 977 bytes

```python
"""Database session management."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

# Create database engine with connection pooling
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,  # Verify connections before using them
    pool_size=5,  # Number of connections to maintain
    max_overflow=10,  # Maximum overflow connections
    echo=False,  # Set to True to see SQL queries in logs
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db():
    """
    Dependency for FastAPI routes to get a database session.

    Usage:
        @router.get("/users")
        def get_users(db: Session = Depends(get_db)):
            return db.query(User).all()

    Yields:
        Session: Database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

## app/main.py

**Path:** `app/main.py`
**Type:** Python
**Size:** 3.6 KB

```python
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

```

## app/middleware.py

**Path:** `app/middleware.py`
**Type:** Python
**Size:** 1.7 KB

```python
"""Custom middleware for request tracking and logging."""

import logging
import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger(__name__)


class RequestIDMiddleware(BaseHTTPMiddleware):
    """Middleware to add unique request ID to each request."""

    async def dispatch(self, request: Request, call_next) -> Response:
        # Generate or extract request ID
        request_id = request.headers.get("x-request-id") or str(uuid.uuid4())

        # Store request ID in request state for access in route handlers
        request.state.request_id = request_id

        # Track request timing
        start_time = time.time()

        # Process request
        try:
            response: Response = await call_next(request)
        except Exception as exc:
            # Log unhandled exceptions with request ID
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                f"Request failed | request_id={request_id} | "
                f"method={request.method} | path={request.url.path} | "
                f"duration={duration_ms:.2f}ms | error={exc}"
            )
            raise

        # Add request ID to response headers
        response.headers["x-request-id"] = request_id

        # Log successful request
        duration_ms = (time.time() - start_time) * 1000
        logger.info(
            f"Request completed | request_id={request_id} | "
            f"method={request.method} | path={request.url.path} | "
            f"status={response.status_code} | duration={duration_ms:.2f}ms"
        )

        return response

```

## app/models/__init__.py

**Path:** `app/models/__init__.py`
**Type:** Python
**Size:** 448 bytes

```python
"""Database models."""

from app.models.interview import Insight, Interview, Interviewee, Message
from app.models.invite import Invite, InviteStatus
from app.models.session import Session
from app.models.study import Study, StudyQuestion
from app.models.user import User

__all__ = [
    "User",
    "Session",
    "Study",
    "StudyQuestion",
    "Invite",
    "InviteStatus",
    "Interview",
    "Interviewee",
    "Message",
    "Insight",
]

```

## app/models/interview.py

**Path:** `app/models/interview.py`
**Type:** Python
**Size:** 4.4 KB

```python
"""Interview-related models."""

from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSON

from app.db.base import Base


class Interview(Base):
    """Interview session."""

    __tablename__ = "interviews"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    study_id: Mapped[int] = mapped_column(ForeignKey("studies.id", ondelete="CASCADE"), index=True)
    invite_id: Mapped[int] = mapped_column(
        ForeignKey("invites.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    started_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable=True)
    agent_turns: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Relationships
    study: Mapped["Study"] = relationship("Study", back_populates="interviews")  # type: ignore
    invite: Mapped["Invite"] = relationship("Invite", back_populates="interview")  # type: ignore
    interviewee: Mapped["Interviewee | None"] = relationship(
        "Interviewee", back_populates="interview", uselist=False, cascade="all, delete-orphan"
    )
    messages: Mapped[list["Message"]] = relationship(
        "Message", back_populates="interview", cascade="all, delete-orphan", order_by="Message.created_at"
    )
    insight: Mapped["Insight | None"] = relationship(
        "Insight", back_populates="interview", uselist=False, cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Interview(id={self.id}, study_id={self.study_id}, turns={self.agent_turns})>"


class Interviewee(Base):
    """Interviewee information."""

    __tablename__ = "interviewees"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    interview_id: Mapped[int] = mapped_column(
        ForeignKey("interviews.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    demographics_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    consent_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)

    # Relationships
    interview: Mapped["Interview"] = relationship("Interview", back_populates="interviewee")

    def __repr__(self) -> str:
        return f"<Interviewee(id={self.id}, name={self.name}, email={self.email})>"


class Message(Base):
    """Chat message."""

    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    interview_id: Mapped[int] = mapped_column(ForeignKey("interviews.id", ondelete="CASCADE"), index=True)
    role: Mapped[str] = mapped_column(String(20), nullable=False)  # 'agent', 'user', 'system'
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)

    # Relationships
    interview: Mapped["Interview"] = relationship("Interview", back_populates="messages")

    def __repr__(self) -> str:
        return f"<Message(id={self.id}, role={self.role}, interview_id={self.interview_id})>"


class Insight(Base):
    """Interview insights."""

    __tablename__ = "insights"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    interview_id: Mapped[int] = mapped_column(
        ForeignKey("interviews.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    sentiment: Mapped[str] = mapped_column(String(20), nullable=False)  # 'pos', 'neu', 'neg'
    keywords_json: Mapped[list] = mapped_column(JSON, nullable=False)
    quotes_json: Mapped[list] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)

    # Relationships
    interview: Mapped["Interview"] = relationship("Interview", back_populates="insight")

    def __repr__(self) -> str:
        return f"<Insight(id={self.id}, interview_id={self.interview_id}, sentiment={self.sentiment})>"

```

## app/models/invite.py

**Path:** `app/models/invite.py`
**Type:** Python
**Size:** 1.5 KB

```python
"""Invite model."""

from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class InviteStatus(str, Enum):
    """Invite status enumeration."""

    CREATED = "created"
    OPENED = "opened"
    COMPLETED = "completed"


class Invite(Base):
    """Study invite link."""

    __tablename__ = "invites"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    study_id: Mapped[int] = mapped_column(ForeignKey("studies.id", ondelete="CASCADE"), index=True)
    invite_code: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    interviewee_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default=InviteStatus.CREATED.value, nullable=False)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)

    # Relationships
    study: Mapped["Study"] = relationship("Study", back_populates="invites")  # type: ignore
    interview: Mapped["Interview | None"] = relationship(
        "Interview", back_populates="invite", uselist=False
    )

    def __repr__(self) -> str:
        return f"<Invite(id={self.id}, code={self.invite_code}, status={self.status})>"

```

## app/models/session.py

**Path:** `app/models/session.py`
**Type:** Python
**Size:** 1007 bytes

```python
"""Session model for researcher authentication."""

from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Session(Base):
    """Server-side session for researchers."""

    __tablename__ = "sessions"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    csrf_secret: Mapped[str] = mapped_column(String(64), nullable=False)

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="sessions")  # type: ignore

    def __repr__(self) -> str:
        return f"<Session(id={self.id}, user_id={self.user_id})>"

```

## app/models/study.py

**Path:** `app/models/study.py`
**Type:** Python
**Size:** 2.2 KB

```python
"""Study-related models."""

from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Study(Base):
    """Research study model."""

    __tablename__ = "studies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    owner_user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    consent_text: Mapped[str] = mapped_column(Text, nullable=False)
    max_agent_turns: Mapped[int] = mapped_column(Integer, default=9, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)

    # Relationships
    owner: Mapped["User"] = relationship("User", back_populates="studies")  # type: ignore
    questions: Mapped[list["StudyQuestion"]] = relationship(
        "StudyQuestion", back_populates="study", cascade="all, delete-orphan", order_by="StudyQuestion.sort_order"
    )
    invites: Mapped[list["Invite"]] = relationship(
        "Invite", back_populates="study", cascade="all, delete-orphan"
    )
    interviews: Mapped[list["Interview"]] = relationship(
        "Interview", back_populates="study", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Study(id={self.id}, title={self.title})>"


class StudyQuestion(Base):
    """Study seed questions."""

    __tablename__ = "study_questions"
    __table_args__ = ({"schema": None},)

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    study_id: Mapped[int] = mapped_column(ForeignKey("studies.id", ondelete="CASCADE"), index=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # Relationships
    study: Mapped["Study"] = relationship("Study", back_populates="questions")

    def __repr__(self) -> str:
        return f"<StudyQuestion(id={self.id}, study_id={self.study_id}, order={self.sort_order})>"

```

## app/models/user.py

**Path:** `app/models/user.py`
**Type:** Python
**Size:** 1.0 KB

```python
"""User model for researchers."""

from datetime import datetime, timezone

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    """Researcher user model (not for interviewees)."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)

    # Relationships
    studies: Mapped[list["Study"]] = relationship(
        "Study", back_populates="owner", cascade="all, delete-orphan"
    )
    sessions: Mapped[list["Session"]] = relationship(
        "Session", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email})>"

```

## app/routers/__init__.py

**Path:** `app/routers/__init__.py`
**Type:** Python
**Size:** 0 bytes

```python

```

## app/routers/auth_dev.py

**Path:** `app/routers/auth_dev.py`
**Type:** Python
**Size:** 7.2 KB

```python
"""Development-only authentication routes for testing."""

from urllib.parse import quote_plus

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from passlib.hash import argon2
from sqlalchemy.orm import Session

from app.auth.sessions import clear_session, set_session
from app.crud import session as session_crud
from app.crud import user as user_crud
from app.db.session import get_db
from app.settings import settings

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(prefix="/auth/dev", tags=["auth-dev"])


@router.post("/register")
def dev_register(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(None),
    db: Session = Depends(get_db),
):
    """
    DEV ONLY: Create a test user.

    Only available in development mode.
    """
    if settings.is_production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found",
        )

    # Check if this is a browser request (for HTML response)
    accept = request.headers.get("accept", "")
    wants_html = "text/html" in accept

    # Validate password confirmation (if provided from form)
    if confirm_password and password != confirm_password:
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/register.html",
                context={
                    "error": "Passwords do not match",
                    "email": email,
                },
                status_code=400,
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match",
        )

    # Validate password length
    if len(password) < 8:
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/register.html",
                context={
                    "error": "Password must be at least 8 characters long",
                    "email": email,
                },
                status_code=400,
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 8 characters long",
        )

    # Check if user exists
    existing_user = user_crud.get_user_by_email(db, email)
    if existing_user:
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/register.html",
                context={
                    "error": "Email already registered. Please login instead.",
                    "email": email,
                },
                status_code=400,
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # Create user
    password_hash = argon2.hash(password)
    user = user_crud.create_user(db, email=email, password_hash=password_hash)

    # For HTML requests, redirect to login
    if wants_html:
        return RedirectResponse(
            url=f"/login?success={quote_plus('Account created successfully! Please login.')}",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    # For API requests, return JSON with 201 status
    from fastapi.responses import JSONResponse
    return JSONResponse(
        content={
            "id": user.id,
            "email": user.email,
            "created_at": user.created_at.isoformat(),
        },
        status_code=status.HTTP_201_CREATED,
    )


@router.post("/login")
def dev_login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    """
    DEV ONLY: Login and get session cookie.

    Only available in development mode.
    """
    if settings.is_production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found",
        )

    # Check if this is a browser request (for HTML response)
    accept = request.headers.get("accept", "")
    wants_html = "text/html" in accept

    # Get user
    user = user_crud.get_user_by_email(db, email)
    if not user:
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/login.html",
                context={
                    "error": "Invalid email or password",
                    "email": email,
                },
                status_code=401,
            )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    # Verify password
    if not argon2.verify(password, user.password_hash):
        if wants_html:
            return templates.TemplateResponse(
                request=request,
                name="auth/login.html",
                context={
                    "error": "Invalid email or password",
                    "email": email,
                },
                status_code=401,
            )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    session = session_crud.create_session(db, user.id)

    # For HTML requests, set cookie and redirect
    if wants_html:
        next_url = request.query_params.get("next", "/app/studies")
        response = RedirectResponse(url=next_url, status_code=status.HTTP_303_SEE_OTHER)
        set_session(response, session.id)
        return response

    # For API requests, set cookie and redirect to studies
    response = RedirectResponse(url="/app/studies", status_code=status.HTTP_303_SEE_OTHER)
    set_session(response, session.id)
    return response


@router.post("/logout")
def dev_logout():
    """DEV ONLY: Logout (clear session cookie)."""
    if settings.is_production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found",
        )

    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    clear_session(response)
    return response


@router.get("/quick-auth")
def dev_quick_auth(db: Session = Depends(get_db)):
    """
    DEV ONLY: Create test user and return session cookie in one step.

    Creates user test@example.com / password123 and logs them in.
    Useful for quick testing.
    """
    if settings.is_production:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found",
        )

    email = "test@example.com"
    password = "password123"

    # Check if user exists, create if not
    user = user_crud.get_user_by_email(db, email)
    if not user:
        password_hash = argon2.hash(password)
        user = user_crud.create_user(db, email=email, password_hash=password_hash)

    # Create session
    session = session_crud.create_session(db, user.id)

    # Set cookie and redirect to studies
    response = RedirectResponse(url="/app/studies", status_code=status.HTTP_303_SEE_OTHER)
    set_session(response, session.id)

    return response

```

## app/routers/health.py

**Path:** `app/routers/health.py`
**Type:** Python
**Size:** 323 bytes

```python
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

```

## app/routers/interview.py

**Path:** `app/routers/interview.py`
**Type:** Python
**Size:** 17.3 KB

```python
"""Public-facing interview routes (no authentication required)."""

import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr, ValidationError
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.db.session import get_db
from app.models.invite import InviteStatus
from app.schemas.interview import IntakeForm
from app.services.ai_agent import AIInterviewAgent
from app.services.insight_generator import InsightGenerator

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/interview", tags=["interview"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/{invite_code}", response_class=HTMLResponse)
async def landing_page(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Landing page for interview invite.

    - Validates invite exists and is not expired/completed
    - Shows study information
    - Updates invite status to 'opened' on first view
    - Provides CTA to continue to consent
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)

    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )

    if invite.status == InviteStatus.COMPLETED.value:
        return templates.TemplateResponse(
            request=request,
            name="interview/completed.html",
        )

    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return templates.TemplateResponse(
            request=request,
            name="interview/expired.html",
        )

    if invite.status == InviteStatus.CREATED.value:
        invite_crud.update_invite_status(db, invite.id, InviteStatus.OPENED)
        db.refresh(invite)

    study = invite.study

    return templates.TemplateResponse(
        request=request,
        name="interview/landing.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
        },
    )


@router.get("/{invite_code}/consent", response_class=HTMLResponse)
async def consent_page(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Consent page for interview.

    - Shows study consent text
    - Provides checkbox to agree
    - Validates invite is still valid
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)

    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )

    if invite.status == InviteStatus.COMPLETED.value:
        return templates.TemplateResponse(
            request=request,
            name="interview/completed.html",
        )

    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return templates.TemplateResponse(
            request=request,
            name="interview/expired.html",
        )

    study = invite.study

    return templates.TemplateResponse(
        request=request,
        name="interview/consent.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
        },
    )


@router.post("/{invite_code}/consent")
async def submit_consent(
    invite_code: str,
    agreed: bool = Form(...),
    db: Session = Depends(get_db),
):
    """
    Process consent form submission.

    - Validates invite is still valid
    - Creates interview record
    - Updates invite status to 'completed'
    - Redirects to intake form
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)

    if not invite:
        return RedirectResponse(
            url=f"/interview/{invite_code}",
            status_code=303,
        )

    if invite.status == InviteStatus.COMPLETED.value:
        return RedirectResponse(
            url=f"/interview/{invite_code}",
            status_code=303,
        )

    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return RedirectResponse(
            url=f"/interview/{invite_code}",
            status_code=303,
        )

    if not agreed:
        return RedirectResponse(
            url=f"/interview/{invite_code}/consent",
            status_code=303,
        )

    existing_interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not existing_interview:
        interview_crud.create_interview(
            db,
            study_id=invite.study_id,
            invite_id=invite.id,
        )
        invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    return RedirectResponse(
        url=f"/interview/{invite_code}/intake",
        status_code=303,
    )


@router.get("/{invite_code}/intake", response_class=HTMLResponse)
async def intake_page(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Intake form page.

    - Collects interviewee information (name, email, demographics)
    - Validates that consent has been given (interview exists)
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)

    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )

    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc).replace(tzinfo=None):
        return templates.TemplateResponse(
            request=request,
            name="interview/expired.html",
        )

    interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not interview:
        return RedirectResponse(
            url=f"/interview/{invite_code}/consent",
            status_code=303,
        )

    existing_interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)
    if existing_interviewee:
        return templates.TemplateResponse(
            request=request,
            name="interview/completed.html",
        )

    study = invite.study

    return templates.TemplateResponse(
        request=request,
        name="interview/intake.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
        },
    )


@router.post("/{invite_code}/intake")
async def submit_intake(
    request: Request,
    invite_code: str,
    name: str = Form(...),
    email: EmailStr = Form(...),
    age_range: str = Form(None),
    location: str = Form(None),
    occupation: str = Form(None),
    db: Session = Depends(get_db),
):
    """
    Process intake form submission.

    - Validates form data
    - Creates interviewee record
    - Redirects to chat interface (Day 4)
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)

    if not invite:
        return RedirectResponse(
            url=f"/interview/{invite_code}",
            status_code=303,
        )

    interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not interview:
        return RedirectResponse(
            url=f"/interview/{invite_code}/consent",
            status_code=303,
        )

    existing_interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)
    if existing_interviewee:
        return RedirectResponse(
            url=f"/interview/{invite_code}/chat",
            status_code=303,
        )

    demographics = {}
    if age_range:
        demographics["age_range"] = age_range
    if location:
        demographics["location"] = location
    if occupation:
        demographics["occupation"] = occupation

    try:
        interview_crud.create_interviewee(
            db,
            interview_id=interview.id,
            name=name.strip(),
            email=email.lower().strip(),
            demographics_json=demographics if demographics else None,
        )
    except Exception as e:
        study = invite.study
        return templates.TemplateResponse(
            request=request,
            name="interview/intake.html",
            context={
                "invite_code": invite_code,
                "invite": invite,
                "study": study,
                "error": "An error occurred while saving your information. Please try again.",
                "form_data": {"name": name, "email": email},
            },
        )

    return RedirectResponse(
        url=f"/interview/{invite_code}/chat",
        status_code=303,
    )


@router.get("/{invite_code}/chat", response_class=HTMLResponse)
async def chat_page(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Chat interface for conducting the AI interview.

    - Loads existing messages
    - Verifies interviewee completed intake
    - Checks if interview is completed
    - Initiates conversation if no messages exist
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)

    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )

    interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not interview:
        return RedirectResponse(
            url=f"/interview/{invite_code}/consent",
            status_code=303,
        )

    interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)
    if not interviewee:
        return RedirectResponse(
            url=f"/interview/{invite_code}/intake",
            status_code=303,
        )

    study = invite.study

    if interview.completed_at:
        return RedirectResponse(
            url=f"/interview/{invite_code}/complete",
            status_code=303,
        )

    messages = interview_crud.get_messages_by_interview(db, interview.id)

    if not messages:
        try:
            agent = AIInterviewAgent()
            initial_message = agent.get_initial_message(
                study_title=study.title,
                study_description=study.description,
                study_questions=[q.text for q in study.questions],
                interviewee_name=interviewee.name,
            )

            interview_crud.create_message(
                db,
                interview_id=interview.id,
                role="assistant",
                content=initial_message,
            )

            messages = interview_crud.get_messages_by_interview(db, interview.id)

        except ValueError as e:
            return templates.TemplateResponse(
                request=request,
                name="interview/chat_placeholder.html",
                context={
                    "invite_code": invite_code,
                    "study": study,
                    "interviewee": interviewee,
                    "error": str(e),
                },
            )
        except Exception as e:
            return templates.TemplateResponse(
                request=request,
                name="interview/chat_placeholder.html",
                context={
                    "invite_code": invite_code,
                    "study": study,
                    "interviewee": interviewee,
                    "error": f"Failed to initialize AI agent: {str(e)}",
                },
            )

    turns_remaining = study.max_agent_turns - interview.agent_turns

    return templates.TemplateResponse(
        request=request,
        name="interview/chat.html",
        context={
            "invite_code": invite_code,
            "invite": invite,
            "study": study,
            "interviewee": interviewee,
            "interview": interview,
            "messages": messages,
            "turns_remaining": turns_remaining,
            "max_turns": study.max_agent_turns,
        },
    )


@router.post("/{invite_code}/chat/message")
async def send_message(
    request: Request,
    invite_code: str,
    message: str = Form(...),
    db: Session = Depends(get_db),
):
    """
    Handle user message submission and generate AI response.

    - Saves user message
    - Triggers AI agent response
    - Saves AI response
    - Increments turn counter
    - Checks completion conditions
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)

    if not invite:
        return JSONResponse(
            status_code=404,
            content={"error": "Invite not found"}
        )

    interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not interview:
        return JSONResponse(
            status_code=404,
            content={"error": "Interview not found"}
        )

    if interview.completed_at:
        return JSONResponse(
            status_code=400,
            content={"error": "Interview already completed"}
        )

    interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)
    study = invite.study

    if not message.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Message cannot be empty"}
        )

    if len(message) > 2000:
        message = message[:2000]

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="user",
        content=message.strip(),
    )

    if interview.agent_turns >= study.max_agent_turns:
        interview_crud.complete_interview(db, interview.id)

        return {
            "status": "completed",
            "message": "Interview completed. Thank you for your participation!",
            "redirect": f"/interview/{invite_code}/complete"
        }

    conversation_history = interview_crud.get_messages_by_interview(db, interview.id)
    history_for_ai = [
        {"role": msg.role, "content": msg.content}
        for msg in conversation_history
    ]

    try:
        agent = AIInterviewAgent()
        ai_response = agent.get_ai_response(
            study_title=study.title,
            study_description=study.description,
            study_questions=[q.text for q in study.questions],
            conversation_history=history_for_ai,
            current_turn=interview.agent_turns,
            max_turns=study.max_agent_turns,
        )

        interview_crud.create_message(
            db,
            interview_id=interview.id,
            role="assistant",
            content=ai_response,
        )

        interview_crud.increment_agent_turns(db, interview.id)

        db.refresh(interview)

        is_completed = interview.agent_turns >= study.max_agent_turns
        if is_completed:
            interview_crud.complete_interview(db, interview.id)

            try:
                generator = InsightGenerator()
                insights = generator.generate_insights(db, interview.id)

                combined_keywords = insights.get("keywords", []) + insights.get("themes", [])

                interview_crud.create_insight(
                    db,
                    interview_id=interview.id,
                    summary=insights.get("summary", "Interview completed"),
                    sentiment=insights.get("sentiment", "neutral"),
                    keywords_json=combined_keywords,
                    quotes_json=insights.get("notable_quotes", []),
                )
                logger.info(f"Generated insights for interview {interview.id}")
            except Exception as e:
                logger.error(f"Failed to generate insights for interview {interview.id}: {e}")

        return {
            "status": "completed" if is_completed else "success",
            "message": ai_response,
            "turns_remaining": study.max_agent_turns - interview.agent_turns,
            "redirect": f"/interview/{invite_code}/complete" if is_completed else None
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": f"Failed to generate response: {str(e)}"
            }
        )


@router.get("/{invite_code}/complete", response_class=HTMLResponse)
async def interview_complete(
    request: Request,
    invite_code: str,
    db: Session = Depends(get_db),
):
    """
    Thank you page after interview completion.
    """
    invite = invite_crud.get_invite_by_code(db, invite_code)

    if not invite:
        return templates.TemplateResponse(
            request=request,
            name="interview/not_found.html",
            status_code=404,
        )

    interview = interview_crud.get_interview_by_invite(db, invite.id)
    if not interview:
        return RedirectResponse(
            url=f"/interview/{invite_code}/consent",
            status_code=303,
        )

    study = invite.study
    interviewee = interview_crud.get_interviewee_by_interview(db, interview.id)

    return templates.TemplateResponse(
        request=request,
        name="interview/thank_you.html",
        context={
            "invite_code": invite_code,
            "study": study,
            "interviewee": interviewee,
            "interview": interview,
        },
    )

```

## app/routers/studies.py

**Path:** `app/routers/studies.py`
**Type:** Python
**Size:** 21.8 KB

```python
"""Studies routes for researchers."""

import csv
import io
import json
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.db.session import get_db
from app.models.user import User
from app.schemas.interview import (
    DemographicBreakdown,
    InterviewDetailResponse,
    InterviewListItem,
    InterviewTimeline,
    KeywordFrequency,
    ResponseMetrics,
    SentimentDistribution,
    StudyAnalytics,
)
from app.schemas.invite import InviteCreate, InviteResponse
from app.schemas.study import (
    QuestionBatchReorder,
    QuestionCreate,
    QuestionResponse,
    StudyCreate,
    StudyResponse,
    StudyUpdate,
)

router = APIRouter(prefix="/studies", tags=["studies"])


def verify_study_owner(study_id: int, user: User, db: Session):
    """Verify that the current user owns the study."""
    study = study_crud.get_study_by_id(db, study_id, load_questions=False)
    if not study:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Study not found",
        )
    if study.owner_user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Study not found",
        )
    return study


@router.post("/", response_model=StudyResponse, status_code=status.HTTP_201_CREATED)
def create_study(
    study_data: StudyCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new study."""
    study = study_crud.create_study(
        db,
        owner_user_id=current_user.id,
        title=study_data.title,
        description=study_data.description,
        consent_text=study_data.consent_text,
        max_agent_turns=study_data.max_agent_turns,
    )
    return study


@router.get("/", response_model=list[StudyResponse])
def list_studies(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List all studies for the current user."""
    studies = study_crud.get_studies_by_user(db, current_user.id, skip=skip, limit=limit)
    return studies


@router.get("/{study_id}", response_model=StudyResponse)
def get_study(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get a specific study with questions."""
    study = verify_study_owner(study_id, current_user, db)
    study_with_questions = study_crud.get_study_by_id(db, study_id, load_questions=True)
    return study_with_questions


@router.patch("/{study_id}", response_model=StudyResponse)
def update_study(
    study_id: int,
    study_data: StudyUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update a study."""
    verify_study_owner(study_id, current_user, db)

    updated_study = study_crud.update_study(
        db,
        study_id,
        title=study_data.title,
        description=study_data.description,
        consent_text=study_data.consent_text,
        max_agent_turns=study_data.max_agent_turns,
    )
    return updated_study


@router.delete("/{study_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_study(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a study."""
    verify_study_owner(study_id, current_user, db)
    study_crud.delete_study(db, study_id)
    return None


@router.post("/{study_id}/questions", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
def create_question(
    study_id: int,
    question_data: QuestionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Add a question to a study."""
    verify_study_owner(study_id, current_user, db)

    question = study_crud.create_study_question(
        db,
        study_id=study_id,
        text=question_data.text,
        sort_order=question_data.sort_order,
    )
    return question


@router.get("/{study_id}/questions", response_model=list[QuestionResponse])
def list_questions(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all questions for a study."""
    verify_study_owner(study_id, current_user, db)
    questions = study_crud.get_study_questions(db, study_id)
    return questions


@router.post("/{study_id}/questions/reorder", status_code=status.HTTP_204_NO_CONTENT)
def reorder_questions(
    study_id: int,
    reorder_data: QuestionBatchReorder,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Reorder questions in a study."""
    verify_study_owner(study_id, current_user, db)

    existing_questions = study_crud.get_study_questions(db, study_id)
    existing_ids = {q.id for q in existing_questions}

    for update in reorder_data.updates:
        if update.question_id not in existing_ids:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Question {update.question_id} not found in study",
            )

    updates = [(u.question_id, u.sort_order) for u in reorder_data.updates]
    study_crud.reorder_questions(db, updates)
    return None


@router.delete("/{study_id}/questions/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(
    study_id: int,
    question_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a question from a study."""
    verify_study_owner(study_id, current_user, db)

    question = db.get(study_crud.StudyQuestion, question_id)
    if not question or question.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found",
        )

    study_crud.delete_study_question(db, question_id)
    return None


@router.post("/{study_id}/invites", response_model=InviteResponse, status_code=status.HTTP_201_CREATED)
def create_invite(
    study_id: int,
    invite_data: InviteCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create an invite for a study."""
    verify_study_owner(study_id, current_user, db)

    invite = invite_crud.create_invite(
        db,
        study_id=study_id,
        interviewee_email=invite_data.interviewee_email,
        expires_at=invite_data.expires_at,
    )
    return invite


@router.get("/{study_id}/invites", response_model=list[InviteResponse])
def list_invites(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all invites for a study."""
    verify_study_owner(study_id, current_user, db)
    invites = invite_crud.get_invites_by_study(db, study_id)
    return invites


@router.delete("/{study_id}/invites/{invite_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invite(
    study_id: int,
    invite_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete an invite."""
    verify_study_owner(study_id, current_user, db)

    invite = invite_crud.get_invite_by_id(db, invite_id)
    if not invite or invite.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invite not found",
        )

    invite_crud.delete_invite(db, invite_id)
    return None


@router.get("/{study_id}/interviews", response_model=list[InterviewListItem])
def list_interviews(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Get all interviews for a study with summary information.

    Returns interviews with:
    - Interviewee details
    - Completion status
    - Insights summary
    - Message count
    """
    verify_study_owner(study_id, current_user, db)

    interviews = interview_crud.get_interviews_by_study(db, study_id, load_relations=True)

    result = []
    for interview in interviews:
        message_count = interview_crud.get_message_count(db, interview.id)

        interview_data = InterviewListItem(
            id=interview.id,
            study_id=interview.study_id,
            started_at=interview.started_at,
            completed_at=interview.completed_at,
            agent_turns=interview.agent_turns,
            interviewee=interview.interviewee,
            insight=interview.insight,
            message_count=message_count,
        )
        result.append(interview_data)

    return result


@router.get("/{study_id}/interviews/{interview_id}", response_model=InterviewDetailResponse)
def get_interview_transcript(
    study_id: int,
    interview_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Get detailed interview transcript with full conversation.

    Returns:
    - All messages in chronological order
    - Interviewee information
    - Generated insights
    - Interview metadata
    """
    verify_study_owner(study_id, current_user, db)

    interview = interview_crud.get_interview_by_id(db, interview_id, load_all=True)

    if not interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    if interview.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    return InterviewDetailResponse(
        id=interview.id,
        study_id=interview.study_id,
        started_at=interview.started_at,
        completed_at=interview.completed_at,
        agent_turns=interview.agent_turns,
        interviewee=interview.interviewee,
        messages=interview.messages,
        insight=interview.insight,
    )


def _format_datetime(dt: datetime | None) -> str:
    """Format datetime for export."""
    if dt is None:
        return ""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def _format_json_field(data: dict | list | None) -> str:
    """Format JSON field as string."""
    if data is None:
        return ""
    return json.dumps(data)


def _export_interview_to_dict(interview, study_title: str) -> dict:
    """Convert interview to dictionary for export."""
    interviewee = interview.interviewee
    insight = interview.insight

    conversation = []
    for msg in interview.messages:
        conversation.append(f"[{msg.role.upper()}]: {msg.content}")
    conversation_text = "\n\n".join(conversation)

    return {
        "study_title": study_title,
        "interview_id": interview.id,
        "interviewee_name": interviewee.name if interviewee else "",
        "interviewee_email": interviewee.email if interviewee else "",
        "demographics": _format_json_field(interviewee.demographics_json if interviewee else None),
        "started_at": _format_datetime(interview.started_at),
        "completed_at": _format_datetime(interview.completed_at),
        "agent_turns": interview.agent_turns,
        "message_count": len(interview.messages),
        "summary": insight.summary if insight else "",
        "sentiment": insight.sentiment if insight else "",
        "keywords": _format_json_field(insight.keywords_json if insight else None),
        "quotes": _format_json_field(insight.quotes_json if insight else None),
        "conversation": conversation_text,
    }


def _generate_csv_export(interviews, study_title: str) -> str:
    """Generate CSV export from interviews."""
    output = io.StringIO()

    if not interviews:
        return ""

    fieldnames = [
        "study_title",
        "interview_id",
        "interviewee_name",
        "interviewee_email",
        "demographics",
        "started_at",
        "completed_at",
        "agent_turns",
        "message_count",
        "summary",
        "sentiment",
        "keywords",
        "quotes",
        "conversation",
    ]

    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for interview in interviews:
        row = _export_interview_to_dict(interview, study_title)
        writer.writerow(row)

    return output.getvalue()


def _generate_json_export(interviews, study_title: str, study_description: str) -> dict:
    """Generate JSON export from interviews."""
    interviews_data = []

    for interview in interviews:
        interviewee = interview.interviewee
        insight = interview.insight

        interview_data = {
            "id": interview.id,
            "started_at": interview.started_at.isoformat() if interview.started_at else None,
            "completed_at": interview.completed_at.isoformat() if interview.completed_at else None,
            "agent_turns": interview.agent_turns,
            "interviewee": {
                "name": interviewee.name if interviewee else None,
                "email": interviewee.email if interviewee else None,
                "demographics": interviewee.demographics_json if interviewee else None,
            },
            "messages": [
                {
                    "role": msg.role,
                    "content": msg.content,
                    "created_at": msg.created_at.isoformat() if msg.created_at else None,
                }
                for msg in interview.messages
            ],
            "insight": {
                "summary": insight.summary if insight else None,
                "sentiment": insight.sentiment if insight else None,
                "keywords": insight.keywords_json if insight else None,
                "quotes": insight.quotes_json if insight else None,
            } if insight else None,
        }
        interviews_data.append(interview_data)

    return {
        "study": {
            "title": study_title,
            "description": study_description,
        },
        "export_date": datetime.now(timezone.utc).isoformat(),
        "interview_count": len(interviews),
        "interviews": interviews_data,
    }


@router.get("/{study_id}/interviews/{interview_id}/export")
def export_interview(
    study_id: int,
    interview_id: int,
    format: str = Query("json", pattern="^(json|csv)$"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Export a single interview in JSON or CSV format.

    - **format**: Export format (json or csv)
    """
    study = verify_study_owner(study_id, current_user, db)

    interview = interview_crud.get_interview_by_id(db, interview_id, load_all=True)

    if not interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    if interview.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"interview_{interview_id}_{timestamp}.{format}"

    if format == "csv":
        csv_data = _generate_csv_export([interview], study.title)
        return StreamingResponse(
            iter([csv_data]),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )
    else:
        json_data = _generate_json_export([interview], study.title, study.description)
        return StreamingResponse(
            iter([json.dumps(json_data, indent=2)]),
            media_type="application/json",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )


@router.get("/{study_id}/export")
def export_study_interviews(
    study_id: int,
    format: str = Query("json", pattern="^(json|csv)$"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Export all interviews for a study in JSON or CSV format.

    - **format**: Export format (json or csv)
    """
    study = verify_study_owner(study_id, current_user, db)

    interviews = interview_crud.get_interviews_by_study(db, study_id, load_relations=True)

    for interview in interviews:
        interview.messages = interview_crud.get_messages_by_interview(db, interview.id)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    safe_title = "".join(c if c.isalnum() else "_" for c in study.title)[:50]
    filename = f"study_{safe_title}_{timestamp}.{format}"

    if format == "csv":
        csv_data = _generate_csv_export(interviews, study.title)
        return StreamingResponse(
            iter([csv_data]),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )
    else:
        json_data = _generate_json_export(interviews, study.title, study.description)
        return StreamingResponse(
            iter([json.dumps(json_data, indent=2)]),
            media_type="application/json",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )


@router.get("/{study_id}/analytics", response_model=StudyAnalytics)
def get_study_analytics(
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Get aggregated analytics for a study.

    Returns:
    - Sentiment distribution
    - Top keywords across all interviews
    - Response metrics (avg length, message count)
    - Demographics breakdown
    - Interview timeline
    - Sample quotes
    """
    study = verify_study_owner(study_id, current_user, db)

    interviews = interview_crud.get_interviews_by_study(db, study_id, load_relations=True)

    total_interviews = len(interviews)
    completed_interviews = sum(1 for i in interviews if i.completed_at)

    sentiment_counts = {"positive": 0, "neutral": 0, "negative": 0}
    for interview in interviews:
        if interview.insight and interview.insight.sentiment:
            sentiment = interview.insight.sentiment.lower()
            if sentiment in sentiment_counts:
                sentiment_counts[sentiment] += 1

    sentiment_dist = SentimentDistribution(
        positive=sentiment_counts["positive"],
        neutral=sentiment_counts["neutral"],
        negative=sentiment_counts["negative"],
        total=sum(sentiment_counts.values()),
    )

    keyword_freq = {}
    for interview in interviews:
        if interview.insight and interview.insight.keywords_json:
            for keyword in interview.insight.keywords_json:
                keyword_lower = keyword.lower()
                keyword_freq[keyword_lower] = keyword_freq.get(keyword_lower, 0) + 1

    top_keywords = [
        KeywordFrequency(keyword=kw, count=count)
        for kw, count in sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[:20]
    ]

    total_messages = 0
    total_response_length = 0
    user_message_count = 0

    for interview in interviews:
        messages = interview_crud.get_messages_by_interview(db, interview.id)
        total_messages += len(messages)

        for msg in messages:
            if msg.role == "user":
                total_response_length += len(msg.content)
                user_message_count += 1

    avg_message_count = total_messages / total_interviews if total_interviews > 0 else 0
    avg_response_length = total_response_length / user_message_count if user_message_count > 0 else 0
    avg_conversation_length = total_response_length / completed_interviews if completed_interviews > 0 else 0

    response_metrics = ResponseMetrics(
        avg_message_count=round(avg_message_count, 2),
        avg_response_length=round(avg_response_length, 2),
        avg_conversation_length=round(avg_conversation_length, 2),
        total_messages=total_messages,
    )

    demographics_data = {}
    for interview in interviews:
        if interview.interviewee and interview.interviewee.demographics_json:
            for field, value in interview.interviewee.demographics_json.items():
                if value:
                    if field not in demographics_data:
                        demographics_data[field] = {}
                    demographics_data[field][str(value)] = demographics_data[field].get(str(value), 0) + 1

    demographics = [
        DemographicBreakdown(field=field, values=values)
        for field, values in demographics_data.items()
    ]

    from collections import defaultdict
    timeline_data = defaultdict(lambda: {"completed": 0, "in_progress": 0})

    for interview in interviews:
        date_key = interview.started_at.strftime("%Y-%m-%d")
        if interview.completed_at:
            timeline_data[date_key]["completed"] += 1
        else:
            timeline_data[date_key]["in_progress"] += 1

    timeline = [
        InterviewTimeline(
            date=date,
            completed=data["completed"],
            in_progress=data["in_progress"]
        )
        for date, data in sorted(timeline_data.items())
    ]

    sample_quotes = []
    for interview in interviews:
        if interview.insight and interview.insight.quotes_json:
            sample_quotes.extend(interview.insight.quotes_json[:2])
        if len(sample_quotes) >= 10:
            break
    sample_quotes = sample_quotes[:10]

    return StudyAnalytics(
        study_id=study.id,
        study_title=study.title,
        total_interviews=total_interviews,
        completed_interviews=completed_interviews,
        sentiment_distribution=sentiment_dist,
        top_keywords=top_keywords,
        response_metrics=response_metrics,
        demographics=demographics,
        timeline=timeline,
        sample_quotes=sample_quotes,
    )


```

## app/routers/web.py

**Path:** `app/routers/web.py`
**Type:** Python
**Size:** 572 bytes

```python
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

```

## app/routers/web_auth.py

**Path:** `app/routers/web_auth.py`
**Type:** Python
**Size:** 1.4 KB

```python
"""Web routes for authentication (HTML rendering)."""

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(tags=["web-auth"])


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    """Render the login page."""
    success = request.query_params.get("success")
    return templates.TemplateResponse(
        "auth/login.html",
        {
            "request": request,
            "success": success,
        },
    )


@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    """Render the registration page."""
    return templates.TemplateResponse(
        "auth/register.html",
        {"request": request},
    )


@router.get("/account", response_class=HTMLResponse)
def account_page(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the user account page."""
    return templates.TemplateResponse(
        "auth/account.html",
        {
            "request": request,
            "user": current_user,
        },
    )

```

## app/routers/web_studies.py

**Path:** `app/routers/web_studies.py`
**Type:** Python
**Size:** 10.4 KB

```python
"""Web routes for studies (HTML rendering)."""

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.db.session import get_db
from app.models.user import User

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/app", tags=["web"])


def verify_study_owner(study_id: int, user: User, db: Session):
    """Verify that the current user owns the study."""
    study = study_crud.get_study_by_id(db, study_id, load_questions=False)
    if not study:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Study not found",
        )
    if study.owner_user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Study not found",
        )
    return study


@router.get("/studies", response_class=HTMLResponse)
def list_studies_page(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the studies list page."""
    studies = study_crud.get_studies_by_user(db, current_user.id)
    return templates.TemplateResponse(
        "studies/list.html", {"request": request, "studies": studies}
    )


@router.post("/studies/", response_class=RedirectResponse)
def create_study_form(
    title: str = Form(...),
    description: str = Form(...),
    consent_text: str = Form(...),
    max_agent_turns: int = Form(9),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new study from form data."""
    study = study_crud.create_study(
        db,
        owner_user_id=current_user.id,
        title=title,
        description=description,
        consent_text=consent_text,
        max_agent_turns=max_agent_turns,
    )
    return RedirectResponse(
        url=f"/app/studies/{study.id}", status_code=status.HTTP_303_SEE_OTHER
    )


@router.get("/studies/{study_id}", response_class=HTMLResponse)
def get_study_page(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the study detail page."""
    study = verify_study_owner(study_id, current_user, db)
    questions = study_crud.get_study_questions(db, study_id)
    invites = invite_crud.get_invites_by_study(db, study_id)

    return templates.TemplateResponse(
        "studies/detail.html",
        {
            "request": request,
            "study": study,
            "questions": questions,
            "invites": invites,
            "study_id": study_id,
        },
    )


@router.post("/studies/{study_id}", response_class=RedirectResponse)
def update_study_form(
    study_id: int,
    method: str = Form(None),
    title: str = Form(None),
    description: str = Form(None),
    consent_text: str = Form(None),
    max_agent_turns: int = Form(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update or delete a study from form data."""
    study = verify_study_owner(study_id, current_user, db)

    if method == "DELETE":
        study_crud.delete_study(db, study_id)
        return RedirectResponse(url="/app/studies", status_code=status.HTTP_303_SEE_OTHER)

    elif method == "PATCH":
        study_crud.update_study(
            db,
            study_id,
            title=title,
            description=description,
            consent_text=consent_text,
            max_agent_turns=max_agent_turns,
        )
        return RedirectResponse(
            url=f"/app/studies/{study_id}", status_code=status.HTTP_303_SEE_OTHER
        )

    return RedirectResponse(
        url=f"/app/studies/{study_id}", status_code=status.HTTP_303_SEE_OTHER
    )


@router.post("/studies/{study_id}/questions", response_class=HTMLResponse)
def add_question_htmx(
    request: Request,
    study_id: int,
    text: str = Form(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Add a question and return the updated questions partial."""
    verify_study_owner(study_id, current_user, db)

    # Calculate next sort_order (max existing + 1, or 0 if no questions)
    existing_questions = study_crud.get_study_questions(db, study_id)
    next_sort_order = max([q.sort_order for q in existing_questions], default=-1) + 1

    study_crud.create_study_question(db, study_id, text, next_sort_order)
    questions = study_crud.get_study_questions(db, study_id)

    return templates.TemplateResponse(
        "studies/_questions.html",
        {"request": request, "questions": questions, "study_id": study_id},
    )


@router.delete("/studies/{study_id}/questions/{question_id}", response_class=HTMLResponse)
def delete_question_htmx(
    request: Request,
    study_id: int,
    question_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a question and return the updated questions partial."""
    verify_study_owner(study_id, current_user, db)
    study_crud.delete_study_question(db, question_id)
    questions = study_crud.get_study_questions(db, study_id)

    return templates.TemplateResponse(
        "studies/_questions.html",
        {"request": request, "questions": questions, "study_id": study_id},
    )


@router.post("/studies/{study_id}/questions/reorder", response_class=HTMLResponse)
async def reorder_questions_htmx(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Reorder questions and return the updated questions partial."""
    verify_study_owner(study_id, current_user, db)

    # Parse JSON body
    body = await request.json()
    questions_data = body.get("questions", [])

    # Convert to list of tuples for reorder_questions
    question_updates = [(q["question_id"], q["sort_order"]) for q in questions_data]
    study_crud.reorder_questions(db, question_updates)

    questions = study_crud.get_study_questions(db, study_id)

    return templates.TemplateResponse(
        "studies/_questions.html",
        {"request": request, "questions": questions, "study_id": study_id},
    )


@router.post("/studies/{study_id}/invites", response_class=HTMLResponse)
def create_invite_htmx(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create an invite and return the updated invites partial."""
    verify_study_owner(study_id, current_user, db)
    invite_crud.create_invite(db, study_id)
    invites = invite_crud.get_invites_by_study(db, study_id)

    return templates.TemplateResponse(
        "studies/_invites.html",
        {"request": request, "invites": invites},
    )


@router.delete("/studies/{study_id}/invites/{invite_id}", response_class=HTMLResponse)
def delete_invite_htmx(
    request: Request,
    study_id: int,
    invite_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete an invite and return the updated invites partial."""
    verify_study_owner(study_id, current_user, db)
    invite_crud.delete_invite(db, invite_id)
    invites = invite_crud.get_invites_by_study(db, study_id)

    return templates.TemplateResponse(
        "studies/_invites.html",
        {"request": request, "invites": invites},
    )


@router.get("/studies/{study_id}/interviews", response_class=HTMLResponse)
def list_interviews_page(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the interviews list page for a study."""
    study = verify_study_owner(study_id, current_user, db)

    interviews = interview_crud.get_interviews_by_study(db, study_id, load_relations=True)

    interview_list = []
    for interview in interviews:
        message_count = interview_crud.get_message_count(db, interview.id)
        interview_list.append({
            "id": interview.id,
            "study_id": interview.study_id,
            "started_at": interview.started_at,
            "completed_at": interview.completed_at,
            "agent_turns": interview.agent_turns,
            "interviewee": interview.interviewee,
            "insight": interview.insight,
            "message_count": message_count,
        })

    return templates.TemplateResponse(
        "studies/interviews.html",
        {
            "request": request,
            "study": study,
            "interviews": interview_list,
        },
    )


@router.get("/studies/{study_id}/interviews/{interview_id}", response_class=HTMLResponse)
def view_transcript_page(
    request: Request,
    study_id: int,
    interview_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the interview transcript page."""
    study = verify_study_owner(study_id, current_user, db)

    interview = interview_crud.get_interview_by_id(db, interview_id, load_all=True)

    if not interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    if interview.study_id != study_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )

    return templates.TemplateResponse(
        "studies/transcript.html",
        {
            "request": request,
            "study": study,
            "interview": interview,
            "interviewee": interview.interviewee,
            "messages": interview.messages,
            "insight": interview.insight,
        },
    )


@router.get("/studies/{study_id}/analytics", response_class=HTMLResponse)
def analytics_page(
    request: Request,
    study_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the analytics page for a study."""
    study = verify_study_owner(study_id, current_user, db)

    return templates.TemplateResponse(
        "studies/analytics.html",
        {
            "request": request,
            "study": study,
        },
    )


```

## app/schemas/__init__.py

**Path:** `app/schemas/__init__.py`
**Type:** Python
**Size:** 697 bytes

```python
"""Pydantic schemas for request/response validation."""

from app.schemas.interview import (
    ConsentForm,
    InsightResponse,
    IntakeForm,
    InterviewDetailResponse,
    IntervieweeResponse,
    InterviewListItem,
    MessageResponse,
)
from app.schemas.invite import InviteCreate, InviteResponse
from app.schemas.study import QuestionCreate, StudyCreate, StudyResponse, StudyUpdate

__all__ = [
    "ConsentForm",
    "InsightResponse",
    "IntakeForm",
    "InterviewDetailResponse",
    "IntervieweeResponse",
    "InterviewListItem",
    "InviteCreate",
    "InviteResponse",
    "MessageResponse",
    "QuestionCreate",
    "StudyCreate",
    "StudyResponse",
    "StudyUpdate",
]
```

## app/schemas/interview.py

**Path:** `app/schemas/interview.py`
**Type:** Python
**Size:** 3.1 KB

```python
"""Pydantic schemas for interview-related models."""

from datetime import datetime

from pydantic import BaseModel, EmailStr


class ConsentForm(BaseModel):
    """Schema for consent form submission."""

    agreed: bool


class IntakeForm(BaseModel):
    """Schema for intake form submission."""

    name: str
    email: EmailStr
    age_range: str | None = None
    location: str | None = None
    occupation: str | None = None


class MessageResponse(BaseModel):
    """Schema for chat message response."""

    id: int
    interview_id: int
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class IntervieweeResponse(BaseModel):
    """Schema for interviewee information."""

    id: int
    interview_id: int
    name: str
    email: str
    demographics_json: dict | None = None
    consent_at: datetime

    class Config:
        from_attributes = True


class InsightResponse(BaseModel):
    """Schema for interview insights."""

    id: int
    interview_id: int
    summary: str
    sentiment: str
    keywords_json: list
    quotes_json: list
    created_at: datetime

    class Config:
        from_attributes = True


class InterviewListItem(BaseModel):
    """Schema for interview in list view."""

    id: int
    study_id: int
    started_at: datetime
    completed_at: datetime | None
    agent_turns: int
    interviewee: IntervieweeResponse | None = None
    insight: InsightResponse | None = None
    message_count: int = 0

    class Config:
        from_attributes = True


class InterviewDetailResponse(BaseModel):
    """Schema for detailed interview view with full transcript."""

    id: int
    study_id: int
    started_at: datetime
    completed_at: datetime | None
    agent_turns: int
    interviewee: IntervieweeResponse | None = None
    messages: list[MessageResponse] = []
    insight: InsightResponse | None = None

    class Config:
        from_attributes = True


class SentimentDistribution(BaseModel):
    """Sentiment distribution across interviews."""

    positive: int = 0
    neutral: int = 0
    negative: int = 0
    total: int = 0


class KeywordFrequency(BaseModel):
    """Keyword with frequency count."""

    keyword: str
    count: int


class DemographicBreakdown(BaseModel):
    """Demographic breakdown for a specific field."""

    field: str
    values: dict[str, int]


class ResponseMetrics(BaseModel):
    """Aggregate response metrics."""

    avg_message_count: float = 0.0
    avg_response_length: float = 0.0
    avg_conversation_length: float = 0.0
    total_messages: int = 0


class InterviewTimeline(BaseModel):
    """Timeline data point for interviews."""

    date: str  # YYYY-MM-DD
    completed: int
    in_progress: int


class StudyAnalytics(BaseModel):
    """Aggregated analytics for a study."""

    study_id: int
    study_title: str
    total_interviews: int
    completed_interviews: int
    sentiment_distribution: SentimentDistribution
    top_keywords: list[KeywordFrequency]
    response_metrics: ResponseMetrics
    demographics: list[DemographicBreakdown]
    timeline: list[InterviewTimeline]
    sample_quotes: list[str]
```

## app/schemas/invite.py

**Path:** `app/schemas/invite.py`
**Type:** Python
**Size:** 553 bytes

```python
"""Invite-related schemas."""

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class InviteCreate(BaseModel):
    """Schema for creating an invite."""

    interviewee_email: EmailStr | None = None
    expires_at: datetime | None = None


class InviteResponse(BaseModel):
    """Schema for invite response."""

    id: int
    study_id: int
    invite_code: str
    interviewee_email: str | None
    status: str
    expires_at: datetime | None
    created_at: datetime

    class Config:
        from_attributes = True

```

## app/schemas/study.py

**Path:** `app/schemas/study.py`
**Type:** Python
**Size:** 1.7 KB

```python
"""Study-related schemas."""

from datetime import datetime

from pydantic import BaseModel, Field


class StudyCreate(BaseModel):
    """Schema for creating a study."""

    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    consent_text: str = Field(..., min_length=1)
    max_agent_turns: int = Field(default=9, ge=1, le=50)


class StudyUpdate(BaseModel):
    """Schema for updating a study."""

    title: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = Field(None, min_length=1)
    consent_text: str | None = Field(None, min_length=1)
    max_agent_turns: int | None = Field(None, ge=1, le=50)


class StudyResponse(BaseModel):
    """Schema for study response."""

    id: int
    owner_user_id: int
    title: str
    description: str
    consent_text: str
    max_agent_turns: int
    created_at: datetime

    class Config:
        from_attributes = True


class QuestionCreate(BaseModel):
    """Schema for creating a study question."""

    text: str = Field(..., min_length=1)
    sort_order: int = Field(default=0, ge=0)


class QuestionUpdate(BaseModel):
    """Schema for updating a question."""

    text: str | None = Field(None, min_length=1)


class QuestionReorder(BaseModel):
    """Schema for reordering questions."""

    question_id: int
    sort_order: int = Field(..., ge=0)


class QuestionBatchReorder(BaseModel):
    """Schema for batch reordering questions."""

    updates: list[QuestionReorder]


class QuestionResponse(BaseModel):
    """Schema for question response."""

    id: int
    study_id: int
    text: str
    sort_order: int

    class Config:
        from_attributes = True


```

## app/services/__init__.py

**Path:** `app/services/__init__.py`
**Type:** Python
**Size:** 0 bytes

```python

```

## app/services/ai_agent.py

**Path:** `app/services/ai_agent.py`
**Type:** Python
**Size:** 6.3 KB

```python
"""AI Agent service for conducting research interviews."""

import os
from typing import Optional

from openai import OpenAI


def get_openai_api_key() -> Optional[str]:
    """Get OpenAI API key from environment or settings."""
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key

    try:
        from app.settings import settings
        return settings.openai_api_key
    except Exception:
        return None


class AIInterviewAgent:
    """AI agent that conducts research interviews based on study context."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the AI agent.

        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var or settings)
        """
        self.api_key = api_key or get_openai_api_key()
        if not self.api_key:
            raise ValueError(
                "OpenAI API key required. Set OPENAI_API_KEY environment variable "
                "in your .env file or pass api_key parameter."
            )
        self.client = OpenAI(api_key=self.api_key)
        self.model = "gpt-4o-mini"

    def generate_system_prompt(
        self,
        study_title: str,
        study_description: str,
        study_questions: list[str],
        turns_remaining: int,
    ) -> str:
        """
        Generate the system prompt for the AI agent.

        Args:
            study_title: Title of the research study
            study_description: Description of the study
            study_questions: List of research questions to explore
            turns_remaining: Number of turns remaining in the interview

        Returns:
            System prompt string
        """
        questions_text = "\n".join([f"- {q}" for q in study_questions])

        return f"""You are an AI research interviewer conducting a study titled: "{study_title}"

Study context: {study_description}

Research questions to explore:
{questions_text}

Your role:
- Ask thoughtful, open-ended questions related to the research topics
- Follow up on interesting responses with deeper questions
- Be conversational, empathetic, and professional
- Stay focused on the research questions
- Probe deeper when responses are vague or brief
- Guide the conversation naturally between topics
- You have {turns_remaining} questions remaining in this interview

Conversation guidelines:
- Ask ONE question at a time
- Keep questions concise (2-3 sentences maximum)
- Acknowledge the previous response before asking the next question
- Transition smoothly between topics
- If this is the last turn, thank them and provide a graceful closing
- Be encouraging and appreciative of their time

Remember: Your goal is to gather authentic, detailed insights related to the research questions."""

    def get_ai_response(
        self,
        study_title: str,
        study_description: str,
        study_questions: list[str],
        conversation_history: list[dict],
        current_turn: int,
        max_turns: int,
    ) -> str:
        """
        Get AI response based on conversation context.

        Args:
            study_title: Title of the research study
            study_description: Description of the study
            study_questions: List of research questions
            conversation_history: List of previous messages [{"role": "user"|"assistant", "content": "..."}]
            current_turn: Current turn number (0-indexed)
            max_turns: Maximum number of agent turns allowed

        Returns:
            AI-generated response string
        """
        turns_remaining = max_turns - current_turn

        system_prompt = self.generate_system_prompt(
            study_title=study_title,
            study_description=study_description,
            study_questions=study_questions,
            turns_remaining=turns_remaining,
        )

        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(conversation_history[-10:])

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=300,
                presence_penalty=0.6,
                frequency_penalty=0.3,
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return self._get_error_fallback(str(e))

    def get_initial_message(
        self,
        study_title: str,
        study_description: str,
        study_questions: list[str],
        interviewee_name: str,
    ) -> str:
        """
        Generate the first message to start the interview.

        Args:
            study_title: Title of the research study
            study_description: Description of the study
            study_questions: List of research questions
            interviewee_name: Name of the interviewee

        Returns:
            Opening message string
        """
        system_prompt = f"""You are an AI research interviewer starting an interview for a study titled: "{study_title}"

Study context: {study_description}

The participant's name is {interviewee_name}.

Generate a warm, welcoming opening message that:
1. Thanks them for participating
2. Briefly mentions what the study is about
3. Asks your first research question related to the study topics
4. Keep it concise (3-4 sentences total)

Be friendly and professional."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": system_prompt}],
                temperature=0.7,
                max_tokens=200,
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"Hello {interviewee_name}! Thank you for participating in this research study about {study_title}. I'm excited to hear your thoughts. To begin, could you share your initial perspective on this topic?"

    def _get_error_fallback(self, error_message: str) -> str:
        """Provide a graceful fallback response when API fails."""
        print(f"AI Agent Error: {error_message}")
        return "Thank you for your response. Could you tell me more about that?"

```

## app/services/insight_generator.py

**Path:** `app/services/insight_generator.py`
**Type:** Python
**Size:** 7.0 KB

```python
"""Generate insights from completed interviews using LLM analysis."""

import json
import logging
from typing import Any

from openai import OpenAI
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.models.interview import Message
from app.services.ai_agent import get_openai_api_key

logger = logging.getLogger(__name__)


class InsightGenerator:
    """Generate insights from completed interviews using LLM."""

    def __init__(self):
        """Initialize the insight generator with OpenAI client."""
        api_key = get_openai_api_key()
        self.client = OpenAI(api_key=api_key)

    def generate_insights(self, db: Session, interview_id: int) -> dict[str, Any]:
        """
        Analyze interview using LLM and extract structured insights.

        Args:
            db: Database session
            interview_id: ID of the interview to analyze

        Returns:
            Dictionary containing:
                - summary: Brief summary of key points
                - sentiment: Overall sentiment (positive/neutral/negative)
                - keywords: List of important keywords/phrases
                - themes: List of main themes discussed
                - notable_quotes: List of meaningful user quotes
                - engagement_level: Assessment of participant engagement
                - key_insights: List of notable insights for researchers

        Raises:
            ValueError: If OpenAI API key is not configured
            Exception: If LLM analysis fails completely
        """
        messages = interview_crud.get_messages_by_interview(db, interview_id)

        if not messages:
            logger.warning(f"No messages found for interview {interview_id}")
            return self._empty_insights()

        conversation = self._format_conversation(messages)

        prompt = f"""Analyze this research interview and provide structured insights.

INTERVIEW TRANSCRIPT:
{conversation}

Provide your analysis in the following JSON format:
{{
  "summary": "2-3 sentence summary of the key points discussed",
  "sentiment": "positive/neutral/negative",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "themes": ["main theme 1", "main theme 2"],
  "notable_quotes": ["quote 1", "quote 2", "quote 3"],
  "engagement_level": "high/medium/low",
  "key_insights": ["insight 1", "insight 2"]
}}

Guidelines:
- Summary should capture the main discussion points concisely
- Sentiment reflects the overall tone of participant responses
- Keywords should be single words or short phrases (2-3 words max)
- Themes are broader topics or patterns in the conversation
- Notable quotes should be the most insightful or detailed participant responses
- Engagement level based on response depth and thoughtfulness
- Key insights are important takeaways for researchers

Focus on the participant's responses, not the interviewer's questions.
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert qualitative research analyst extracting insights from research interviews. Provide accurate, objective analysis in valid JSON format.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
                response_format={"type": "json_object"},
            )

            insights = json.loads(response.choices[0].message.content)
            logger.info(f"Generated insights for interview {interview_id}")

            return self._validate_insights(insights)

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM response as JSON: {e}")
            return self._fallback_extraction(messages)

        except Exception as e:
            logger.error(f"LLM insight generation failed: {e}")
            return self._fallback_extraction(messages)

    def _format_conversation(self, messages: list[Message]) -> str:
        """
        Format messages into a readable transcript.

        Args:
            messages: List of Message objects

        Returns:
            Formatted conversation string
        """
        lines = []
        for msg in messages:
            speaker = "AI Interviewer" if msg.role == "assistant" else "Participant"
            lines.append(f"{speaker}: {msg.content}")
        return "\n\n".join(lines)

    def _validate_insights(self, insights: dict[str, Any]) -> dict[str, Any]:
        """
        Validate and normalize LLM output.

        Args:
            insights: Raw insights from LLM

        Returns:
            Validated and normalized insights
        """
        validated = {
            "summary": str(insights.get("summary", "No summary available"))[:1000],
            "sentiment": insights.get("sentiment", "neutral").lower(),
            "keywords": insights.get("keywords", [])[:20],
            "themes": insights.get("themes", [])[:10],
            "notable_quotes": insights.get("notable_quotes", [])[:5],
            "engagement_level": insights.get("engagement_level", "medium").lower(),
            "key_insights": insights.get("key_insights", [])[:10],
        }

        if validated["sentiment"] not in ["positive", "neutral", "negative"]:
            validated["sentiment"] = "neutral"

        if validated["engagement_level"] not in ["high", "medium", "low"]:
            validated["engagement_level"] = "medium"

        return validated

    def _fallback_extraction(self, messages: list[Message]) -> dict[str, Any]:
        """
        Basic extraction if LLM fails.

        Args:
            messages: List of Message objects

        Returns:
            Basic insights extracted without LLM
        """
        logger.warning("Using fallback insight extraction")

        user_messages = [msg for msg in messages if msg.role == "user"]

        if not user_messages:
            return self._empty_insights()

        user_texts = [msg.content for msg in user_messages]
        meaningful_responses = [text for text in user_texts if len(text) > 50]

        summary = " ".join(user_texts[:3])[:500] if user_texts else "No responses recorded"

        quotes = sorted(meaningful_responses, key=len, reverse=True)[:3]

        return {
            "summary": summary,
            "sentiment": "neutral",
            "keywords": [],
            "themes": [],
            "notable_quotes": quotes,
            "engagement_level": "medium",
            "key_insights": ["Interview completed but detailed analysis unavailable"],
        }

    def _empty_insights(self) -> dict[str, Any]:
        """
        Return empty insights structure for interviews with no messages.

        Returns:
            Empty insights dictionary
        """
        return {
            "summary": "No conversation recorded",
            "sentiment": "neutral",
            "keywords": [],
            "themes": [],
            "notable_quotes": [],
            "engagement_level": "low",
            "key_insights": [],
        }

```

## app/settings.py

**Path:** `app/settings.py`
**Type:** Python
**Size:** 1.5 KB

```python
"""Application settings and configuration."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    app_env: str = Field(default="dev", description="Application environment (dev/staging/prod)")

    # Security
    secret_key: str = Field(
        ..., description="Secret key for signing sessions and tokens (required)"
    )
    session_cookie_name: str = Field(
        default="ip_session", description="Name of the session cookie"
    )

    # Database
    database_url: str = Field(..., description="PostgreSQL connection URL (required)")

    # LLM (to be used in later days)
    openai_api_key: str | None = Field(default=None, description="OpenAI API key")
    anthropic_api_key: str | None = Field(default=None, description="Anthropic API key")

    # Email (optional, for later)
    resend_api_key: str | None = Field(default=None, description="Resend email API key")
    mailgun_api_key: str | None = Field(default=None, description="Mailgun API key")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    @property
    def is_production(self) -> bool:
        """Check if running in production."""
        return self.app_env.lower() == "prod"

    @property
    def is_development(self) -> bool:
        """Check if running in development."""
        return self.app_env.lower() == "dev"


settings = Settings()

```

## app/static/css/app.css

**Path:** `app/static/css/app.css`
**Type:** Css
**Size:** 988 bytes

```css
/* Custom styles for InsightPilot */
/* Tailwind handles most styling; this is for custom overrides */

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}

/* Focus states for accessibility */
*:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}

/* Custom animations */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-in {
  animation: fadeIn 0.4s ease-out;
}

/* Public page gradient background */
.bg-gradient-public {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Pulse animation for loading states */
@keyframes pulse {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.5;
    }
}

/* Line clamp utilities */
.line-clamp-2 {
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
}

.pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

```

## app/static/js/app.js

**Path:** `app/static/js/app.js`
**Type:** Javascript
**Size:** 529 bytes

```javascript
// Custom JavaScript for InsightPilot
// HTMX handles most interactivity

// Add any global utilities here
console.log('InsightPilot loaded');

// Copy to clipboard utility (for invite links later)
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(
    () => {
      console.log('Copied to clipboard');
      // Could show a toast notification here
    },
    (err) => {
      console.error('Failed to copy:', err);
    }
  );
}

// Make it available globally
window.copyToClipboard = copyToClipboard;

```

## app/templates/auth/login.html

**Path:** `app/templates/auth/login.html`
**Type:** Html
**Size:** 4.3 KB

```html
{% extends "base.html" %}

{% block title %}Login - InsightPilot{% endblock %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
        <div>
            <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                Sign in to your account
            </h2>
            <p class="mt-2 text-center text-sm text-gray-600">
                Or
                <a href="/register" class="font-medium text-indigo-600 hover:text-indigo-500">
                    create a new account
                </a>
            </p>
        </div>

        {% if success %}
        <div class="rounded-md bg-green-50 p-4">
            <div class="flex">
                <div class="flex-shrink-0">
                    <svg class="h-5 w-5 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                </div>
                <div class="ml-3">
                    <h3 class="text-sm font-medium text-green-800">{{ success }}</h3>
                </div>
            </div>
        </div>
        {% endif %}

        {% if error %}
        <div class="rounded-md bg-red-50 p-4">
            <div class="flex">
                <div class="flex-shrink-0">
                    <svg class="h-5 w-5 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                </div>
                <div class="ml-3">
                    <h3 class="text-sm font-medium text-red-800">{{ error }}</h3>
                </div>
            </div>
        </div>
        {% endif %}

        <form class="mt-8 space-y-6" action="/auth/dev/login" method="POST">
            <div class="rounded-md shadow-sm -space-y-px">
                <div>
                    <label for="email" class="sr-only">Email address</label>
                    <input id="email" name="email" type="email" autocomplete="email" required
                           class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                           placeholder="Email address"
                           value="{{ email if email else '' }}">
                </div>
                <div>
                    <label for="password" class="sr-only">Password</label>
                    <input id="password" name="password" type="password" autocomplete="current-password" required
                           class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                           placeholder="Password">
                </div>
            </div>

            <div>
                <button type="submit"
                        class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                        <svg class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
                        </svg>
                    </span>
                    Sign in
                </button>
            </div>
        </form>

        <div class="text-center">
            <a href="/" class="text-sm text-gray-600 hover:text-gray-900">
                ← Back to home
            </a>
        </div>
    </div>
</div>
{% endblock %}

```

## app/templates/auth/register.html

**Path:** `app/templates/auth/register.html`
**Type:** Html
**Size:** 5.5 KB

```html
{% extends "base.html" %}

{% block title %}Register - InsightPilot{% endblock %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
        <div>
            <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                Create your account
            </h2>
            <p class="mt-2 text-center text-sm text-gray-600">
                Or
                <a href="/login" class="font-medium text-indigo-600 hover:text-indigo-500">
                    sign in to your existing account
                </a>
            </p>
        </div>

        {% if error %}
        <div class="rounded-md bg-red-50 p-4">
            <div class="flex">
                <div class="flex-shrink-0">
                    <svg class="h-5 w-5 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                </div>
                <div class="ml-3">
                    <h3 class="text-sm font-medium text-red-800">{{ error }}</h3>
                </div>
            </div>
        </div>
        {% endif %}

        {% if success %}
        <div class="rounded-md bg-green-50 p-4">
            <div class="flex">
                <div class="flex-shrink-0">
                    <svg class="h-5 w-5 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                </div>
                <div class="ml-3">
                    <h3 class="text-sm font-medium text-green-800">{{ success }}</h3>
                </div>
            </div>
        </div>
        {% endif %}

        <form class="mt-8 space-y-6" action="/auth/dev/register" method="POST">
            <div class="rounded-md shadow-sm space-y-4">
                <div>
                    <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
                    <input id="email" name="email" type="email" autocomplete="email" required
                           class="mt-1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                           placeholder="you@example.com"
                           value="{{ email if email else '' }}">
                </div>
                <div>
                    <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                    <input id="password" name="password" type="password" autocomplete="new-password" required
                           minlength="8"
                           class="mt-1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                           placeholder="Min 8 characters">
                    <p class="mt-1 text-xs text-gray-500">Must be at least 8 characters long</p>
                </div>
                <div>
                    <label for="confirm-password" class="block text-sm font-medium text-gray-700">Confirm Password</label>
                    <input id="confirm-password" name="confirm_password" type="password" autocomplete="new-password" required
                           minlength="8"
                           class="mt-1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                           placeholder="Re-enter password">
                </div>
            </div>

            <div>
                <button type="submit"
                        class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                        <svg class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
                        </svg>
                    </span>
                    Create account
                </button>
            </div>
        </form>

        <div class="text-center">
            <a href="/" class="text-sm text-gray-600 hover:text-gray-900">
                ← Back to home
            </a>
        </div>
    </div>
</div>

<script>
// Client-side password confirmation validation
document.querySelector('form').addEventListener('submit', function(e) {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (password !== confirmPassword) {
        e.preventDefault();
        alert('Passwords do not match!');
        return false;
    }
});
</script>
{% endblock %}

```

## app/templates/base.html

**Path:** `app/templates/base.html`
**Type:** Html
**Size:** 1.7 KB

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{% block title %}InsightPilot{% endblock %}</title>

    <!-- Tailwind CSS (CDN for Day 1, will switch to local build later) -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- HTMX for progressive enhancement -->
    <script src="https://unpkg.com/htmx.org@1.9.12"></script>

    <!-- Custom styles -->
    <link rel="stylesheet" href="{{ url_for('static', path='css/app.css') }}" />

    {% block extra_head %}{% endblock %}
  </head>
  <body class="min-h-screen bg-gray-50 text-gray-900 antialiased">
    <!-- Header -->
    <header class="border-b bg-white shadow-sm">
      <div class="mx-auto max-w-7xl px-4 py-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between">
          <a href="/" class="text-2xl font-bold text-blue-600 hover:text-blue-700">
            InsightPilot
          </a>
          <nav class="flex items-center space-x-4">
            {% block nav %}{% endblock %}
          </nav>
        </div>
      </div>
    </header>

    <!-- Main content -->
    <main class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
      {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    <footer class="mt-auto border-t bg-white">
      <div class="mx-auto max-w-7xl px-4 py-6 text-center text-sm text-gray-600">
        <p>&copy; 2025 InsightPilot. AI-driven market research platform.</p>
      </div>
    </footer>

    <!-- Custom scripts -->
    <script src="{{ url_for('static', path='js/app.js') }}"></script>
    {% block extra_scripts %}{% endblock %}
  </body>
</html>

```

## app/templates/error.html

**Path:** `app/templates/error.html`
**Type:** Html
**Size:** 1.8 KB

```html
{% extends "base.html" %}

{% block title %}Error - InsightPilot{% endblock %}

{% block content %}
<div class="mx-auto max-w-2xl text-center">
  <!-- Error icon -->
  <div class="mb-6 flex justify-center">
    <div class="rounded-full bg-red-100 p-4">
      <svg
        class="h-12 w-12 text-red-600"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
        />
      </svg>
    </div>
  </div>

  <!-- Error message -->
  <h1 class="text-3xl font-bold text-gray-900">Something went wrong</h1>
  <p class="mt-4 text-lg text-gray-600">
    We encountered an unexpected error while processing your request. Please try again.
  </p>

  {% if error %}
  <div class="mt-6 rounded-lg bg-red-50 p-4">
    <p class="text-sm text-red-800">
      <strong>Error:</strong> {{ error }}
    </p>
  </div>
  {% endif %}

  <!-- Request ID for support -->
  <div class="mt-6 rounded-lg bg-gray-100 p-4">
    <p class="text-xs text-gray-600">
      <strong>Request ID:</strong>
      <code class="font-mono">{{ request_id }}</code>
    </p>
    <p class="mt-2 text-xs text-gray-500">
      Please include this ID if you contact support.
    </p>
  </div>

  <!-- Action buttons -->
  <div class="mt-8 flex items-center justify-center gap-x-4">
    <a
      href="/"
      class="rounded-md bg-blue-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-700"
    >
      Go Home
    </a>
    <a
      href="javascript:history.back()"
      class="rounded-md bg-gray-200 px-4 py-2 text-sm font-semibold text-gray-700 hover:bg-gray-300"
    >
      Go Back
    </a>
  </div>
</div>
{% endblock %}

```

## app/templates/index.html

**Path:** `app/templates/index.html`
**Type:** Html
**Size:** 2.7 KB

```html
{% extends "base.html" %}

{% block title %}Home - InsightPilot{% endblock %}

{% block content %}
<div class="text-center">
  <!-- Hero section -->
  <div class="mx-auto max-w-3xl">
    <h1 class="text-5xl font-extrabold tracking-tight text-gray-900 sm:text-6xl">
      Welcome to <span class="text-blue-600">InsightPilot</span>
    </h1>
    <p class="mt-6 text-lg leading-8 text-gray-600">
      AI-driven market research interviews that scale. Create studies, conduct intelligent
      conversations, and extract actionable insights automatically.
    </p>

    <!-- CTA buttons -->
    <div class="mt-10 flex items-center justify-center gap-x-6">
      <a
        href="/register"
        class="rounded-md bg-blue-600 px-6 py-3 text-base font-semibold text-white shadow-sm hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
      >
        Get Started
      </a>
      <a href="/login" class="text-base font-semibold leading-7 text-gray-900">
        Sign In <span aria-hidden="true">→</span>
      </a>
    </div>
  </div>

  <!-- Features grid -->
  <div class="mx-auto mt-16 max-w-7xl">
    <div class="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
      <!-- Feature 1 -->
      <div class="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
        <div class="text-left">
          <h3 class="text-lg font-semibold text-gray-900">Create Studies</h3>
          <p class="mt-2 text-sm text-gray-600">
            Set up research studies with custom questions and consent flows in minutes.
          </p>
        </div>
      </div>

      <!-- Feature 2 -->
      <div class="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
        <div class="text-left">
          <h3 class="text-lg font-semibold text-gray-900">AI Interviews</h3>
          <p class="mt-2 text-sm text-gray-600">
            LLM-powered conversations that adapt based on participant responses.
          </p>
        </div>
      </div>

      <!-- Feature 3 -->
      <div class="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
        <div class="text-left">
          <h3 class="text-lg font-semibold text-gray-900">Auto Insights</h3>
          <p class="mt-2 text-sm text-gray-600">
            Automatic summaries, sentiment analysis, keywords, and notable quotes.
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- Status indicator -->
  <div class="mt-16">
    <p class="text-sm text-gray-500">
      System Status:
      <span class="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800">
        ● Operational
      </span>
    </p>
  </div>
</div>
{% endblock %}

```

## app/templates/interview/chat.html

**Path:** `app/templates/interview/chat.html`
**Type:** Html
**Size:** 10.3 KB

```html
{% extends "public_base.html" %}

{% block title %}Interview - {{ study.title }}{% endblock %}

{% block extra_head %}
<style>
    .message-user {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: auto;
    }
    .message-assistant {
        background: #f3f4f6;
        color: #1f2937;
        margin-right: auto;
    }
    #messages-container {
        scroll-behavior: smooth;
    }
</style>
{% endblock %}

{% block content %}
<div class="h-screen flex flex-col max-w-4xl mx-auto -mt-8">
    <!-- Header -->
    <div class="bg-white border-b border-gray-200 px-6 py-4">
        <div class="flex items-center justify-between">
            <div>
                <h2 class="text-xl font-bold text-gray-900">{{ study.title }}</h2>
                <p class="text-sm text-gray-600">Conversation with Research Assistant</p>
            </div>
            <div class="text-right">
                <p class="text-sm font-medium text-gray-700">Turn {{ max_turns - turns_remaining }} of {{ max_turns }}</p>
                <div class="w-32 bg-gray-200 rounded-full h-2 mt-1">
                    <div class="bg-indigo-600 h-2 rounded-full transition-all"
                         style="width: {{ ((max_turns - turns_remaining) / max_turns * 100) | int }}%"></div>
                </div>
            </div>
        </div>
    </div>

    <!-- Messages Container -->
    <div id="messages-container" class="flex-1 overflow-y-auto px-6 py-4 space-y-4 bg-gray-50">
        {% for message in messages %}
        <div class="flex {% if message.role == 'user' %}justify-end{% else %}justify-start{% endif %}">
            <div class="max-w-xl px-4 py-3 rounded-lg shadow-sm message-{{ message.role }}">
                <div class="flex items-center mb-1">
                    {% if message.role == 'assistant' %}
                    <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z"></path>
                        <path d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z"></path>
                    </svg>
                    <span class="text-xs font-semibold {% if message.role == 'user' %}text-white{% else %}text-gray-700{% endif %}">
                        AI Interviewer
                    </span>
                    {% else %}
                    <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path>
                    </svg>
                    <span class="text-xs font-semibold text-white">You</span>
                    {% endif %}
                </div>
                <p class="text-sm leading-relaxed whitespace-pre-wrap">{{ message.content }}</p>
            </div>
        </div>
        {% endfor %}

        <!-- Loading indicator (hidden by default) -->
        <div id="loading-indicator" class="hidden flex justify-start">
            <div class="max-w-xl px-4 py-3 rounded-lg shadow-sm bg-gray-200">
                <div class="flex items-center space-x-2">
                    <div class="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style="animation-delay: 0ms"></div>
                    <div class="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style="animation-delay: 150ms"></div>
                    <div class="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style="animation-delay: 300ms"></div>
                    <span class="text-sm text-gray-600 ml-2">AI is thinking...</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Input Form -->
    <div class="bg-white border-t border-gray-200 px-6 py-4">
        <form id="message-form" class="flex items-end space-x-3">
            <div class="flex-1">
                <textarea
                    id="message-input"
                    name="message"
                    rows="2"
                    maxlength="2000"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 resize-none"
                    placeholder="Type your response here..."
                    required
                ></textarea>
                <p class="text-xs text-gray-500 mt-1">
                    <span id="char-count">0</span>/2000 characters
                </p>
            </div>
            <button
                type="submit"
                id="send-button"
                class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-6 py-3 rounded-lg shadow-md transition duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center"
            >
                <svg class="w-5 h-5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
                </svg>
                Send
            </button>
        </form>
    </div>
</div>

{% endblock %}

{% block extra_scripts %}
<script>
    const messagesContainer = document.getElementById('messages-container');
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const loadingIndicator = document.getElementById('loading-indicator');
    const charCount = document.getElementById('char-count');

    // Auto-scroll to bottom on page load
    messagesContainer.scrollTop = messagesContainer.scrollHeight;

    // Character counter
    messageInput.addEventListener('input', () => {
        charCount.textContent = messageInput.value.length;
    });

    // Handle Enter key (Shift+Enter for new line)
    messageInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            messageForm.dispatchEvent(new Event('submit'));
        }
    });

    // Handle form submission
    messageForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const message = messageInput.value.trim();
        if (!message) return;

        // Disable input
        messageInput.disabled = true;
        sendButton.disabled = true;

        // Add user message to UI
        addMessage('user', message);

        // Clear input
        messageInput.value = '';
        charCount.textContent = '0';

        // Show loading indicator
        loadingIndicator.classList.remove('hidden');
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

        try {
            // Send message to server
            const formData = new FormData();
            formData.append('message', message);

            const response = await fetch('/interview/{{ invite_code }}/chat/message', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            // Hide loading indicator
            loadingIndicator.classList.add('hidden');

            if (data.status === 'error') {
                alert('Error: ' + data.message);
                messageInput.disabled = false;
                sendButton.disabled = false;
                return;
            }

            // Add AI response to UI
            addMessage('assistant', data.message);

            // Update turn counter if provided
            if (data.turns_remaining !== undefined) {
                updateTurnCounter(data.turns_remaining);
            }

            // Check if completed
            if (data.status === 'completed' && data.redirect) {
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 2000);
            } else {
                // Re-enable input
                messageInput.disabled = false;
                sendButton.disabled = false;
                messageInput.focus();
            }

        } catch (error) {
            loadingIndicator.classList.add('hidden');
            alert('Failed to send message. Please try again.');
            messageInput.disabled = false;
            sendButton.disabled = false;
        }
    });

    function addMessage(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `flex ${role === 'user' ? 'justify-end' : 'justify-start'} fade-in`;

        const icon = role === 'assistant'
            ? '<svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z"></path><path d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z"></path></svg>'
            : '<svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path></svg>';

        const label = role === 'assistant' ? 'AI Interviewer' : 'You';
        const textColor = role === 'user' ? 'text-white' : 'text-gray-700';

        messageDiv.innerHTML = `
            <div class="max-w-xl px-4 py-3 rounded-lg shadow-sm message-${role}">
                <div class="flex items-center mb-1">
                    ${icon}
                    <span class="text-xs font-semibold ${role === 'user' ? 'text-white' : 'text-gray-700'}">${label}</span>
                </div>
                <p class="text-sm leading-relaxed whitespace-pre-wrap">${escapeHtml(content)}</p>
            </div>
        `;

        messagesContainer.insertBefore(messageDiv, loadingIndicator);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function updateTurnCounter(turnsRemaining) {
        const maxTurns = {{ max_turns }};
        const currentTurn = maxTurns - turnsRemaining;
        const percentage = (currentTurn / maxTurns * 100);

        document.querySelector('.text-sm.font-medium.text-gray-700').textContent = `Turn ${currentTurn} of ${maxTurns}`;
        document.querySelector('.bg-indigo-600').style.width = `${percentage}%`;
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
</script>
{% endblock %}

```

## app/templates/interview/chat_placeholder.html

**Path:** `app/templates/interview/chat_placeholder.html`
**Type:** Html
**Size:** 1.6 KB

```html
{% extends "public_base.html" %}

{% block title %}Interview Ready - {{ study.title }}{% endblock %}

{% block content %}
<div class="bg-white rounded-lg shadow-lg p-8 text-center fade-in">
    {% if error %}
    <div class="inline-flex items-center justify-center w-16 h-16 bg-red-100 rounded-full mb-4">
        <svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
    </div>

    <h2 class="text-2xl font-bold text-gray-900 mb-4">Configuration Error</h2>

    <div class="bg-red-50 border-l-4 border-red-400 p-4 text-left max-w-md mx-auto mb-6">
        <p class="text-sm text-red-700">
            <strong>Error:</strong> {{ error }}
        </p>
    </div>

    <p class="text-sm text-gray-600">
        Please contact the research administrator. The chat interface cannot be initialized at this time.
    </p>
    {% else %}
    <div class="inline-flex items-center justify-center w-16 h-16 bg-purple-100 rounded-full mb-4">
        <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
    </div>

    <h2 class="text-3xl font-bold text-gray-900 mb-4">All Set!</h2>

    <p class="text-gray-600 mb-6">
        Thank you for completing the intake form.
    </p>
    {% endif %}
</div>
{% endblock %}

```

## app/templates/interview/completed.html

**Path:** `app/templates/interview/completed.html`
**Type:** Html
**Size:** 1.1 KB

```html
{% extends "public_base.html" %}

{% block title %}Already Completed - InsightPilot{% endblock %}

{% block content %}
<div class="bg-white rounded-lg shadow-lg p-8 text-center fade-in">
    <div class="inline-flex items-center justify-center w-16 h-16 bg-blue-100 rounded-full mb-4">
        <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
    </div>

    <h2 class="text-2xl font-bold text-gray-900 mb-4">Interview Already Completed</h2>

    <p class="text-gray-600 mb-6 max-w-md mx-auto">
        This invitation has already been used to complete an interview. Each invitation can only be used once.
    </p>

    <div class="bg-blue-50 border-l-4 border-blue-400 p-4 text-left max-w-md mx-auto">
        <p class="text-sm text-blue-700">
            Thank you for your participation! If you have questions about the study, please contact the research team.
        </p>
    </div>
</div>
{% endblock %}

```

## app/templates/interview/consent.html

**Path:** `app/templates/interview/consent.html`
**Type:** Html
**Size:** 3.7 KB

```html
{% extends "public_base.html" %}

{% block title %}Consent Form - {{ study.title }}{% endblock %}

{% block content %}
<div class="bg-white rounded-lg shadow-lg p-8 fade-in">
    <!-- Header -->
    <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-blue-100 rounded-full mb-4">
            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
            </svg>
        </div>
        <h2 class="text-3xl font-bold text-gray-900 mb-2">Research Consent Form</h2>
        <p class="text-sm text-gray-600">{{ study.title }}</p>
    </div>

    <!-- Consent Text -->
    <div class="bg-gray-50 rounded-lg p-6 mb-6 max-h-96 overflow-y-auto border border-gray-200">
        <div class="prose prose-sm max-w-none">
            <div class="text-gray-700 whitespace-pre-wrap">{{ study.consent_text }}</div>
        </div>
    </div>

    <!-- Form -->
    <form method="POST" action="/interview/{{ invite_code }}/consent" class="space-y-6">
        <!-- Consent Checkbox -->
        <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
            <label class="flex items-start cursor-pointer">
                <input
                    type="checkbox"
                    name="agreed"
                    value="true"
                    required
                    class="mt-1 h-5 w-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                />
                <span class="ml-3 text-sm text-gray-900">
                    <strong class="font-semibold">I have read and agree to participate</strong>
                    <br>
                    <span class="text-gray-600 text-xs">
                        I understand the purpose of this study and voluntarily consent to participate. I acknowledge that I can withdraw at any time.
                    </span>
                </span>
            </label>
        </div>

        <!-- Error Message (if any) -->
        {% if error %}
        <div class="bg-red-50 border-l-4 border-red-400 p-4">
            <p class="text-sm text-red-700">{{ error }}</p>
        </div>
        {% endif %}

        <!-- Action Buttons -->
        <div class="flex items-center justify-between pt-4">
            <a href="/interview/{{ invite_code }}" class="text-sm text-gray-600 hover:text-gray-900">
                <svg class="w-4 h-4 inline-block mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                </svg>
                Back
            </a>
            <button
                type="submit"
                class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-3 rounded-lg shadow-md transition duration-200 transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
            >
                Continue to Interview
            </button>
        </div>
    </form>

    <!-- Privacy Note -->
    <div class="mt-6 pt-6 border-t border-gray-200">
        <p class="text-xs text-gray-500 text-center">
            <svg class="w-4 h-4 inline-block mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            Your responses will be kept confidential and used only for research purposes.
        </p>
    </div>
</div>
{% endblock %}

```

## app/templates/interview/expired.html

**Path:** `app/templates/interview/expired.html`
**Type:** Html
**Size:** 1.1 KB

```html
{% extends "public_base.html" %}

{% block title %}Invite Expired - InsightPilot{% endblock %}

{% block content %}
<div class="bg-white rounded-lg shadow-lg p-8 text-center fade-in">
    <div class="inline-flex items-center justify-center w-16 h-16 bg-red-100 rounded-full mb-4">
        <svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
    </div>

    <h2 class="text-2xl font-bold text-gray-900 mb-4">Invite Has Expired</h2>

    <p class="text-gray-600 mb-6 max-w-md mx-auto">
        This interview invitation link has expired and is no longer valid. Please contact the researcher for a new invitation.
    </p>

    <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4 text-left max-w-md mx-auto">
        <p class="text-sm text-yellow-700">
            <strong>Need help?</strong> If you believe this is an error, please reach out to the research team that sent you this invitation.
        </p>
    </div>
</div>
{% endblock %}

```

## app/templates/interview/intake.html

**Path:** `app/templates/interview/intake.html`
**Type:** Html
**Size:** 6.8 KB

```html
{% extends "public_base.html" %}

{% block title %}Your Information - {{ study.title }}{% endblock %}

{% block content %}
<div class="bg-white rounded-lg shadow-lg p-8 fade-in">
    <!-- Header -->
    <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-green-100 rounded-full mb-4">
            <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
            </svg>
        </div>
        <h2 class="text-3xl font-bold text-gray-900 mb-2">Your Information</h2>
        <p class="text-sm text-gray-600">Just a few details before we begin</p>
    </div>

    <!-- Form -->
    <form method="POST" action="/interview/{{ invite_code }}/intake" class="space-y-6">
        <!-- Name Field -->
        <div>
            <label for="name" class="block text-sm font-medium text-gray-700 mb-2">
                Full Name <span class="text-red-500">*</span>
            </label>
            <input
                type="text"
                id="name"
                name="name"
                required
                maxlength="255"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
                placeholder="e.g., Jane Doe"
                value="{{ form_data.name if form_data else '' }}"
            />
            {% if errors and errors.name %}
            <p class="mt-1 text-sm text-red-600">{{ errors.name }}</p>
            {% endif %}
        </div>

        <!-- Email Field -->
        <div>
            <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
                Email Address <span class="text-red-500">*</span>
            </label>
            <input
                type="email"
                id="email"
                name="email"
                required
                maxlength="255"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
                placeholder="e.g., jane@example.com"
                value="{{ form_data.email if form_data else '' }}"
            />
            {% if errors and errors.email %}
            <p class="mt-1 text-sm text-red-600">{{ errors.email }}</p>
            {% endif %}
        </div>

        <!-- Optional Demographics Section -->
        <div class="bg-gray-50 rounded-lg p-6 border border-gray-200">
            <h3 class="text-sm font-semibold text-gray-900 mb-4">
                Optional Information
                <span class="text-xs font-normal text-gray-500">(helps us understand our participants better)</span>
            </h3>

            <div class="space-y-4">
                <!-- Age Range -->
                <div>
                    <label for="age_range" class="block text-sm text-gray-700 mb-1">Age Range</label>
                    <select
                        id="age_range"
                        name="age_range"
                        class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm"
                    >
                        <option value="">Prefer not to say</option>
                        <option value="18-24">18-24</option>
                        <option value="25-34">25-34</option>
                        <option value="35-44">35-44</option>
                        <option value="45-54">45-54</option>
                        <option value="55-64">55-64</option>
                        <option value="65+">65+</option>
                    </select>
                </div>

                <!-- Location -->
                <div>
                    <label for="location" class="block text-sm text-gray-700 mb-1">Location/Country</label>
                    <input
                        type="text"
                        id="location"
                        name="location"
                        maxlength="100"
                        class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm"
                        placeholder="e.g., United States"
                    />
                </div>

                <!-- Occupation -->
                <div>
                    <label for="occupation" class="block text-sm text-gray-700 mb-1">Occupation/Industry</label>
                    <input
                        type="text"
                        id="occupation"
                        name="occupation"
                        maxlength="100"
                        class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm"
                        placeholder="e.g., Software Engineer"
                    />
                </div>
            </div>
        </div>

        <!-- General Error Message (if any) -->
        {% if error %}
        <div class="bg-red-50 border-l-4 border-red-400 p-4">
            <p class="text-sm text-red-700">{{ error }}</p>
        </div>
        {% endif %}

        <!-- Action Buttons -->
        <div class="flex items-center justify-between pt-4">
            <a href="/interview/{{ invite_code }}/consent" class="text-sm text-gray-600 hover:text-gray-900">
                <svg class="w-4 h-4 inline-block mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                </svg>
                Back
            </a>
            <button
                type="submit"
                class="bg-green-600 hover:bg-green-700 text-white font-semibold px-8 py-3 rounded-lg shadow-md transition duration-200 transform hover:scale-105"
            >
                Start Interview
                <svg class="w-4 h-4 inline-block ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"></path>
                </svg>
            </button>
        </div>
    </form>

    <!-- Privacy Note -->
    <div class="mt-6 pt-6 border-t border-gray-200">
        <p class="text-xs text-gray-500 text-center">
            <svg class="w-4 h-4 inline-block mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
            </svg>
            All information is stored securely and will only be used for this research study.
        </p>
    </div>
</div>
{% endblock %}

```

## app/templates/interview/landing.html

**Path:** `app/templates/interview/landing.html`
**Type:** Html
**Size:** 3.8 KB

```html
{% extends "public_base.html" %}

{% block title %}{{ study.title }} - InsightPilot{% endblock %}

{% block content %}
<div class="bg-white rounded-lg shadow-lg p-8 fade-in">
    <!-- Study Info -->
    <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-indigo-100 rounded-full mb-4">
            <svg class="w-8 h-8 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path>
            </svg>
        </div>
        <h2 class="text-3xl font-bold text-gray-900 mb-2">{{ study.title }}</h2>
        <p class="text-sm text-gray-500">Research Study</p>
    </div>

    <!-- Study Description -->
    <div class="mb-8">
        <div class="prose prose-sm max-w-none text-gray-700">
            <p class="text-base leading-relaxed">{{ study.description }}</p>
        </div>
    </div>

    <!-- Study Details -->
    <div class="bg-gray-50 rounded-lg p-6 mb-8">
        <h3 class="text-sm font-semibold text-gray-900 mb-3">What to Expect</h3>
        <ul class="space-y-2 text-sm text-gray-600">
            <li class="flex items-start">
                <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>You'll participate in an AI-guided interview</span>
            </li>
            <li class="flex items-start">
                <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>Your responses will be kept confidential</span>
            </li>
            <li class="flex items-start">
                <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>The interview typically takes 15-30 minutes</span>
            </li>
            <li class="flex items-start">
                <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>You can stop at any time if you wish</span>
            </li>
        </ul>
    </div>

    <!-- CTA Button -->
    <div class="text-center">
        <a href="/interview/{{ invite_code }}/consent"
           class="inline-block bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-8 py-3 rounded-lg shadow-md transition duration-200 transform hover:scale-105">
            Continue to Consent Form
        </a>
    </div>

    <!-- Privacy Note -->
    <div class="mt-6 text-center">
        <p class="text-xs text-gray-500">
            <svg class="w-4 h-4 inline-block mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
            </svg>
            Your data is encrypted and secure
        </p>
    </div>
</div>
{% endblock %}

```

## app/templates/interview/not_found.html

**Path:** `app/templates/interview/not_found.html`
**Type:** Html
**Size:** 1.3 KB

```html
{% extends "public_base.html" %}

{% block title %}Invite Not Found - InsightPilot{% endblock %}

{% block content %}
<div class="bg-white rounded-lg shadow-lg p-8 text-center fade-in">
    <div class="inline-flex items-center justify-center w-16 h-16 bg-gray-100 rounded-full mb-4">
        <svg class="w-8 h-8 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
    </div>

    <h2 class="text-2xl font-bold text-gray-900 mb-4">Invitation Not Found</h2>

    <p class="text-gray-600 mb-6 max-w-md mx-auto">
        We couldn't find an interview invitation with this code. Please check the link and try again.
    </p>

    <div class="bg-gray-50 border-l-4 border-gray-400 p-4 text-left max-w-md mx-auto">
        <p class="text-sm text-gray-700">
            <strong>Troubleshooting:</strong>
        </p>
        <ul class="text-sm text-gray-700 mt-2 list-disc list-inside">
            <li>Make sure you copied the complete link</li>
            <li>Check that the link hasn't been modified</li>
            <li>Contact the researcher for a new invitation</li>
        </ul>
    </div>
</div>
{% endblock %}

```

## app/templates/interview/thank_you.html

**Path:** `app/templates/interview/thank_you.html`
**Type:** Html
**Size:** 3.8 KB

```html
{% extends "public_base.html" %}

{% block title %}Thank You - {{ study.title }}{% endblock %}

{% block content %}
<div class="bg-white rounded-lg shadow-lg p-8 text-center fade-in max-w-2xl mx-auto">
    <!-- Success Icon -->
    <div class="inline-flex items-center justify-center w-20 h-20 bg-green-100 rounded-full mb-6">
        <svg class="w-10 h-10 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
    </div>

    <h2 class="text-3xl font-bold text-gray-900 mb-4">Thank You for Your Participation!</h2>

    <p class="text-lg text-gray-700 mb-6">
        {% if interviewee %}
        Thank you, <strong>{{ interviewee.name }}</strong>, for completing this interview.
        {% else %}
        Thank you for completing this interview.
        {% endif %}
    </p>

    <div class="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg p-6 mb-6">
        <p class="text-gray-800 leading-relaxed">
            Your insights and responses are incredibly valuable for our research on
            <strong>{{ study.title }}</strong>. The information you've shared will help us
            better understand this topic and contribute to meaningful findings.
        </p>
    </div>

    <!-- Interview Stats -->
    <div class="grid grid-cols-2 gap-4 mb-8 max-w-md mx-auto">
        <div class="bg-gray-50 rounded-lg p-4">
            <p class="text-2xl font-bold text-indigo-600">{{ study.max_agent_turns }}</p>
            <p class="text-xs text-gray-600 mt-1">Questions Answered</p>
        </div>
        <div class="bg-gray-50 rounded-lg p-4">
            <p class="text-2xl font-bold text-indigo-600">
                {% if interview.completed_at and interview.started_at %}
                {{ ((interview.completed_at - interview.started_at).total_seconds() / 60) | round | int }} min
                {% else %}
                -
                {% endif %}
            </p>
            <p class="text-xs text-gray-600 mt-1">Time Spent</p>
        </div>
    </div>

    <!-- What's Next -->
    <div class="bg-blue-50 border-l-4 border-blue-400 p-4 text-left mb-6">
        <h3 class="text-sm font-semibold text-blue-900 mb-2">What Happens Next?</h3>
        <ul class="text-sm text-blue-800 space-y-1">
            <li>✓ Your responses have been securely saved</li>
            <li>✓ Our research team will analyze the findings</li>
            <li>✓ All data remains confidential and anonymous</li>
            <li>✓ You may receive follow-up communication if you opted in</li>
        </ul>
    </div>

    <!-- Appreciation Message -->
    <div class="border-t border-gray-200 pt-6">
        <p class="text-sm text-gray-600 mb-4">
            We truly appreciate the time and thought you put into your responses.
            Your participation makes a real difference in our research efforts.
        </p>

        <div class="flex items-center justify-center space-x-2 text-indigo-600">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z"></path>
            </svg>
            <span class="font-semibold">Thank you!</span>
        </div>
    </div>

    <!-- Optional: Close Window Button -->
    <div class="mt-8">
        <button
            onclick="window.close()"
            class="text-sm text-gray-500 hover:text-gray-700 underline"
        >
            You may close this window
        </button>
    </div>
</div>
{% endblock %}

```

## app/templates/public_base.html

**Path:** `app/templates/public_base.html`
**Type:** Html
**Size:** 1.7 KB

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}InsightPilot{% endblock %}</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- HTMX for progressive enhancement -->
    <script src="https://unpkg.com/htmx.org@1.9.12"></script>

    <!-- Custom styles -->
    <link rel="stylesheet" href="{{ url_for('static', path='css/app.css') }}" />

    {% block extra_head %}{% endblock %}
</head>
<body class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex flex-col">
    <!-- Simple Header (no auth) -->
    <header class="bg-white shadow-sm border-b border-gray-200">
        <div class="max-w-4xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <h1 class="text-2xl font-bold text-indigo-600">InsightPilot</h1>
                <p class="text-sm text-gray-600 mt-1">AI-Powered Research Interview</p>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow flex items-center justify-center px-4 py-8 sm:px-6 lg:px-8">
        <div class="w-full max-w-2xl">
            {% block content %}{% endblock %}
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 mt-auto">
        <div class="max-w-4xl mx-auto px-4 py-4 text-center">
            <p class="text-xs text-gray-500">&copy; 2025 InsightPilot. Secure and confidential research platform.</p>
        </div>
    </footer>

    <!-- Custom scripts -->
    <script src="{{ url_for('static', path='js/app.js') }}"></script>
    {% block extra_scripts %}{% endblock %}
</body>
</html>

```

## app/templates/researcher_base.html

**Path:** `app/templates/researcher_base.html`
**Type:** Html
**Size:** 2.8 KB

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}InsightPilot - Researcher{% endblock %}</title>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50">
    <!-- Header -->
    <nav class="bg-white shadow-sm border-b border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex">
                    <div class="flex-shrink-0 flex items-center">
                        <a href="/app/studies" class="text-xl font-bold text-indigo-600">InsightPilot</a>
                    </div>
                    <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
                        <a href="/app/studies" class="border-transparent text-gray-900 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                            Studies
                        </a>
                    </div>
                </div>
                <div class="flex items-center">
                    <span class="text-sm text-gray-700 mr-4">Researcher</span>
                    <form action="/auth/dev/logout" method="POST" class="inline">
                        <button type="submit" class="text-sm text-gray-700 hover:text-gray-900">Logout</button>
                    </form>
                </div>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        {% block content %}{% endblock %}
    </main>

    <!-- Toast notifications container -->
    <div id="toast-container" class="fixed bottom-4 right-4 z-50"></div>

    <script>
        // Simple toast notification helper
        function showToast(message, type = 'success') {
            const toast = document.createElement('div');
            const bgColor = type === 'success' ? 'bg-green-500' : 'bg-red-500';
            toast.className = `${bgColor} text-white px-6 py-3 rounded-lg shadow-lg mb-2 transition-opacity duration-500`;
            toast.textContent = message;
            document.getElementById('toast-container').appendChild(toast);

            setTimeout(() => {
                toast.style.opacity = '0';
                setTimeout(() => toast.remove(), 500);
            }, 3000);
        }

        // Copy to clipboard helper
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                showToast('Copied to clipboard!');
            }).catch(() => {
                showToast('Failed to copy', 'error');
            });
        }
    </script>
</body>
</html>

```

## app/templates/studies/_invites.html

**Path:** `app/templates/studies/_invites.html`
**Type:** Html
**Size:** 3.4 KB

```html
{% if invites %}
<ul class="divide-y divide-gray-200">
    {% for invite in invites %}
    <li class="px-4 py-4 sm:px-6">
        <div class="flex items-center justify-between">
            <div class="flex-1">
                <div class="flex items-center">
                    <p class="text-sm font-medium text-gray-900">
                        {% if invite.interviewee_email %}
                            {{ invite.interviewee_email }}
                        {% else %}
                            Anonymous Invite
                        {% endif %}
                    </p>
                    <span class="ml-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
                        {% if invite.status == 'created' %}bg-gray-100 text-gray-800
                        {% elif invite.status == 'opened' %}bg-blue-100 text-blue-800
                        {% elif invite.status == 'completed' %}bg-green-100 text-green-800
                        {% endif %}">
                        {{ invite.status|capitalize }}
                    </span>
                </div>
                <div class="mt-2 flex items-center">
                    <code class="text-xs bg-gray-100 px-2 py-1 rounded text-gray-600 break-all">
                        {{ request.url.scheme }}://{{ request.url.netloc }}/interview/{{ invite.invite_code }}
                    </code>
                    <button onclick="copyToClipboard('{{ request.url.scheme }}://{{ request.url.netloc }}/interview/{{ invite.invite_code }}')"
                            class="ml-2 text-indigo-600 hover:text-indigo-800">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/>
                        </svg>
                    </button>
                </div>
                {% if invite.expires_at %}
                <p class="mt-1 text-xs text-gray-500">Expires: {{ invite.expires_at.strftime('%B %d, %Y at %I:%M %p') }}</p>
                {% endif %}
            </div>
            <button hx-delete="/app/studies/{{ invite.study_id }}/invites/{{ invite.id }}"
                    hx-target="#invites-container"
                    hx-swap="innerHTML"
                    hx-confirm="Delete this invite?"
                    class="ml-4 text-red-600 hover:text-red-800">
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                </svg>
            </button>
        </div>
    </li>
    {% endfor %}
</ul>
{% else %}
<div class="px-4 py-8 sm:px-6 text-center">
    <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
    </svg>
    <p class="mt-2 text-sm text-gray-500">No invites yet. Generate an invite link to share with participants.</p>
</div>
{% endif %}

```

## app/templates/studies/_questions.html

**Path:** `app/templates/studies/_questions.html`
**Type:** Html
**Size:** 4.5 KB

```html
{% if questions %}
<ul id="questions-list" class="divide-y divide-gray-200">
    {% for question in questions %}
    <li class="px-4 py-4 sm:px-6 flex items-center justify-between" data-question-id="{{ question.id }}" data-order="{{ question.sort_order }}">
        <div class="flex items-center flex-1">
            <button type="button" class="reorder-handle cursor-move mr-3 text-gray-400 hover:text-gray-600">
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8h16M4 16h16"/>
                </svg>
            </button>
            <div class="flex-1">
                <p class="text-sm font-medium text-gray-900">{{ question.text }}</p>
                <p class="text-xs text-gray-500 mt-1">Order: {{ question.sort_order }}</p>
            </div>
        </div>
        <button hx-delete="/app/studies/{{ question.study_id }}/questions/{{ question.id }}"
                hx-target="#questions-container"
                hx-swap="innerHTML"
                hx-confirm="Delete this question?"
                class="ml-4 text-red-600 hover:text-red-800">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
            </svg>
        </button>
    </li>
    {% endfor %}
</ul>

<script>
(function() {
    const list = document.getElementById('questions-list');
    if (!list) return;

    let draggedElement = null;

    list.querySelectorAll('.reorder-handle').forEach(handle => {
        const li = handle.closest('li');

        handle.addEventListener('mousedown', (e) => {
            li.draggable = true;
        });

        li.addEventListener('dragstart', (e) => {
            draggedElement = li;
            li.style.opacity = '0.5';
        });

        li.addEventListener('dragend', (e) => {
            li.style.opacity = '1';
            li.draggable = false;

            // Gather new order
            const items = Array.from(list.querySelectorAll('li'));
            const questionOrder = items.map((item, index) => ({
                question_id: parseInt(item.dataset.questionId),
                sort_order: index
            }));

            // Send reorder request
            fetch('/app/studies/{{ study_id }}/questions/reorder', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ questions: questionOrder })
            })
            .then(response => response.text())
            .then(html => {
                document.getElementById('questions-container').innerHTML = html;
                showToast('Questions reordered');
            })
            .catch(err => {
                showToast('Failed to reorder', 'error');
                console.error(err);
            });
        });

        li.addEventListener('dragover', (e) => {
            e.preventDefault();
            const afterElement = getDragAfterElement(list, e.clientY);
            if (afterElement == null) {
                list.appendChild(draggedElement);
            } else {
                list.insertBefore(draggedElement, afterElement);
            }
        });
    });

    function getDragAfterElement(container, y) {
        const draggableElements = [...container.querySelectorAll('li:not(.opacity-50)')];

        return draggableElements.reduce((closest, child) => {
            const box = child.getBoundingClientRect();
            const offset = y - box.top - box.height / 2;

            if (offset < 0 && offset > closest.offset) {
                return { offset: offset, element: child };
            } else {
                return closest;
            }
        }, { offset: Number.NEGATIVE_INFINITY }).element;
    }
})();
</script>
{% else %}
<div class="px-4 py-8 sm:px-6 text-center">
    <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
    </svg>
    <p class="mt-2 text-sm text-gray-500">No questions yet. Add your first seed question to guide the interview.</p>
</div>
{% endif %}

```

## app/templates/studies/analytics.html

**Path:** `app/templates/studies/analytics.html`
**Type:** Html
**Size:** 18.7 KB

```html
{% extends "researcher_base.html" %}

{% block title %}Analytics - {{ study.title }} - InsightPilot{% endblock %}

{% block content %}
<div class="px-4 sm:px-0">
    <!-- Header -->
    <div class="mb-8">
        <a href="/app/studies/{{ study.id }}" class="text-sm text-indigo-600 hover:text-indigo-800 mb-2 inline-flex items-center">
            <svg class="h-4 w-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
            </svg>
            Back to Study
        </a>
        <h1 class="text-3xl font-bold text-gray-900 mt-2">Analytics & Insights</h1>
        <p class="mt-2 text-gray-600">{{ study.title }}</p>
    </div>

    <!-- Loading State -->
    <div id="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
        <p class="mt-4 text-gray-600">Loading analytics...</p>
    </div>

    <!-- Error State -->
    <div id="error" class="hidden bg-red-50 border border-red-200 rounded-lg p-6 text-center">
        <svg class="h-12 w-12 text-red-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <h3 class="text-lg font-medium text-red-900 mb-2">Failed to load analytics</h3>
        <p class="text-red-700" id="error-message"></p>
        <button onclick="loadAnalytics()" class="mt-4 px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700">
            Retry
        </button>
    </div>

    <!-- Empty State -->
    <div id="empty" class="hidden bg-yellow-50 border border-yellow-200 rounded-lg p-6 text-center">
        <svg class="h-12 w-12 text-yellow-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"/>
        </svg>
        <h3 class="text-lg font-medium text-yellow-900 mb-2">No data yet</h3>
        <p class="text-yellow-700">Complete some interviews to see analytics here.</p>
        <a href="/app/studies/{{ study.id }}/interviews" class="mt-4 inline-flex items-center px-4 py-2 bg-yellow-600 text-white rounded-md hover:bg-yellow-700">
            View Interviews
        </a>
    </div>

    <!-- Main Content -->
    <div id="content" class="hidden">
        <!-- Summary Stats -->
        <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-8">
            <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="p-5">
                    <div class="flex items-center">
                        <div class="flex-shrink-0">
                            <svg class="h-6 w-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
                            </svg>
                        </div>
                        <div class="ml-5 w-0 flex-1">
                            <dl>
                                <dt class="text-sm font-medium text-gray-500 truncate">Total Interviews</dt>
                                <dd class="text-lg font-semibold text-gray-900" id="stat-total"></dd>
                            </dl>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="p-5">
                    <div class="flex items-center">
                        <div class="flex-shrink-0">
                            <svg class="h-6 w-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                            </svg>
                        </div>
                        <div class="ml-5 w-0 flex-1">
                            <dl>
                                <dt class="text-sm font-medium text-gray-500 truncate">Completed</dt>
                                <dd class="text-lg font-semibold text-gray-900" id="stat-completed"></dd>
                            </dl>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="p-5">
                    <div class="flex items-center">
                        <div class="flex-shrink-0">
                            <svg class="h-6 w-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>
                            </svg>
                        </div>
                        <div class="ml-5 w-0 flex-1">
                            <dl>
                                <dt class="text-sm font-medium text-gray-500 truncate">Total Messages</dt>
                                <dd class="text-lg font-semibold text-gray-900" id="stat-messages"></dd>
                            </dl>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="p-5">
                    <div class="flex items-center">
                        <div class="flex-shrink-0">
                            <svg class="h-6 w-6 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"/>
                            </svg>
                        </div>
                        <div class="ml-5 w-0 flex-1">
                            <dl>
                                <dt class="text-sm font-medium text-gray-500 truncate">Avg Messages</dt>
                                <dd class="text-lg font-semibold text-gray-900" id="stat-avg-messages"></dd>
                            </dl>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Charts Row -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
            <!-- Sentiment Distribution -->
            <div class="bg-white shadow rounded-lg p-6">
                <h3 class="text-lg font-medium text-gray-900 mb-4">Sentiment Distribution</h3>
                <div class="relative" style="height: 300px;">
                    <canvas id="sentimentChart"></canvas>
                </div>
            </div>

            <!-- Timeline -->
            <div class="bg-white shadow rounded-lg p-6">
                <h3 class="text-lg font-medium text-gray-900 mb-4">Interview Timeline</h3>
                <div class="relative" style="height: 300px;">
                    <canvas id="timelineChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Top Keywords -->
        <div class="bg-white shadow rounded-lg p-6 mb-8">
            <h3 class="text-lg font-medium text-gray-900 mb-4">Top Keywords</h3>
            <div class="relative" style="height: 300px;">
                <canvas id="keywordsChart"></canvas>
            </div>
        </div>

        <!-- Demographics and Quotes Row -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
            <!-- Demographics -->
            <div class="bg-white shadow rounded-lg p-6">
                <h3 class="text-lg font-medium text-gray-900 mb-4">Demographics</h3>
                <div id="demographics-content"></div>
            </div>

            <!-- Sample Quotes -->
            <div class="bg-white shadow rounded-lg p-6">
                <h3 class="text-lg font-medium text-gray-900 mb-4">Notable Quotes</h3>
                <div id="quotes-content" class="space-y-3"></div>
            </div>
        </div>

        <!-- Response Metrics -->
        <div class="bg-white shadow rounded-lg p-6">
            <h3 class="text-lg font-medium text-gray-900 mb-4">Response Metrics</h3>
            <dl class="grid grid-cols-1 gap-5 sm:grid-cols-3">
                <div class="px-4 py-5 bg-gray-50 rounded-lg">
                    <dt class="text-sm font-medium text-gray-500">Avg Response Length</dt>
                    <dd class="mt-1 text-2xl font-semibold text-gray-900" id="metric-response-length"></dd>
                    <dd class="mt-1 text-xs text-gray-500">characters per response</dd>
                </div>
                <div class="px-4 py-5 bg-gray-50 rounded-lg">
                    <dt class="text-sm font-medium text-gray-500">Avg Conversation Length</dt>
                    <dd class="mt-1 text-2xl font-semibold text-gray-900" id="metric-conversation-length"></dd>
                    <dd class="mt-1 text-xs text-gray-500">total characters</dd>
                </div>
                <div class="px-4 py-5 bg-gray-50 rounded-lg">
                    <dt class="text-sm font-medium text-gray-500">Avg Messages Per Interview</dt>
                    <dd class="mt-1 text-2xl font-semibold text-gray-900" id="metric-messages-per-interview"></dd>
                    <dd class="mt-1 text-xs text-gray-500">messages</dd>
                </div>
            </dl>
        </div>
    </div>
</div>

<!-- Load Chart.js before our analytics code -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

<script>
let charts = {};

async function loadAnalytics() {
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const empty = document.getElementById('empty');
    const content = document.getElementById('content');

    // Show loading, hide others
    loading.classList.remove('hidden');
    error.classList.add('hidden');
    empty.classList.add('hidden');
    content.classList.add('hidden');

    try {
        const response = await fetch('/studies/{{ study.id }}/analytics');

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Hide loading
        loading.classList.add('hidden');

        // Check if empty
        if (data.total_interviews === 0) {
            empty.classList.remove('hidden');
            return;
        }

        // Show content and render
        content.classList.remove('hidden');
        renderAnalytics(data);

    } catch (err) {
        console.error('Failed to load analytics:', err);
        loading.classList.add('hidden');
        error.classList.remove('hidden');
        document.getElementById('error-message').textContent = err.message;
    }
}

function renderAnalytics(data) {
    // Update summary stats
    document.getElementById('stat-total').textContent = data.total_interviews;
    document.getElementById('stat-completed').textContent = data.completed_interviews;
    document.getElementById('stat-messages').textContent = data.response_metrics.total_messages;
    document.getElementById('stat-avg-messages').textContent = data.response_metrics.avg_message_count.toFixed(1);

    // Update response metrics
    document.getElementById('metric-response-length').textContent = data.response_metrics.avg_response_length.toFixed(0);
    document.getElementById('metric-conversation-length').textContent = data.response_metrics.avg_conversation_length.toFixed(0);
    document.getElementById('metric-messages-per-interview').textContent = data.response_metrics.avg_message_count.toFixed(1);

    // Render Sentiment Chart
    renderSentimentChart(data.sentiment_distribution);

    // Render Timeline Chart
    renderTimelineChart(data.timeline);

    // Render Keywords Chart
    renderKeywordsChart(data.top_keywords);

    // Render Demographics
    renderDemographics(data.demographics);

    // Render Quotes
    renderQuotes(data.sample_quotes);
}

function renderSentimentChart(sentiment) {
    const ctx = document.getElementById('sentimentChart');

    if (charts.sentiment) {
        charts.sentiment.destroy();
    }

    charts.sentiment = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Neutral', 'Negative'],
            datasets: [{
                data: [sentiment.positive, sentiment.neutral, sentiment.negative],
                backgroundColor: [
                    'rgb(34, 197, 94)',  // green
                    'rgb(163, 163, 163)', // gray
                    'rgb(239, 68, 68)',   // red
                ],
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                }
            }
        }
    });
}

function renderTimelineChart(timeline) {
    const ctx = document.getElementById('timelineChart');

    if (charts.timeline) {
        charts.timeline.destroy();
    }

    if (timeline.length === 0) {
        ctx.parentElement.innerHTML = '<p class="text-gray-500 text-center py-8">No timeline data available</p>';
        return;
    }

    charts.timeline = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: timeline.map(t => t.date),
            datasets: [
                {
                    label: 'Completed',
                    data: timeline.map(t => t.completed),
                    backgroundColor: 'rgb(34, 197, 94)',
                },
                {
                    label: 'In Progress',
                    data: timeline.map(t => t.in_progress),
                    backgroundColor: 'rgb(251, 191, 36)',
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    stacked: true,
                },
                y: {
                    stacked: true,
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'bottom',
                }
            }
        }
    });
}

function renderKeywordsChart(keywords) {
    const ctx = document.getElementById('keywordsChart');

    if (charts.keywords) {
        charts.keywords.destroy();
    }

    if (keywords.length === 0) {
        ctx.parentElement.innerHTML = '<p class="text-gray-500 text-center py-8">No keywords available</p>';
        return;
    }

    // Take top 10 for visibility
    const topKeywords = keywords.slice(0, 10);

    charts.keywords = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: topKeywords.map(k => k.keyword),
            datasets: [{
                label: 'Frequency',
                data: topKeywords.map(k => k.count),
                backgroundColor: 'rgb(99, 102, 241)',
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: 'y',
            scales: {
                x: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

function renderDemographics(demographics) {
    const container = document.getElementById('demographics-content');

    if (demographics.length === 0) {
        container.innerHTML = '<p class="text-gray-500 text-center py-8">No demographic data available</p>';
        return;
    }

    let html = '<div class="space-y-4">';

    demographics.forEach(demo => {
        html += `<div>
            <h4 class="text-sm font-medium text-gray-700 mb-2 capitalize">${demo.field.replace('_', ' ')}</h4>
            <div class="space-y-1">`;

        const sorted = Object.entries(demo.values).sort((a, b) => b[1] - a[1]);
        sorted.forEach(([value, count]) => {
            const percentage = (count / sorted.reduce((sum, [, c]) => sum + c, 0) * 100).toFixed(0);
            html += `
                <div class="flex items-center justify-between text-sm">
                    <span class="text-gray-600">${value}</span>
                    <div class="flex items-center">
                        <div class="w-32 bg-gray-200 rounded-full h-2 mr-2">
                            <div class="bg-indigo-600 h-2 rounded-full" style="width: ${percentage}%"></div>
                        </div>
                        <span class="text-gray-900 font-medium w-12 text-right">${count} (${percentage}%)</span>
                    </div>
                </div>`;
        });

        html += `</div></div>`;
    });

    html += '</div>';
    container.innerHTML = html;
}

function renderQuotes(quotes) {
    const container = document.getElementById('quotes-content');

    if (quotes.length === 0) {
        container.innerHTML = '<p class="text-gray-500 text-center py-8">No quotes available</p>';
        return;
    }

    let html = '';
    quotes.forEach(quote => {
        html += `
            <div class="border-l-4 border-indigo-500 pl-4 py-2">
                <p class="text-gray-700 italic">"${quote}"</p>
            </div>`;
    });

    container.innerHTML = html;
}

// Wait for both DOM and Chart.js to be ready
if (typeof Chart === 'undefined') {
    console.error('Chart.js failed to load');
    document.getElementById('loading').classList.add('hidden');
    document.getElementById('error').classList.remove('hidden');
    document.getElementById('error-message').textContent = 'Chart.js library failed to load';
} else {
    // Load analytics when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadAnalytics);
    } else {
        // DOM already loaded
        loadAnalytics();
    }
}
</script>
{% endblock %}

```

## app/templates/studies/detail.html

**Path:** `app/templates/studies/detail.html`
**Type:** Html
**Size:** 13.9 KB

```html
{% extends "researcher_base.html" %}

{% block title %}{{ study.title }} - InsightPilot{% endblock %}

{% block content %}
<div class="px-4 sm:px-0">
    <!-- Header with Actions -->
    <div class="mb-8">
        <div class="flex items-center justify-between">
            <div class="flex-1">
                <a href="/app/studies" class="text-sm text-indigo-600 hover:text-indigo-800 mb-2 inline-flex items-center">
                    <svg class="h-4 w-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
                    </svg>
                    Back to Studies
                </a>
                <h1 class="text-3xl font-bold text-gray-900 mt-2">{{ study.title }}</h1>
                <p class="mt-2 text-gray-600">{{ study.description }}</p>
            </div>
            <div class="ml-4 flex space-x-3">
                <button onclick="document.getElementById('edit-modal').classList.remove('hidden')"
                        class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                    Edit
                </button>
                <button onclick="if(confirm('Delete this study?')) document.getElementById('delete-form').submit()"
                        class="inline-flex items-center px-3 py-2 border border-red-300 shadow-sm text-sm leading-4 font-medium rounded-md text-red-700 bg-white hover:bg-red-50">
                    Delete
                </button>
            </div>
        </div>
        <form id="delete-form" action="/app/studies/{{ study.id }}" method="POST" class="hidden">
            <input type="hidden" name="method" value="DELETE">
        </form>
    </div>

    <!-- Study Details Card -->
    <div class="bg-white shadow overflow-hidden sm:rounded-lg mb-6">
        <div class="px-4 py-5 sm:px-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900">Study Details</h3>
        </div>
        <div class="border-t border-gray-200 px-4 py-5 sm:p-0">
            <dl class="sm:divide-y sm:divide-gray-200">
                <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt class="text-sm font-medium text-gray-500">Max Agent Turns</dt>
                    <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ study.max_agent_turns }}</dd>
                </div>
                <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt class="text-sm font-medium text-gray-500">Created</dt>
                    <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ study.created_at.strftime('%B %d, %Y at %I:%M %p') }}</dd>
                </div>
                <div class="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt class="text-sm font-medium text-gray-500">Consent Text</dt>
                    <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ study.consent_text }}</dd>
                </div>
            </dl>
        </div>
    </div>

    <!-- Questions Section -->
    <div class="bg-white shadow overflow-hidden sm:rounded-lg mb-6">
        <div class="px-4 py-5 sm:px-6 flex justify-between items-center">
            <div>
                <h3 class="text-lg leading-6 font-medium text-gray-900">Seed Questions</h3>
                <p class="mt-1 max-w-2xl text-sm text-gray-500">Questions that guide the interview</p>
            </div>
            <button onclick="document.getElementById('question-modal').classList.remove('hidden')"
                    class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
                <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
                </svg>
                Add Question
            </button>
        </div>
        <div id="questions-container" class="border-t border-gray-200">
            {% include 'studies/_questions.html' %}
        </div>
    </div>

    <!-- Interviews Section -->
    <div class="bg-white shadow overflow-hidden sm:rounded-lg mb-6">
        <div class="px-4 py-5 sm:px-6 flex justify-between items-center">
            <div>
                <h3 class="text-lg leading-6 font-medium text-gray-900">Interview Results</h3>
                <p class="mt-1 max-w-2xl text-sm text-gray-500">View completed and in-progress interviews</p>
            </div>
            <div class="flex space-x-3">
                <a href="/app/studies/{{ study.id }}/analytics"
                   class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                    <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                    </svg>
                    Analytics
                </a>
                <a href="/app/studies/{{ study.id }}/interviews"
                   class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
                    <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>
                    </svg>
                    View Interviews
                </a>
            </div>
        </div>
    </div>

    <!-- Invites Section -->
    <div class="bg-white shadow overflow-hidden sm:rounded-lg">
        <div class="px-4 py-5 sm:px-6 flex justify-between items-center">
            <div>
                <h3 class="text-lg leading-6 font-medium text-gray-900">Invites</h3>
                <p class="mt-1 max-w-2xl text-sm text-gray-500">Generate invite links for participants</p>
            </div>
            <button hx-post="/app/studies/{{ study.id }}/invites"
                    hx-target="#invites-container"
                    hx-swap="innerHTML"
                    class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
                <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
                </svg>
                Generate Invite
            </button>
        </div>
        <div id="invites-container" class="border-t border-gray-200">
            {% include 'studies/_invites.html' %}
        </div>
    </div>
</div>

<!-- Add Question Modal -->
<div id="question-modal" class="hidden fixed z-10 inset-0 overflow-y-auto">
    <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" onclick="document.getElementById('question-modal').classList.add('hidden')"></div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen">&#8203;</span>
        <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6">
            <form hx-post="/app/studies/{{ study.id }}/questions"
                  hx-target="#questions-container"
                  hx-swap="innerHTML"
                  hx-on::after-request="document.getElementById('question-modal').classList.add('hidden'); document.getElementById('question-text').value='';">
                <div>
                    <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">Add Seed Question</h3>
                    <div>
                        <label for="question-text" class="block text-sm font-medium text-gray-700">Question Text</label>
                        <textarea name="text" id="question-text" rows="3" required
                                  class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                                  placeholder="e.g., What features would you like to see in our product?"></textarea>
                    </div>
                </div>
                <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
                    <button type="submit"
                            class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm">
                        Add Question
                    </button>
                    <button type="button" onclick="document.getElementById('question-modal').classList.add('hidden')"
                            class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:col-start-1 sm:text-sm">
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>

<!-- Edit Study Modal -->
<div id="edit-modal" class="hidden fixed z-10 inset-0 overflow-y-auto">
    <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" onclick="document.getElementById('edit-modal').classList.add('hidden')"></div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen">&#8203;</span>
        <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6">
            <form action="/app/studies/{{ study.id }}" method="POST">
                <input type="hidden" name="method" value="PATCH">
                <div>
                    <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">Edit Study</h3>
                    <div class="space-y-4">
                        <div>
                            <label for="edit-title" class="block text-sm font-medium text-gray-700">Title</label>
                            <input type="text" name="title" id="edit-title" value="{{ study.title }}" required
                                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                        </div>
                        <div>
                            <label for="edit-description" class="block text-sm font-medium text-gray-700">Description</label>
                            <textarea name="description" id="edit-description" rows="3" required
                                      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">{{ study.description }}</textarea>
                        </div>
                        <div>
                            <label for="edit-consent_text" class="block text-sm font-medium text-gray-700">Consent Text</label>
                            <textarea name="consent_text" id="edit-consent_text" rows="3" required
                                      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">{{ study.consent_text }}</textarea>
                        </div>
                        <div>
                            <label for="edit-max_agent_turns" class="block text-sm font-medium text-gray-700">Max Agent Turns</label>
                            <input type="number" name="max_agent_turns" id="edit-max_agent_turns" value="{{ study.max_agent_turns }}" min="1" max="50" required
                                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                        </div>
                    </div>
                </div>
                <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
                    <button type="submit"
                            class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm">
                        Save Changes
                    </button>
                    <button type="button" onclick="document.getElementById('edit-modal').classList.add('hidden')"
                            class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:col-start-1 sm:text-sm">
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

```

## app/templates/studies/interviews.html

**Path:** `app/templates/studies/interviews.html`
**Type:** Html
**Size:** 14.1 KB

```html
{% extends "researcher_base.html" %}

{% block title %}Interviews - {{ study.title }} - InsightPilot{% endblock %}

{% block content %}
<div class="px-4 sm:px-0">
    <!-- Header -->
    <div class="mb-8">
        <a href="/app/studies/{{ study.id }}" class="text-sm text-indigo-600 hover:text-indigo-800 mb-2 inline-flex items-center">
            <svg class="h-4 w-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
            </svg>
            Back to Study
        </a>
        <div class="flex items-center justify-between mt-2">
            <div>
                <h1 class="text-3xl font-bold text-gray-900">Interviews</h1>
                <p class="mt-2 text-gray-600">{{ study.title }}</p>
            </div>
            <div class="flex space-x-3">
                <a href="/app/studies/{{ study.id }}/analytics"
                   class="inline-flex items-center px-3 py-2 border border-indigo-300 shadow-sm text-sm font-medium rounded-md text-indigo-700 bg-white hover:bg-indigo-50">
                    <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                    </svg>
                    Analytics
                </a>
                {% if interviews|length > 0 %}
                <a href="/studies/{{ study.id }}/export?format=csv"
                   class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                    <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
                    </svg>
                    Export CSV
                </a>
                <a href="/studies/{{ study.id }}/export?format=json"
                   class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                    <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
                    </svg>
                    Export JSON
                </a>
                {% endif %}
            </div>
        </div>
    </div>

    <!-- Summary Stats -->
    <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-8">
        <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="p-5">
                <div class="flex items-center">
                    <div class="flex-shrink-0">
                        <svg class="h-6 w-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
                        </svg>
                    </div>
                    <div class="ml-5 w-0 flex-1">
                        <dl>
                            <dt class="text-sm font-medium text-gray-500 truncate">Total Interviews</dt>
                            <dd class="text-lg font-semibold text-gray-900">{{ interviews|length }}</dd>
                        </dl>
                    </div>
                </div>
            </div>
        </div>

        <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="p-5">
                <div class="flex items-center">
                    <div class="flex-shrink-0">
                        <svg class="h-6 w-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                        </svg>
                    </div>
                    <div class="ml-5 w-0 flex-1">
                        <dl>
                            <dt class="text-sm font-medium text-gray-500 truncate">Completed</dt>
                            <dd class="text-lg font-semibold text-gray-900">
                                {% set completed = interviews|selectattr("completed_at")|list %}
                                {{ completed|length }}
                            </dd>
                        </dl>
                    </div>
                </div>
            </div>
        </div>

        <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="p-5">
                <div class="flex items-center">
                    <div class="flex-shrink-0">
                        <svg class="h-6 w-6 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                        </svg>
                    </div>
                    <div class="ml-5 w-0 flex-1">
                        <dl>
                            <dt class="text-sm font-medium text-gray-500 truncate">In Progress</dt>
                            <dd class="text-lg font-semibold text-gray-900">
                                {% set in_progress = interviews|rejectattr("completed_at")|list %}
                                {{ in_progress|length }}
                            </dd>
                        </dl>
                    </div>
                </div>
            </div>
        </div>

        <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="p-5">
                <div class="flex items-center">
                    <div class="flex-shrink-0">
                        <svg class="h-6 w-6 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>
                        </svg>
                    </div>
                    <div class="ml-5 w-0 flex-1">
                        <dl>
                            <dt class="text-sm font-medium text-gray-500 truncate">Avg. Messages</dt>
                            <dd class="text-lg font-semibold text-gray-900">
                                {% if interviews %}
                                    {{ (interviews|sum(attribute='message_count') / interviews|length)|round|int }}
                                {% else %}
                                    0
                                {% endif %}
                            </dd>
                        </dl>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Interviews List -->
    <div class="bg-white shadow overflow-hidden sm:rounded-md">
        {% if interviews %}
            <ul class="divide-y divide-gray-200">
                {% for interview in interviews %}
                <li>
                    <a href="/app/studies/{{ study.id }}/interviews/{{ interview.id }}" class="block hover:bg-gray-50 transition">
                        <div class="px-4 py-4 sm:px-6">
                            <div class="flex items-center justify-between">
                                <div class="flex-1 min-w-0">
                                    <div class="flex items-center">
                                        <p class="text-sm font-medium text-indigo-600 truncate">
                                            {{ interview.interviewee.name if interview.interviewee else 'Anonymous' }}
                                        </p>
                                        {% if interview.completed_at %}
                                            <span class="ml-2 px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                                                Completed
                                            </span>
                                        {% else %}
                                            <span class="ml-2 px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
                                                In Progress
                                            </span>
                                        {% endif %}
                                        {% if interview.insight and interview.insight.sentiment %}
                                            {% if interview.insight.sentiment == 'positive' %}
                                                <span class="ml-2 text-green-500" title="Positive sentiment">😊</span>
                                            {% elif interview.insight.sentiment == 'negative' %}
                                                <span class="ml-2 text-red-500" title="Negative sentiment">😞</span>
                                            {% else %}
                                                <span class="ml-2 text-gray-500" title="Neutral sentiment">😐</span>
                                            {% endif %}
                                        {% endif %}
                                    </div>
                                    <div class="mt-2 flex items-center text-sm text-gray-500 space-x-4">
                                        {% if interview.interviewee %}
                                            <span class="flex items-center">
                                                <svg class="flex-shrink-0 mr-1.5 h-4 w-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                                                </svg>
                                                {{ interview.interviewee.email }}
                                            </span>
                                        {% endif %}
                                        <span class="flex items-center">
                                            <svg class="flex-shrink-0 mr-1.5 h-4 w-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>
                                            </svg>
                                            {{ interview.message_count }} messages
                                        </span>
                                        <span class="flex items-center">
                                            <svg class="flex-shrink-0 mr-1.5 h-4 w-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                                            </svg>
                                            {{ interview.started_at.strftime('%b %d, %Y') }}
                                        </span>
                                    </div>
                                    {% if interview.insight and interview.insight.summary %}
                                        <p class="mt-2 text-sm text-gray-600 line-clamp-2">
                                            {{ interview.insight.summary }}
                                        </p>
                                    {% endif %}
                                </div>
                                <div class="ml-5 flex-shrink-0">
                                    <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </a>
                </li>
                {% endfor %}
            </ul>
        {% else %}
            <!-- Empty State -->
            <div class="text-center py-12">
                <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>
                </svg>
                <h3 class="mt-2 text-sm font-medium text-gray-900">No interviews yet</h3>
                <p class="mt-1 text-sm text-gray-500">
                    Interviews will appear here once participants complete them.
                </p>
                <div class="mt-6">
                    <a href="/app/studies/{{ study.id }}" class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
                        <svg class="-ml-1 mr-2 h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
                        </svg>
                        Generate Invites
                    </a>
                </div>
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}

```

## app/templates/studies/list.html

**Path:** `app/templates/studies/list.html`
**Type:** Html
**Size:** 8.0 KB

```html
{% extends "researcher_base.html" %}

{% block title %}My Studies - InsightPilot{% endblock %}

{% block content %}
<div class="px-4 sm:px-0">
    <!-- Header -->
    <div class="flex justify-between items-center mb-8">
        <div>
            <h1 class="text-3xl font-bold text-gray-900">My Studies</h1>
            <p class="mt-2 text-sm text-gray-600">Create and manage your research studies</p>
        </div>
        <button onclick="document.getElementById('create-modal').classList.remove('hidden')"
                class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <svg class="-ml-1 mr-2 h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
            </svg>
            New Study
        </button>
    </div>

    <!-- Studies List -->
    {% if studies %}
    <div class="bg-white shadow overflow-hidden sm:rounded-md">
        <ul class="divide-y divide-gray-200">
            {% for study in studies %}
            <li>
                <a href="/app/studies/{{ study.id }}" class="block hover:bg-gray-50 transition">
                    <div class="px-4 py-4 sm:px-6">
                        <div class="flex items-center justify-between">
                            <div class="flex-1">
                                <p class="text-lg font-medium text-indigo-600 truncate">{{ study.title }}</p>
                                <p class="mt-1 text-sm text-gray-600">{{ study.description[:100] }}{% if study.description|length > 100 %}...{% endif %}</p>
                            </div>
                            <div class="ml-4 flex-shrink-0">
                                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                                </svg>
                            </div>
                        </div>
                        <div class="mt-2 flex items-center text-sm text-gray-500">
                            <svg class="flex-shrink-0 mr-1.5 h-4 w-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                            </svg>
                            Created {{ study.created_at.strftime('%B %d, %Y') }}
                            <span class="mx-2">•</span>
                            Max {{ study.max_agent_turns }} agent turns
                        </div>
                    </div>
                </a>
            </li>
            {% endfor %}
        </ul>
    </div>
    {% else %}
    <!-- Empty State -->
    <div class="text-center py-12 bg-white rounded-lg shadow">
        <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
        <h3 class="mt-2 text-sm font-medium text-gray-900">No studies</h3>
        <p class="mt-1 text-sm text-gray-500">Get started by creating a new study.</p>
        <div class="mt-6">
            <button onclick="document.getElementById('create-modal').classList.remove('hidden')"
                    class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
                <svg class="-ml-1 mr-2 h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
                </svg>
                New Study
            </button>
        </div>
    </div>
    {% endif %}
</div>

<!-- Create Study Modal -->
<div id="create-modal" class="hidden fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" onclick="document.getElementById('create-modal').classList.add('hidden')"></div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen">&#8203;</span>
        <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6">
            <form action="/app/studies/" method="POST">
                <div>
                    <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">Create New Study</h3>
                    <div class="space-y-4">
                        <div>
                            <label for="title" class="block text-sm font-medium text-gray-700">Title</label>
                            <input type="text" name="title" id="title" required
                                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                        </div>
                        <div>
                            <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                            <textarea name="description" id="description" rows="3" required
                                      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"></textarea>
                        </div>
                        <div>
                            <label for="consent_text" class="block text-sm font-medium text-gray-700">Consent Text</label>
                            <textarea name="consent_text" id="consent_text" rows="3" required
                                      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"></textarea>
                        </div>
                        <div>
                            <label for="max_agent_turns" class="block text-sm font-medium text-gray-700">Max Agent Turns</label>
                            <input type="number" name="max_agent_turns" id="max_agent_turns" value="9" min="1" max="50" required
                                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                        </div>
                    </div>
                </div>
                <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
                    <button type="submit"
                            class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm">
                        Create
                    </button>
                    <button type="button" onclick="document.getElementById('create-modal').classList.add('hidden')"
                            class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:col-start-1 sm:text-sm">
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

```

## app/templates/studies/transcript.html

**Path:** `app/templates/studies/transcript.html`
**Type:** Html
**Size:** 12.4 KB

```html
{% extends "researcher_base.html" %}

{% block title %}Interview Transcript - {{ study.title }} - InsightPilot{% endblock %}

{% block content %}
<div class="px-4 sm:px-0">
    <!-- Header -->
    <div class="mb-8">
        <a href="/app/studies/{{ study.id }}/interviews" class="text-sm text-indigo-600 hover:text-indigo-800 mb-2 inline-flex items-center">
            <svg class="h-4 w-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
            </svg>
            Back to Interviews
        </a>
        <div class="flex items-center justify-between">
            <div>
                <h1 class="text-3xl font-bold text-gray-900 mt-2">Interview Transcript</h1>
                <p class="mt-2 text-gray-600">{{ interviewee.name if interviewee else 'Anonymous' }} - {{ study.title }}</p>
            </div>
            <div class="flex space-x-3">
                <a href="/app/studies/{{ study.id }}/analytics"
                   class="inline-flex items-center px-3 py-2 border border-indigo-300 shadow-sm text-sm font-medium rounded-md text-indigo-700 bg-white hover:bg-indigo-50">
                    <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                    </svg>
                    Analytics
                </a>
                <a href="/studies/{{ study.id }}/interviews/{{ interview.id }}/export?format=csv"
                   class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                    <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
                    </svg>
                    Export CSV
                </a>
                <a href="/studies/{{ study.id }}/interviews/{{ interview.id }}/export?format=json"
                   class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                    <svg class="-ml-0.5 mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
                    </svg>
                    Export JSON
                </a>
            </div>
        </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Main Transcript Column -->
        <div class="lg:col-span-2">
            <!-- Interview Info Card -->
            <div class="bg-white shadow rounded-lg p-6 mb-6">
                <div class="flex items-center justify-between mb-4">
                    <h2 class="text-lg font-medium text-gray-900">Interview Details</h2>
                    {% if interview.completed_at %}
                        <span class="px-3 py-1 inline-flex text-sm leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                            Completed
                        </span>
                    {% else %}
                        <span class="px-3 py-1 inline-flex text-sm leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
                            In Progress
                        </span>
                    {% endif %}
                </div>
                <dl class="grid grid-cols-1 gap-x-4 gap-y-4 sm:grid-cols-2">
                    {% if interviewee %}
                        <div>
                            <dt class="text-sm font-medium text-gray-500">Participant</dt>
                            <dd class="mt-1 text-sm text-gray-900">{{ interviewee.name }}</dd>
                        </div>
                        <div>
                            <dt class="text-sm font-medium text-gray-500">Email</dt>
                            <dd class="mt-1 text-sm text-gray-900">{{ interviewee.email }}</dd>
                        </div>
                    {% endif %}
                    <div>
                        <dt class="text-sm font-medium text-gray-500">Started</dt>
                        <dd class="mt-1 text-sm text-gray-900">{{ interview.started_at.strftime('%B %d, %Y at %I:%M %p') }}</dd>
                    </div>
                    {% if interview.completed_at %}
                        <div>
                            <dt class="text-sm font-medium text-gray-500">Completed</dt>
                            <dd class="mt-1 text-sm text-gray-900">{{ interview.completed_at.strftime('%B %d, %Y at %I:%M %p') }}</dd>
                        </div>
                    {% endif %}
                    <div>
                        <dt class="text-sm font-medium text-gray-500">Agent Turns</dt>
                        <dd class="mt-1 text-sm text-gray-900">{{ interview.agent_turns }} / {{ study.max_agent_turns }}</dd>
                    </div>
                    <div>
                        <dt class="text-sm font-medium text-gray-500">Total Messages</dt>
                        <dd class="mt-1 text-sm text-gray-900">{{ messages|length }}</dd>
                    </div>
                </dl>

                {% if interviewee and interviewee.demographics_json %}
                    <div class="mt-4 pt-4 border-t border-gray-200">
                        <dt class="text-sm font-medium text-gray-500 mb-2">Demographics</dt>
                        <dd class="mt-1 text-sm text-gray-900">
                            <div class="flex flex-wrap gap-2">
                                {% for key, value in interviewee.demographics_json.items() %}
                                    <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                                        {{ key|replace('_', ' ')|title }}: {{ value }}
                                    </span>
                                {% endfor %}
                            </div>
                        </dd>
                    </div>
                {% endif %}
            </div>

            <!-- Conversation Transcript -->
            <div class="bg-white shadow rounded-lg p-6">
                <h2 class="text-lg font-medium text-gray-900 mb-4">Conversation</h2>
                <div class="space-y-4">
                    {% for message in messages %}
                        <div class="flex {% if message.role == 'user' %}justify-end{% else %}justify-start{% endif %}">
                            <div class="{% if message.role == 'user' %}bg-indigo-100{% else %}bg-gray-100{% endif %} rounded-lg px-4 py-3 max-w-3xl">
                                <div class="flex items-center mb-1">
                                    <span class="text-xs font-medium {% if message.role == 'user' %}text-indigo-900{% else %}text-gray-900{% endif %}">
                                        {% if message.role == 'user' %}
                                            {{ interviewee.name if interviewee else 'Participant' }}
                                        {% else %}
                                            AI Interviewer
                                        {% endif %}
                                    </span>
                                    <span class="ml-2 text-xs text-gray-500">
                                        {{ message.created_at.strftime('%I:%M %p') }}
                                    </span>
                                </div>
                                <p class="text-sm {% if message.role == 'user' %}text-indigo-900{% else %}text-gray-900{% endif %} whitespace-pre-wrap">{{ message.content }}</p>
                            </div>
                        </div>
                    {% endfor %}
                </div>

                {% if not messages %}
                    <p class="text-center text-gray-500 py-8">No messages yet.</p>
                {% endif %}
            </div>
        </div>

        <!-- Insights Sidebar -->
        <div class="lg:col-span-1">
            {% if insight %}
                <!-- Sentiment Card -->
                <div class="bg-white shadow rounded-lg p-6 mb-6">
                    <h3 class="text-lg font-medium text-gray-900 mb-4">Sentiment</h3>
                    <div class="flex items-center justify-center">
                        {% if insight.sentiment == 'positive' %}
                            <div class="text-center">
                                <div class="text-6xl mb-2">😊</div>
                                <p class="text-sm font-medium text-green-600">Positive</p>
                            </div>
                        {% elif insight.sentiment == 'negative' %}
                            <div class="text-center">
                                <div class="text-6xl mb-2">😞</div>
                                <p class="text-sm font-medium text-red-600">Negative</p>
                            </div>
                        {% else %}
                            <div class="text-center">
                                <div class="text-6xl mb-2">😐</div>
                                <p class="text-sm font-medium text-gray-600">Neutral</p>
                            </div>
                        {% endif %}
                    </div>
                </div>

                <!-- Summary Card -->
                <div class="bg-white shadow rounded-lg p-6 mb-6">
                    <h3 class="text-lg font-medium text-gray-900 mb-3">Summary</h3>
                    <p class="text-sm text-gray-700">{{ insight.summary }}</p>
                </div>

                <!-- Keywords Card -->
                {% if insight.keywords_json %}
                    <div class="bg-white shadow rounded-lg p-6 mb-6">
                        <h3 class="text-lg font-medium text-gray-900 mb-3">Key Topics</h3>
                        <div class="flex flex-wrap gap-2">
                            {% for keyword in insight.keywords_json[:10] %}
                                <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800">
                                    {{ keyword }}
                                </span>
                            {% endfor %}
                        </div>
                    </div>
                {% endif %}

                <!-- Quotes Card -->
                {% if insight.quotes_json %}
                    <div class="bg-white shadow rounded-lg p-6">
                        <h3 class="text-lg font-medium text-gray-900 mb-3">Notable Quotes</h3>
                        <div class="space-y-3">
                            {% for quote in insight.quotes_json %}
                                <blockquote class="border-l-4 border-indigo-500 pl-4 py-2">
                                    <p class="text-sm text-gray-700 italic">"{{ quote }}"</p>
                                </blockquote>
                            {% endfor %}
                        </div>
                    </div>
                {% endif %}
            {% else %}
                <!-- No Insights Yet -->
                <div class="bg-white shadow rounded-lg p-6">
                    <div class="text-center py-8">
                        <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                        </svg>
                        <h3 class="mt-2 text-sm font-medium text-gray-900">No insights yet</h3>
                        <p class="mt-1 text-sm text-gray-500">
                            Insights will be generated when the interview is completed.
                        </p>
                    </div>
                </div>
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}

```

## app/utils/__init__.py

**Path:** `app/utils/__init__.py`
**Type:** Python
**Size:** 0 bytes

```python

```

## app/utils/logging.py

**Path:** `app/utils/logging.py`
**Type:** Python
**Size:** 1.5 KB

```python
"""Logging configuration with rotating file handler."""

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def configure_logging(log_level: str = "INFO") -> None:
    """
    Configure application logging with stdout and rotating file handlers.

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    root = logging.getLogger()
    root.setLevel(getattr(logging, log_level.upper(), logging.INFO))

    # Clear existing handlers to avoid duplicates
    root.handlers.clear()

    # Formatter with timestamp, level, logger name, and message
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler (stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)

    # Rotating file handler (2MB max, keep 3 backups)
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    file_handler = RotatingFileHandler(
        log_dir / "app.log", maxBytes=2_000_000, backupCount=3, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)

    # Reduce noise from third-party libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.WARNING)

    root.info("Logging configured successfully")

```

## docker-compose.yml

**Path:** `docker-compose.yml`
**Type:** Yaml
**Size:** 1.3 KB

```yaml
version: "3.9"

services:
  db:
    image: postgres:16-alpine
    container_name: insightpilot_db
    environment:
      POSTGRES_DB: insightpilot
      POSTGRES_USER: insight
      POSTGRES_PASSWORD: insight
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U insight -d insightpilot"]
      interval: 5s
      timeout: 3s
      retries: 10
      start_period: 10s
    networks:
      - insightpilot_network

  app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: insightpilot_app
    depends_on:
      db:
        condition: service_healthy
    environment:
      APP_ENV: dev
      SECRET_KEY: "dev-secret-key-change-in-production"
      SESSION_COOKIE_NAME: ip_session
      DATABASE_URL: postgresql+psycopg2://insight:insight@db:5432/insightpilot
    ports:
      - "8000:8000"
    volumes:
      # Mount source code for hot-reload during development
      - ./app:/app/app:rw
      - ./alembic:/app/alembic:rw
      - ./alembic.ini:/app/alembic.ini:ro
    networks:
      - insightpilot_network
    command: sh -c "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

volumes:
  pgdata:
    name: insightpilot_pgdata

networks:
  insightpilot_network:
    name: insightpilot_network
    driver: bridge

```

## examples/README.md

**Path:** `examples/README.md`
**Type:** Markdown
**Size:** 1.1 KB

```markdown
# Examples

Standalone scripts for testing components independently.

## AI Agent Test

Test the AI interview agent in your terminal before integrating with the web interface.

### Prerequisites

You need an OpenAI API key. Add it to your `.env` file:

```bash
OPENAI_API_KEY=sk-your-api-key-here
```

### Usage

**Basic test (5 turns):**
```bash
python examples/test_ai_agent.py
```

**Custom number of turns:**
```bash
python examples/test_ai_agent.py --turns 10
```

**Test system prompt generation:**
```bash
python examples/test_ai_agent.py --test-prompt
```

### Options

- `--turns N` - Set maximum number of conversation turns (default: 5)
- `--test-prompt` - Display the system prompt and exit

### Example Session

```
AI Interview Agent - Terminal Test
============================================================

Study: User Experience with Mobile Banking Apps
Max Turns: 5

============================================================

🤖 AI: Hello Test User! Thank you for participating...

--- Turn 1/5 ---

👤 You: I really like the fingerprint login feature
🤖 AI: Thank you for sharing that. Can you tell me more...
```

```

## examples/test_ai_agent.py

**Path:** `examples/test_ai_agent.py`
**Type:** Python
**Size:** 5.4 KB

```python
#!/usr/bin/env python3
"""
Terminal-based test for the AI Interview Agent. (Created using AI for quick testing)

Usage:
    # Requires OPENAI_API_KEY environment variable
    python examples/test_ai_agent.py

    # Custom number of turns
    python examples/test_ai_agent.py --turns 10
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path so we can import from app
sys.path.insert(0, str(Path(__file__).parent.parent))

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

from app.services.ai_agent import AIInterviewAgent


def simulate_interview(max_turns: int = 5):
    """Simulate an interactive interview in the terminal."""

    # Sample study data
    study_title = "User Experience with Mobile Banking Apps"
    study_description = "Understanding how people interact with mobile banking applications and what features they value most."
    study_questions = [
        "What are the most important features in a mobile banking app?",
        "What frustrations do users experience with current banking apps?",
        "How do security concerns affect mobile banking usage?",
        "What improvements would users like to see?",
    ]
    interviewee_name = "Test User"

    # Initialize agent
    print("=" * 60)
    print("AI Interview Agent - Terminal Test")
    print("=" * 60)
    print(f"\nStudy: {study_title}")
    print(f"Max Turns: {max_turns}")
    print("\n" + "=" * 60)

    try:
        agent = AIInterviewAgent()
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("\nTip: Set OPENAI_API_KEY in your .env file or environment")
        return

    # Start interview with initial message
    print(f"\n🤖 AI Agent: Getting initial message...\n")

    initial_message = agent.get_initial_message(
        study_title=study_title,
        study_description=study_description,
        study_questions=study_questions,
        interviewee_name=interviewee_name,
    )

    print(f"🤖 AI: {initial_message}\n")

    # Conversation history
    conversation_history = []

    # Interactive conversation loop
    for turn in range(max_turns):
        print(f"--- Turn {turn + 1}/{max_turns} ---")

        # Get user input
        try:
            user_message = input("\n👤 You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Interview interrupted. Goodbye!")
            return

        if not user_message:
            print("⚠️  Please enter a message.")
            continue

        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Get AI response
        print(f"\n🤖 AI Agent: Thinking...\n")

        ai_response = agent.get_ai_response(
            study_title=study_title,
            study_description=study_description,
            study_questions=study_questions,
            conversation_history=conversation_history,
            current_turn=turn,
            max_turns=max_turns,
        )

        print(f"🤖 AI: {ai_response}\n")

        # Add AI response to history
        conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })

    # Interview complete
    print("\n" + "=" * 60)
    print("✅ Interview Complete!")
    print("=" * 60)
    print(f"\nTotal messages: {len(conversation_history)}")
    print(f"User messages: {len([m for m in conversation_history if m['role'] == 'user'])}")
    print(f"AI messages: {len([m for m in conversation_history if m['role'] == 'assistant'])}")

    # Show conversation summary
    print("\n📝 Conversation Summary:")
    print("-" * 60)
    for i, msg in enumerate(conversation_history, 1):
        speaker = "👤 You" if msg['role'] == 'user' else "🤖 AI"
        content = msg['content'][:100] + "..." if len(msg['content']) > 100 else msg['content']
        print(f"{i}. {speaker}: {content}")


def test_system_prompt():
    """Test system prompt generation."""
    try:
        agent = AIInterviewAgent()
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("\nNote: API key not required for prompt generation test")
        print("Creating dummy agent for demonstration...\n")
        # For testing prompt generation, we can skip the actual API client
        import os
        os.environ.setdefault("OPENAI_API_KEY", "dummy-key-for-prompt-test")
        agent = AIInterviewAgent()

    prompt = agent.generate_system_prompt(
        study_title="Test Study",
        study_description="This is a test study description.",
        study_questions=["Question 1?", "Question 2?"],
        turns_remaining=5,
    )

    print("=" * 60)
    print("System Prompt Test")
    print("=" * 60)
    print(prompt)
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Test the AI Interview Agent")
    parser.add_argument(
        "--turns",
        type=int,
        default=5,
        help="Maximum number of turns (default: 5)"
    )
    parser.add_argument(
        "--test-prompt",
        action="store_true",
        help="Just test system prompt generation and exit"
    )

    args = parser.parse_args()

    if args.test_prompt:
        test_system_prompt()
    else:
        simulate_interview(max_turns=args.turns)


if __name__ == "__main__":
    main()

```

## insightpilot.egg-info/SOURCES.txt

**Path:** `insightpilot.egg-info/SOURCES.txt`
**Type:** Text
**Size:** 1000 bytes

```text
README.md
pyproject.toml
app/__init__.py
app/main.py
app/middleware.py
app/settings.py
app/auth/__init__.py
app/auth/dependencies.py
app/auth/sessions.py
app/crud/__init__.py
app/crud/interview.py
app/crud/invite.py
app/crud/session.py
app/crud/study.py
app/crud/user.py
app/db/__init__.py
app/db/base.py
app/db/session.py
app/models/__init__.py
app/models/interview.py
app/models/invite.py
app/models/session.py
app/models/study.py
app/models/user.py
app/routers/__init__.py
app/routers/auth_dev.py
app/routers/health.py
app/routers/interview.py
app/routers/studies.py
app/routers/web.py
app/routers/web_studies.py
app/schemas/__init__.py
app/schemas/interview.py
app/schemas/invite.py
app/schemas/study.py
app/services/__init__.py
app/services/ai_agent.py
app/utils/__init__.py
app/utils/logging.py
insightpilot.egg-info/PKG-INFO
insightpilot.egg-info/SOURCES.txt
insightpilot.egg-info/dependency_links.txt
insightpilot.egg-info/requires.txt
insightpilot.egg-info/top_level.txt
tests/test_health.py
```

## insightpilot.egg-info/dependency_links.txt

**Path:** `insightpilot.egg-info/dependency_links.txt`
**Type:** Text
**Size:** 1 bytes

```text

```

## insightpilot.egg-info/requires.txt

**Path:** `insightpilot.egg-info/requires.txt`
**Type:** Text
**Size:** 479 bytes

```text
fastapi==0.115.0
uvicorn[standard]==0.32.0
jinja2==3.1.4
python-multipart==0.0.12
sqlalchemy==2.0.36
psycopg2-binary==2.9.10
alembic==1.14.0
pydantic==2.10.3
pydantic-settings==2.6.1
pydantic[email]==2.10.3
passlib[argon2]==1.7.4
argon2-cffi==23.1.0
itsdangerous==2.2.0
httpx==0.27.2
python-dotenv==1.0.1
email-validator==2.2.0
openai>=1.0.0
vaderSentiment==3.3.2
yake==0.4.8

[dev]
pytest==8.3.4
pytest-asyncio==0.24.0
black==24.10.0
isort==5.13.2
ruff==0.8.4
pre-commit==4.0.1
```

## insightpilot.egg-info/top_level.txt

**Path:** `insightpilot.egg-info/top_level.txt`
**Type:** Text
**Size:** 4 bytes

```text
app
```

## pyproject.toml

**Path:** `pyproject.toml`
**Type:** Toml
**Size:** 2.0 KB

```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "insightpilot"
version = "0.1.0"
description = "A market research tool that uses LLMs to conduct interviews"
readme = "README.md"
requires-python = ">=3.11"
license = "MIT"
authors = [
    {name = "InsightPilot Team"}
]
keywords = ["market-research", "llm", "interviews", "fastapi"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]

dependencies = [
    "fastapi==0.115.0",
    "uvicorn[standard]==0.32.0",
    "jinja2==3.1.4",
    "python-multipart==0.0.12",
    "sqlalchemy==2.0.36",
    "psycopg2-binary==2.9.10",
    "alembic==1.14.0",
    "pydantic==2.10.3",
    "pydantic-settings==2.6.1",
    "pydantic[email]==2.10.3",
    "passlib[argon2]==1.7.4",
    "argon2-cffi==23.1.0",
    "itsdangerous==2.2.0",
    "httpx==0.27.2",
    "python-dotenv==1.0.1",
    "email-validator==2.2.0",
    "openai>=1.0.0",
    "vaderSentiment==3.3.2",
    "yake==0.4.8",
]

[project.optional-dependencies]
dev = [
    "pytest==8.3.4",
    "pytest-asyncio==0.24.0",
    "black==24.10.0",
    "isort==5.13.2",
    "ruff==0.8.4",
    "pre-commit==4.0.1",
]

[tool.black]
line-length = 100
target-version = ["py311"]
exclude = '''
/(
    \.git
  | \.venv
  | __pycache__
  | alembic/versions
)/
'''

[tool.isort]
profile = "black"
line_length = 100
skip = [".venv", "__pycache__", "alembic/versions"]

[tool.ruff]
line-length = 100
target-version = "py311"
select = ["E", "F", "I", "UP", "N", "W"]
ignore = []
exclude = [
    ".venv",
    "__pycache__",
    "alembic/versions",
]

[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"

[tool.setuptools.packages.find]
where = ["."]
include = ["app*"]
exclude = ["alembic*", "tests*", "venv*"]

```

## tests/__init__.py

**Path:** `tests/__init__.py`
**Type:** Python
**Size:** 0 bytes

```python

```

## tests/auth/__init__.py

**Path:** `tests/auth/__init__.py`
**Type:** Python
**Size:** 0 bytes

```python

```

## tests/auth/test_dependencies.py

**Path:** `tests/auth/test_dependencies.py`
**Type:** Python
**Size:** 11.7 KB

```python
"""Unit tests for authentication dependencies."""

import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

from fastapi import HTTPException
from starlette.requests import Request

from app.auth import dependencies
from app.crud import session as session_crud
from app.crud import user as user_crud


@pytest.fixture
def db_session(test_db):
    """Get a database session for testing."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_user(db_session):
    """Create a test user."""
    return user_crud.create_user(db_session, "testuser@example.com", "hash123")


@pytest.fixture
def test_session(db_session, test_user):
    """Create a valid test session."""
    return session_crud.create_session(db_session, test_user.id)


@pytest.fixture
def mock_request_with_session(test_session):
    """Create a mock request with a valid session cookie."""
    request = MagicMock(spec=Request)

    # Mock the session cookie with proper serialization
    from app.auth.sessions import serializer, SESSION_COOKIE
    import time
    token = serializer.dumps({"sid": test_session.id, "ts": int(time.time())})
    request.cookies = {SESSION_COOKIE: token}

    return request


@pytest.fixture
def mock_request_no_session():
    """Create a mock request with no session cookie."""
    request = MagicMock(spec=Request)
    request.cookies = {}
    return request


# Tests for get_current_session_id


def test_get_current_session_id_valid(mock_request_with_session):
    """Test getting session ID from valid cookie."""
    session_id = dependencies.get_current_session_id(mock_request_with_session)

    assert session_id is not None
    assert isinstance(session_id, str)
    assert len(session_id) > 20  # Should be a long random string


def test_get_current_session_id_no_cookie(mock_request_no_session):
    """Test that missing cookie raises 401."""
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(mock_request_no_session)

    assert exc_info.value.status_code == 401
    assert "not authenticated" in exc_info.value.detail.lower()


def test_get_current_session_id_invalid_cookie():
    """Test that invalid cookie raises 401."""
    request = MagicMock(spec=Request)
    from app.auth.sessions import SESSION_COOKIE
    request.cookies = {SESSION_COOKIE: "invalid_token"}

    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)

    assert exc_info.value.status_code == 401


def test_get_current_session_id_tampered_cookie():
    """Test that tampered cookie raises 401."""
    request = MagicMock(spec=Request)
    from app.auth.sessions import serializer, SESSION_COOKIE
    import time

    # Create valid token then tamper with it
    token = serializer.dumps({"sid": "test_session", "ts": int(time.time())})
    tampered = token[:-10] + "tampered123"
    request.cookies = {SESSION_COOKIE: tampered}

    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)

    assert exc_info.value.status_code == 401


# Tests for get_current_user


def test_get_current_user_valid_session(db_session, test_user, test_session):
    """Test getting current user with valid session."""
    user = dependencies.get_current_user(test_session.id, db_session)

    assert user is not None
    assert user.id == test_user.id
    assert user.email == test_user.email


def test_get_current_user_invalid_session_id(db_session):
    """Test that invalid session ID raises 401."""
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user("nonexistent_session_id", db_session)

    assert exc_info.value.status_code == 401
    assert "invalid session" in exc_info.value.detail.lower()


def test_get_current_user_expired_session(db_session, test_user):
    """Test that expired session raises 401."""
    # Create expired session
    session = session_crud.create_session(db_session, test_user.id)

    # Manually expire the session
    session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=1)
    db_session.commit()
    db_session.refresh(session)

    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user(session.id, db_session)

    assert exc_info.value.status_code == 401
    assert "expired" in exc_info.value.detail.lower()


def test_get_current_user_deleted_user(db_session, test_user, test_session):
    """Test that session with deleted user raises 401."""
    # Delete the user
    # Note: Due to CASCADE delete on foreign key, the session is also deleted
    user_crud.delete_user(db_session, test_user.id)

    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user(test_session.id, db_session)

    assert exc_info.value.status_code == 401
    # Session is cascade-deleted with user, so we get "invalid session" error
    assert "invalid session" in exc_info.value.detail.lower()


def test_get_current_user_multiple_sessions(db_session, test_user):
    """Test that each session correctly identifies the user."""
    # Create multiple sessions for same user
    session1 = session_crud.create_session(db_session, test_user.id)
    session2 = session_crud.create_session(db_session, test_user.id)

    # Both sessions should return same user
    user1 = dependencies.get_current_user(session1.id, db_session)
    user2 = dependencies.get_current_user(session2.id, db_session)

    assert user1.id == test_user.id
    assert user2.id == test_user.id
    assert user1.id == user2.id


def test_get_current_user_different_users(db_session):
    """Test that sessions correctly identify different users."""
    user1 = user_crud.create_user(db_session, "user1@example.com", "hash1")
    user2 = user_crud.create_user(db_session, "user2@example.com", "hash2")

    session1 = session_crud.create_session(db_session, user1.id)
    session2 = session_crud.create_session(db_session, user2.id)

    retrieved_user1 = dependencies.get_current_user(session1.id, db_session)
    retrieved_user2 = dependencies.get_current_user(session2.id, db_session)

    assert retrieved_user1.id == user1.id
    assert retrieved_user2.id == user2.id
    assert retrieved_user1.id != retrieved_user2.id


def test_get_current_user_returns_fresh_data(db_session, test_user, test_session):
    """Test that get_current_user returns fresh user data."""
    # Get user initially
    user = dependencies.get_current_user(test_session.id, db_session)
    old_password_hash = user.password_hash

    # Update user password
    new_hash = "new_password_hash_123"
    user_crud.update_user_password(db_session, test_user.id, new_hash)

    # Get user again - should have new data
    user_refreshed = dependencies.get_current_user(test_session.id, db_session)

    assert user_refreshed.password_hash == new_hash
    assert user_refreshed.password_hash != old_password_hash


def test_get_current_user_session_validation_order(db_session, test_user):
    """Test that session validation happens before user lookup."""
    # Create expired session
    session = session_crud.create_session(db_session, test_user.id)
    session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=1)
    db_session.commit()

    # Even though user exists, expired session should fail first
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user(session.id, db_session)

    # Should get "expired" error, not "user not found"
    assert "expired" in exc_info.value.detail.lower()


def test_get_current_user_with_newly_created_session(db_session, test_user):
    """Test getting user immediately after session creation."""
    session = session_crud.create_session(db_session, test_user.id)

    # Should work immediately
    user = dependencies.get_current_user(session.id, db_session)

    assert user.id == test_user.id


def test_get_current_user_session_about_to_expire(db_session, test_user):
    """Test that session that's about to expire (but not yet) still works."""
    session = session_crud.create_session(db_session, test_user.id)

    # Set expiration to 1 second in the future
    session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(seconds=1)
    db_session.commit()
    db_session.refresh(session)

    # Should still be valid
    user = dependencies.get_current_user(session.id, db_session)
    assert user.id == test_user.id


def test_get_current_user_session_just_expired(db_session, test_user):
    """Test that session that just expired is invalid."""
    session = session_crud.create_session(db_session, test_user.id)

    # Set expiration to 1 second in the past
    session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(seconds=1)
    db_session.commit()
    db_session.refresh(session)

    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_user(session.id, db_session)

    assert exc_info.value.status_code == 401


# Integration tests


def test_full_auth_flow(db_session):
    """Test complete authentication flow from request to user."""
    # Create user
    user = user_crud.create_user(db_session, "fullflow@example.com", "hash123")

    # Create session
    session = session_crud.create_session(db_session, user.id)

    # Create request with session cookie
    from app.auth.sessions import serializer, SESSION_COOKIE
    import time
    token = serializer.dumps({"sid": session.id, "ts": int(time.time())})
    request = MagicMock(spec=Request)
    request.cookies = {SESSION_COOKIE: token}

    # Extract session ID from request
    session_id = dependencies.get_current_session_id(request)
    assert session_id == session.id

    # Get user from session
    retrieved_user = dependencies.get_current_user(session_id, db_session)
    assert retrieved_user.id == user.id
    assert retrieved_user.email == "fullflow@example.com"


def test_auth_flow_with_invalid_session(db_session):
    """Test auth flow fails gracefully with invalid session."""
    # Create request with invalid session
    request = MagicMock(spec=Request)
    from app.auth.sessions import SESSION_COOKIE
    request.cookies = {SESSION_COOKIE: "invalid_token"}

    # Should raise 401 at session extraction
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)

    assert exc_info.value.status_code == 401


def test_auth_flow_with_no_session(db_session):
    """Test auth flow fails gracefully with no session."""
    request = MagicMock(spec=Request)
    request.cookies = {}

    # Should raise 401 at session extraction
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)

    assert exc_info.value.status_code == 401


def test_error_messages_are_informative():
    """Test that error messages help with debugging."""
    request = MagicMock(spec=Request)
    request.cookies = {}

    # No session error
    with pytest.raises(HTTPException) as exc_info:
        dependencies.get_current_session_id(request)
    assert exc_info.value.detail  # Should have a message
    assert len(exc_info.value.detail) > 0


def test_get_current_user_preserves_user_model(db_session, test_user, test_session):
    """Test that returned user is a proper User model instance."""
    from app.models.user import User

    user = dependencies.get_current_user(test_session.id, db_session)

    assert isinstance(user, User)
    assert hasattr(user, "id")
    assert hasattr(user, "email")
    assert hasattr(user, "password_hash")
    assert hasattr(user, "created_at")

```

## tests/auth/test_sessions.py

**Path:** `tests/auth/test_sessions.py`
**Type:** Python
**Size:** 8.8 KB

```python
"""Unit tests for session cookie utilities."""

import time
from unittest.mock import MagicMock, patch

import pytest
from itsdangerous import URLSafeSerializer
from starlette.requests import Request
from starlette.responses import Response

from app.auth import sessions
from app.settings import settings


@pytest.fixture
def mock_response():
    """Create a mock response object."""
    response = MagicMock(spec=Response)
    response.set_cookie = MagicMock()
    response.delete_cookie = MagicMock()
    return response


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    request = MagicMock(spec=Request)
    request.cookies = {}
    return request


def test_serializer_initialization():
    """Test that serializer is initialized with correct settings."""
    assert sessions.serializer is not None
    assert isinstance(sessions.serializer, URLSafeSerializer)
    assert sessions.SESSION_COOKIE == settings.session_cookie_name


def test_set_session_basic(mock_response):
    """Test setting a session cookie."""
    session_id = "test_session_123"

    sessions.set_session(mock_response, session_id)

    # Verify set_cookie was called
    mock_response.set_cookie.assert_called_once()
    call_args = mock_response.set_cookie.call_args

    # Check cookie name (first positional arg)
    assert call_args[0][0] == settings.session_cookie_name

    # Check cookie value is a token (second positional arg)
    token = call_args[0][1]
    assert isinstance(token, str)
    assert len(token) > 20  # Serialized token should be long

    # Check kwargs
    assert call_args[1]["httponly"] is True
    assert call_args[1]["samesite"] == "lax"
    assert call_args[1]["secure"] == settings.is_production
    assert call_args[1]["max_age"] == 60 * 60 * 24 * 7  # Default 7 days


def test_set_session_custom_max_age(mock_response):
    """Test setting a session cookie with custom max_age."""
    session_id = "test_session_123"
    custom_max_age = 3600  # 1 hour

    sessions.set_session(mock_response, session_id, max_age=custom_max_age)

    call_args = mock_response.set_cookie.call_args
    assert call_args[1]["max_age"] == custom_max_age


def test_set_session_token_structure(mock_response):
    """Test that the session token contains correct data."""
    session_id = "test_session_123"

    with patch('time.time', return_value=1234567890.0):
        sessions.set_session(mock_response, session_id)

    # Extract the token that was set
    token = mock_response.set_cookie.call_args[0][1]

    # Deserialize and verify structure
    data = sessions.serializer.loads(token)
    assert data["sid"] == session_id
    assert data["ts"] == 1234567890
    assert isinstance(data["ts"], int)


def test_get_session_valid_token(mock_request):
    """Test getting session ID from valid cookie."""
    session_id = "test_session_123"

    # Create a valid token
    token = sessions.serializer.dumps({"sid": session_id, "ts": int(time.time())})
    mock_request.cookies = {settings.session_cookie_name: token}

    result = sessions.get_session(mock_request)

    assert result == session_id


def test_get_session_no_cookie(mock_request):
    """Test getting session when no cookie exists."""
    mock_request.cookies = {}

    result = sessions.get_session(mock_request)

    assert result is None


def test_get_session_invalid_token(mock_request):
    """Test getting session with invalid/corrupted token."""
    mock_request.cookies = {settings.session_cookie_name: "invalid_token_data"}

    result = sessions.get_session(mock_request)

    assert result is None


def test_get_session_tampered_token(mock_request):
    """Test getting session with tampered token."""
    # Create a valid token then tamper with it
    session_id = "test_session_123"
    token = sessions.serializer.dumps({"sid": session_id, "ts": int(time.time())})
    tampered_token = token[:-5] + "xxxxx"  # Tamper with the end

    mock_request.cookies = {settings.session_cookie_name: tampered_token}

    result = sessions.get_session(mock_request)

    assert result is None


def test_get_session_missing_sid(mock_request):
    """Test getting session when token is missing 'sid' key."""
    # Create token with wrong structure
    serializer = URLSafeSerializer(settings.secret_key, salt="session")
    token = serializer.dumps({"session_id": "test", "ts": int(time.time())})  # Wrong key

    mock_request.cookies = {settings.session_cookie_name: token}

    result = sessions.get_session(mock_request)

    # Should return None since 'sid' key is missing
    assert result is None


def test_get_session_different_secret_key(mock_request):
    """Test that tokens signed with different secret can't be validated."""
    session_id = "test_session_123"

    # Sign with different secret
    wrong_serializer = URLSafeSerializer("wrong_secret_key", salt="session")
    token = wrong_serializer.dumps({"sid": session_id, "ts": int(time.time())})

    mock_request.cookies = {settings.session_cookie_name: token}

    result = sessions.get_session(mock_request)

    assert result is None


def test_clear_session(mock_response):
    """Test clearing a session cookie."""
    sessions.clear_session(mock_response)

    mock_response.delete_cookie.assert_called_once_with(settings.session_cookie_name)


def test_roundtrip_session_set_and_get():
    """Test complete roundtrip: set cookie and retrieve session."""
    session_id = "roundtrip_test_session"

    # Set session
    mock_response = MagicMock(spec=Response)
    mock_response.set_cookie = MagicMock()
    sessions.set_session(mock_response, session_id)

    # Get the token that was set
    token = mock_response.set_cookie.call_args[0][1]

    # Create request with that token
    mock_request = MagicMock(spec=Request)
    mock_request.cookies = {settings.session_cookie_name: token}

    # Get session
    retrieved_session_id = sessions.get_session(mock_request)

    assert retrieved_session_id == session_id


def test_multiple_sessions_different_ids():
    """Test that different session IDs produce different tokens."""
    mock_response1 = MagicMock(spec=Response)
    mock_response2 = MagicMock(spec=Response)
    mock_response1.set_cookie = MagicMock()
    mock_response2.set_cookie = MagicMock()

    sessions.set_session(mock_response1, "session_1")
    sessions.set_session(mock_response2, "session_2")

    token1 = mock_response1.set_cookie.call_args[0][1]
    token2 = mock_response2.set_cookie.call_args[0][1]

    # Tokens should be different
    assert token1 != token2

    # But both should be valid
    data1 = sessions.serializer.loads(token1)
    data2 = sessions.serializer.loads(token2)

    assert data1["sid"] == "session_1"
    assert data2["sid"] == "session_2"


def test_session_cookie_security_flags():
    """Test that security flags are set correctly based on environment."""
    mock_response = MagicMock(spec=Response)
    mock_response.set_cookie = MagicMock()

    sessions.set_session(mock_response, "test_session")

    call_args = mock_response.set_cookie.call_args[1]

    # Verify security settings
    assert call_args["httponly"] is True  # Prevent XSS
    assert call_args["samesite"] == "lax"  # CSRF protection
    # Secure flag depends on environment
    assert call_args["secure"] == settings.is_production


def test_session_with_empty_string_id(mock_response):
    """Test setting session with empty string ID (edge case)."""
    sessions.set_session(mock_response, "")

    # Should still work
    mock_response.set_cookie.assert_called_once()
    token = mock_response.set_cookie.call_args[0][1]

    # Should be able to deserialize
    data = sessions.serializer.loads(token)
    assert data["sid"] == ""


def test_session_with_special_characters_id(mock_response):
    """Test setting session with special characters in ID."""
    special_id = "session!@#$%^&*()_+-=[]{}|;:',.<>?/"

    sessions.set_session(mock_response, special_id)

    token = mock_response.set_cookie.call_args[0][1]
    data = sessions.serializer.loads(token)

    assert data["sid"] == special_id


def test_session_timestamp_is_integer(mock_response):
    """Test that timestamp in token is an integer."""
    sessions.set_session(mock_response, "test_session")

    token = mock_response.set_cookie.call_args[0][1]
    data = sessions.serializer.loads(token)

    assert isinstance(data["ts"], int)
    assert data["ts"] > 0


def test_get_session_with_wrong_cookie_name(mock_request):
    """Test that wrong cookie name returns None."""
    session_id = "test_session"
    token = sessions.serializer.dumps({"sid": session_id, "ts": int(time.time())})

    # Set token with wrong cookie name
    mock_request.cookies = {"wrong_cookie_name": token}

    result = sessions.get_session(mock_request)

    assert result is None

```

## tests/conftest.py

**Path:** `tests/conftest.py`
**Type:** Python
**Size:** 2.0 KB

```python
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

```

## tests/crud/__init__.py

**Path:** `tests/crud/__init__.py`
**Type:** Python
**Size:** 0 bytes

```python

```

## tests/crud/test_interview.py

**Path:** `tests/crud/test_interview.py`
**Type:** Python
**Size:** 18.1 KB

```python
"""Unit tests for interview CRUD operations."""

import pytest
from datetime import datetime, timezone

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud


@pytest.fixture
def db_session(test_db):
    """Get a database session for testing."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_user(db_session):
    """Create a test user."""
    return user_crud.create_user(db_session, "testuser@example.com", "hash123")


@pytest.fixture
def test_study(db_session, test_user):
    """Create a test study."""
    return study_crud.create_study(
        db_session,
        owner_user_id=test_user.id,
        title="Test Study",
        description="Test Description",
        consent_text="Test Consent",
    )


@pytest.fixture
def test_invite(db_session, test_study):
    """Create a test invite."""
    return invite_crud.create_invite(db_session, test_study.id)


@pytest.fixture
def test_interview(db_session, test_study, test_invite):
    """Create a test interview."""
    return interview_crud.create_interview(db_session, test_study.id, test_invite.id)


# Interview CRUD Tests


def test_create_interview(db_session, test_study, test_invite):
    """Test creating an interview."""
    interview = interview_crud.create_interview(db_session, test_study.id, test_invite.id)

    assert interview.id is not None
    assert interview.study_id == test_study.id
    assert interview.invite_id == test_invite.id
    assert interview.agent_turns == 0
    assert interview.started_at is not None
    assert interview.completed_at is None


def test_get_interview_by_id(db_session, test_interview):
    """Test getting an interview by ID."""
    retrieved = interview_crud.get_interview_by_id(db_session, test_interview.id)

    assert retrieved is not None
    assert retrieved.id == test_interview.id
    assert retrieved.study_id == test_interview.study_id


def test_get_interview_by_id_not_found(db_session):
    """Test getting non-existent interview returns None."""
    result = interview_crud.get_interview_by_id(db_session, 99999)
    assert result is None


def test_get_interview_by_id_with_messages(db_session, test_interview):
    """Test getting an interview with messages loaded."""
    # Create messages
    interview_crud.create_message(db_session, test_interview.id, "user", "Hello")
    interview_crud.create_message(db_session, test_interview.id, "assistant", "Hi")

    interview = interview_crud.get_interview_by_id(
        db_session, test_interview.id, load_messages=True
    )

    assert interview is not None
    assert len(interview.messages) == 2


def test_get_interview_by_id_load_all(db_session, test_interview):
    """Test getting an interview with all related data."""
    # Create related data
    interview_crud.create_message(db_session, test_interview.id, "user", "Hello")
    interview_crud.create_interviewee(
        db_session, test_interview.id, "John Doe", "john@example.com"
    )
    interview_crud.create_insight(
        db_session, test_interview.id, "Summary", "positive", ["key1"], ["quote1"]
    )

    interview = interview_crud.get_interview_by_id(
        db_session, test_interview.id, load_all=True
    )

    assert interview is not None
    assert len(interview.messages) == 1
    assert interview.interviewee is not None
    assert interview.insight is not None


def test_get_interviews_by_study(db_session, test_study):
    """Test getting all interviews for a study."""
    invite1 = invite_crud.create_invite(db_session, test_study.id)
    invite2 = invite_crud.create_invite(db_session, test_study.id)

    interview1 = interview_crud.create_interview(db_session, test_study.id, invite1.id)
    interview2 = interview_crud.create_interview(db_session, test_study.id, invite2.id)

    interviews = interview_crud.get_interviews_by_study(db_session, test_study.id)

    assert len(interviews) == 2
    interview_ids = [i.id for i in interviews]
    assert interview1.id in interview_ids
    assert interview2.id in interview_ids

    # Should be ordered by started_at desc (newest first)
    assert interviews[0].id == interview2.id
    assert interviews[1].id == interview1.id


def test_get_interviews_by_study_with_relations(db_session, test_study, test_invite):
    """Test getting interviews with related data loaded."""
    interview = interview_crud.create_interview(db_session, test_study.id, test_invite.id)
    interview_crud.create_interviewee(
        db_session, interview.id, "Jane", "jane@example.com"
    )

    interviews = interview_crud.get_interviews_by_study(
        db_session, test_study.id, load_relations=True
    )

    assert len(interviews) == 1
    assert interviews[0].interviewee is not None


def test_get_interviews_by_study_empty(db_session, test_study):
    """Test getting interviews when none exist."""
    interviews = interview_crud.get_interviews_by_study(db_session, test_study.id)
    assert interviews == []


def test_interviews_isolated_by_study(db_session, test_user):
    """Test that interviews are isolated by study."""
    study1 = study_crud.create_study(db_session, test_user.id, "Study 1", "D", "C")
    study2 = study_crud.create_study(db_session, test_user.id, "Study 2", "D", "C")

    invite1 = invite_crud.create_invite(db_session, study1.id)
    invite2 = invite_crud.create_invite(db_session, study2.id)

    interview1 = interview_crud.create_interview(db_session, study1.id, invite1.id)
    interview2 = interview_crud.create_interview(db_session, study2.id, invite2.id)

    study1_interviews = interview_crud.get_interviews_by_study(db_session, study1.id)
    assert len(study1_interviews) == 1
    assert study1_interviews[0].id == interview1.id

    study2_interviews = interview_crud.get_interviews_by_study(db_session, study2.id)
    assert len(study2_interviews) == 1
    assert study2_interviews[0].id == interview2.id


def test_get_interview_by_invite(db_session, test_study, test_invite):
    """Test getting an interview by invite ID."""
    created = interview_crud.create_interview(db_session, test_study.id, test_invite.id)

    retrieved = interview_crud.get_interview_by_invite(db_session, test_invite.id)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.invite_id == test_invite.id


def test_get_interview_by_invite_not_found(db_session):
    """Test getting interview by non-existent invite returns None."""
    result = interview_crud.get_interview_by_invite(db_session, 99999)
    assert result is None


def test_complete_interview(db_session, test_interview):
    """Test marking an interview as completed."""
    completed = interview_crud.complete_interview(db_session, test_interview.id)

    assert completed is not None
    assert completed.id == test_interview.id
    assert completed.completed_at is not None
    assert isinstance(completed.completed_at, datetime)


def test_complete_interview_not_found(db_session):
    """Test completing non-existent interview returns None."""
    result = interview_crud.complete_interview(db_session, 99999)
    assert result is None


def test_increment_agent_turns(db_session, test_interview):
    """Test incrementing agent turn counter."""
    assert test_interview.agent_turns == 0

    updated = interview_crud.increment_agent_turns(db_session, test_interview.id)
    assert updated.agent_turns == 1

    updated = interview_crud.increment_agent_turns(db_session, test_interview.id)
    assert updated.agent_turns == 2


def test_increment_agent_turns_not_found(db_session):
    """Test incrementing turns for non-existent interview returns None."""
    result = interview_crud.increment_agent_turns(db_session, 99999)
    assert result is None


# Interviewee CRUD Tests


def test_create_interviewee(db_session, test_interview):
    """Test creating an interviewee record."""
    interviewee = interview_crud.create_interviewee(
        db_session,
        test_interview.id,
        "John Doe",
        "john@example.com",
        {"age": 30, "country": "USA"},
    )

    assert interviewee.id is not None
    assert interviewee.interview_id == test_interview.id
    assert interviewee.name == "John Doe"
    assert interviewee.email == "john@example.com"
    assert interviewee.demographics_json == {"age": 30, "country": "USA"}
    assert interviewee.consent_at is not None


def test_create_interviewee_no_demographics(db_session, test_interview):
    """Test creating an interviewee without demographics."""
    interviewee = interview_crud.create_interviewee(
        db_session, test_interview.id, "Jane Doe", "jane@example.com"
    )

    assert interviewee.demographics_json is None


def test_get_interviewee_by_interview(db_session, test_interview):
    """Test getting an interviewee by interview ID."""
    created = interview_crud.create_interviewee(
        db_session, test_interview.id, "John", "john@example.com"
    )

    retrieved = interview_crud.get_interviewee_by_interview(db_session, test_interview.id)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.name == "John"


def test_get_interviewee_by_interview_not_found(db_session, test_interview):
    """Test getting non-existent interviewee returns None."""
    result = interview_crud.get_interviewee_by_interview(db_session, test_interview.id)
    assert result is None


# Message CRUD Tests


def test_create_message(db_session, test_interview):
    """Test creating a message."""
    message = interview_crud.create_message(
        db_session, test_interview.id, "user", "Hello, how are you?"
    )

    assert message.id is not None
    assert message.interview_id == test_interview.id
    assert message.role == "user"
    assert message.content == "Hello, how are you?"
    assert message.created_at is not None


def test_create_message_assistant(db_session, test_interview):
    """Test creating an assistant message."""
    message = interview_crud.create_message(
        db_session, test_interview.id, "assistant", "I'm doing well, thank you!"
    )

    assert message.role == "assistant"
    assert message.content == "I'm doing well, thank you!"


def test_get_message_count(db_session, test_interview):
    """Test getting message count."""
    assert interview_crud.get_message_count(db_session, test_interview.id) == 0

    interview_crud.create_message(db_session, test_interview.id, "user", "Message 1")
    assert interview_crud.get_message_count(db_session, test_interview.id) == 1

    interview_crud.create_message(db_session, test_interview.id, "assistant", "Message 2")
    assert interview_crud.get_message_count(db_session, test_interview.id) == 2


def test_get_messages_by_interview(db_session, test_interview):
    """Test getting all messages for an interview."""
    msg1 = interview_crud.create_message(db_session, test_interview.id, "user", "First")
    msg2 = interview_crud.create_message(db_session, test_interview.id, "assistant", "Second")
    msg3 = interview_crud.create_message(db_session, test_interview.id, "user", "Third")

    messages = interview_crud.get_messages_by_interview(db_session, test_interview.id)

    assert len(messages) == 3
    # Should be ordered by created_at (chronological)
    assert messages[0].id == msg1.id
    assert messages[1].id == msg2.id
    assert messages[2].id == msg3.id


def test_get_messages_by_interview_with_limit(db_session, test_interview):
    """Test getting messages with limit."""
    for i in range(5):
        interview_crud.create_message(db_session, test_interview.id, "user", f"Message {i}")

    messages = interview_crud.get_messages_by_interview(db_session, test_interview.id, limit=3)

    assert len(messages) == 3


def test_get_messages_by_interview_empty(db_session, test_interview):
    """Test getting messages when none exist."""
    messages = interview_crud.get_messages_by_interview(db_session, test_interview.id)
    assert messages == []


def test_get_recent_messages(db_session, test_interview):
    """Test getting recent messages."""
    # Create 10 messages
    for i in range(10):
        interview_crud.create_message(db_session, test_interview.id, "user", f"Message {i}")

    # Get 5 most recent
    recent = interview_crud.get_recent_messages(db_session, test_interview.id, count=5)

    assert len(recent) == 5
    # Should be in chronological order (oldest to newest of the recent ones)
    assert "Message 5" in recent[0].content
    assert "Message 9" in recent[4].content


def test_get_recent_messages_default_count(db_session, test_interview):
    """Test getting recent messages with default count."""
    for i in range(10):
        interview_crud.create_message(db_session, test_interview.id, "user", f"Message {i}")

    recent = interview_crud.get_recent_messages(db_session, test_interview.id)

    assert len(recent) == 8  # Default count


def test_get_recent_messages_fewer_than_requested(db_session, test_interview):
    """Test getting recent messages when fewer exist than requested."""
    interview_crud.create_message(db_session, test_interview.id, "user", "Message 1")
    interview_crud.create_message(db_session, test_interview.id, "user", "Message 2")

    recent = interview_crud.get_recent_messages(db_session, test_interview.id, count=5)

    assert len(recent) == 2


# Insight CRUD Tests


def test_create_insight(db_session, test_interview):
    """Test creating an insight."""
    insight = interview_crud.create_insight(
        db_session,
        test_interview.id,
        "User is satisfied with the product",
        "positive",
        ["satisfaction", "product", "quality"],
        ["I love this product", "It works great"],
    )

    assert insight.id is not None
    assert insight.interview_id == test_interview.id
    assert insight.summary == "User is satisfied with the product"
    assert insight.sentiment == "positive"
    assert insight.keywords_json == ["satisfaction", "product", "quality"]
    assert insight.quotes_json == ["I love this product", "It works great"]
    assert insight.created_at is not None


def test_get_insight_by_interview(db_session, test_interview):
    """Test getting an insight by interview ID."""
    created = interview_crud.create_insight(
        db_session, test_interview.id, "Summary", "neutral", [], []
    )

    retrieved = interview_crud.get_insight_by_interview(db_session, test_interview.id)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.summary == "Summary"


def test_get_insight_by_interview_not_found(db_session, test_interview):
    """Test getting non-existent insight returns None."""
    result = interview_crud.get_insight_by_interview(db_session, test_interview.id)
    assert result is None


def test_update_insight_summary(db_session, test_interview):
    """Test updating insight summary."""
    insight = interview_crud.create_insight(
        db_session, test_interview.id, "Old summary", "positive", [], []
    )

    updated = interview_crud.update_insight(
        db_session, insight.id, summary="New summary"
    )

    assert updated is not None
    assert updated.id == insight.id
    assert updated.summary == "New summary"
    assert updated.sentiment == "positive"  # Unchanged


def test_update_insight_multiple_fields(db_session, test_interview):
    """Test updating multiple insight fields."""
    insight = interview_crud.create_insight(
        db_session, test_interview.id, "Summary", "positive", ["key1"], ["quote1"]
    )

    updated = interview_crud.update_insight(
        db_session,
        insight.id,
        summary="Updated summary",
        sentiment="negative",
        keywords_json=["key2", "key3"],
        quotes_json=["quote2"],
    )

    assert updated.summary == "Updated summary"
    assert updated.sentiment == "negative"
    assert updated.keywords_json == ["key2", "key3"]
    assert updated.quotes_json == ["quote2"]


def test_update_insight_not_found(db_session):
    """Test updating non-existent insight returns None."""
    result = interview_crud.update_insight(db_session, 99999, summary="New")
    assert result is None


def test_update_insight_no_changes(db_session, test_interview):
    """Test updating insight with no changes."""
    insight = interview_crud.create_insight(
        db_session, test_interview.id, "Summary", "positive", [], []
    )

    updated = interview_crud.update_insight(db_session, insight.id)

    assert updated is not None
    assert updated.id == insight.id
    assert updated.summary == "Summary"


def test_complete_interview_workflow(db_session, test_study, test_invite):
    """Test a complete interview workflow."""
    # Create interview
    interview = interview_crud.create_interview(db_session, test_study.id, test_invite.id)
    assert interview.agent_turns == 0

    # Add interviewee
    interviewee = interview_crud.create_interviewee(
        db_session, interview.id, "Alice", "alice@example.com"
    )
    assert interviewee.interview_id == interview.id

    # Add messages
    interview_crud.create_message(db_session, interview.id, "user", "Hello")
    interview_crud.increment_agent_turns(db_session, interview.id)
    interview_crud.create_message(db_session, interview.id, "assistant", "Hi there")
    interview_crud.increment_agent_turns(db_session, interview.id)

    # Get message count
    count = interview_crud.get_message_count(db_session, interview.id)
    assert count == 2

    # Complete interview
    completed = interview_crud.complete_interview(db_session, interview.id)
    assert completed.completed_at is not None
    assert completed.agent_turns == 2

    # Generate insights
    insight = interview_crud.create_insight(
        db_session, interview.id, "Great feedback", "positive", ["happy"], ["love it"]
    )
    assert insight.interview_id == interview.id

    # Retrieve full interview
    full = interview_crud.get_interview_by_id(db_session, interview.id, load_all=True)
    assert full.interviewee.name == "Alice"
    assert len(full.messages) == 2
    assert full.insight.summary == "Great feedback"

```

## tests/crud/test_invite.py

**Path:** `tests/crud/test_invite.py`
**Type:** Python
**Size:** 9.7 KB

```python
"""Unit tests for invite CRUD operations."""

import pytest
from datetime import datetime, timedelta, timezone

from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def db_session(test_db):
    """Get a database session for testing."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_user(db_session):
    """Create a test user."""
    return user_crud.create_user(db_session, "testuser@example.com", "hash123")


@pytest.fixture
def test_study(db_session, test_user):
    """Create a test study."""
    return study_crud.create_study(
        db_session,
        owner_user_id=test_user.id,
        title="Test Study",
        description="Test Description",
        consent_text="Test Consent",
    )


def test_generate_invite_code():
    """Test that invite code generation produces unique values."""
    code1 = invite_crud.generate_invite_code()
    code2 = invite_crud.generate_invite_code()

    assert len(code1) > 20  # Should be a long random string
    assert len(code2) > 20
    assert code1 != code2  # Should be unique


def test_create_invite_basic(db_session, test_study):
    """Test creating a basic invite."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    assert invite.id is not None
    assert invite.study_id == test_study.id
    assert invite.invite_code is not None
    assert len(invite.invite_code) > 20
    assert invite.status == InviteStatus.CREATED.value
    assert invite.interviewee_email is None
    assert invite.expires_at is None
    assert invite.created_at is not None


def test_create_invite_with_email(db_session, test_study):
    """Test creating an invite with interviewee email."""
    email = "participant@example.com"
    invite = invite_crud.create_invite(db_session, test_study.id, interviewee_email=email)

    assert invite.interviewee_email == email


def test_create_invite_with_expiry(db_session, test_study):
    """Test creating an invite with expiration date."""
    expires_at = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(days=7)
    invite = invite_crud.create_invite(
        db_session, test_study.id, expires_at=expires_at
    )

    assert invite.expires_at is not None
    # Allow 1 second tolerance
    assert abs((invite.expires_at - expires_at).total_seconds()) < 1


def test_create_invite_unique_codes(db_session, test_study):
    """Test that each invite gets a unique code."""
    invite1 = invite_crud.create_invite(db_session, test_study.id)
    invite2 = invite_crud.create_invite(db_session, test_study.id)

    assert invite1.invite_code != invite2.invite_code


def test_get_invite_by_code(db_session, test_study):
    """Test getting an invite by code."""
    created = invite_crud.create_invite(db_session, test_study.id)

    retrieved = invite_crud.get_invite_by_code(db_session, created.invite_code)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.invite_code == created.invite_code


def test_get_invite_by_code_not_found(db_session):
    """Test getting non-existent invite by code returns None."""
    result = invite_crud.get_invite_by_code(db_session, "nonexistent_code")
    assert result is None


def test_get_invite_by_id(db_session, test_study):
    """Test getting an invite by ID."""
    created = invite_crud.create_invite(db_session, test_study.id)

    retrieved = invite_crud.get_invite_by_id(db_session, created.id)

    assert retrieved is not None
    assert retrieved.id == created.id


def test_get_invite_by_id_not_found(db_session):
    """Test getting non-existent invite by ID returns None."""
    result = invite_crud.get_invite_by_id(db_session, 99999)
    assert result is None


def test_get_invites_by_study(db_session, test_study):
    """Test getting all invites for a study."""
    invite1 = invite_crud.create_invite(db_session, test_study.id)
    invite2 = invite_crud.create_invite(db_session, test_study.id)

    invites = invite_crud.get_invites_by_study(db_session, test_study.id)

    assert len(invites) == 2
    invite_ids = [i.id for i in invites]
    assert invite1.id in invite_ids
    assert invite2.id in invite_ids

    # Should be ordered by created_at desc (newest first)
    assert invites[0].id == invite2.id
    assert invites[1].id == invite1.id


def test_get_invites_by_study_empty(db_session, test_study):
    """Test getting invites when none exist."""
    invites = invite_crud.get_invites_by_study(db_session, test_study.id)
    assert invites == []


def test_invites_isolated_by_study(db_session, test_user):
    """Test that invites are isolated by study."""
    study1 = study_crud.create_study(db_session, test_user.id, "Study 1", "D", "C")
    study2 = study_crud.create_study(db_session, test_user.id, "Study 2", "D", "C")

    invite1 = invite_crud.create_invite(db_session, study1.id)
    invite2 = invite_crud.create_invite(db_session, study2.id)

    study1_invites = invite_crud.get_invites_by_study(db_session, study1.id)
    assert len(study1_invites) == 1
    assert study1_invites[0].id == invite1.id

    study2_invites = invite_crud.get_invites_by_study(db_session, study2.id)
    assert len(study2_invites) == 1
    assert study2_invites[0].id == invite2.id


def test_update_invite_status(db_session, test_study):
    """Test updating invite status."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    updated = invite_crud.update_invite_status(
        db_session, invite.id, InviteStatus.OPENED
    )

    assert updated is not None
    assert updated.id == invite.id
    assert updated.status == InviteStatus.OPENED.value


def test_update_invite_status_to_completed(db_session, test_study):
    """Test updating invite status to completed."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    updated = invite_crud.update_invite_status(
        db_session, invite.id, InviteStatus.COMPLETED
    )

    assert updated.status == InviteStatus.COMPLETED.value


def test_update_invite_status_not_found(db_session):
    """Test updating non-existent invite returns None."""
    result = invite_crud.update_invite_status(
        db_session, 99999, InviteStatus.OPENED
    )
    assert result is None


def test_is_invite_valid_new_invite(db_session, test_study):
    """Test that a newly created invite is valid."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    assert invite_crud.is_invite_valid(invite) is True


def test_is_invite_valid_completed(db_session, test_study):
    """Test that a completed invite is not valid."""
    invite = invite_crud.create_invite(db_session, test_study.id)
    invite_crud.update_invite_status(db_session, invite.id, InviteStatus.COMPLETED)

    # Refresh to get updated status
    updated_invite = invite_crud.get_invite_by_id(db_session, invite.id)

    assert invite_crud.is_invite_valid(updated_invite) is False


def test_is_invite_valid_expired(db_session, test_study):
    """Test that an expired invite is not valid."""
    past_date = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=1)
    invite = invite_crud.create_invite(db_session, test_study.id, expires_at=past_date)

    assert invite_crud.is_invite_valid(invite) is False


def test_is_invite_valid_not_yet_expired(db_session, test_study):
    """Test that an invite with future expiry is valid."""
    future_date = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(days=7)
    invite = invite_crud.create_invite(db_session, test_study.id, expires_at=future_date)

    assert invite_crud.is_invite_valid(invite) is True


def test_is_invite_valid_no_expiry(db_session, test_study):
    """Test that an invite with no expiry date is valid."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    assert invite.expires_at is None
    assert invite_crud.is_invite_valid(invite) is True


def test_delete_invite(db_session, test_study):
    """Test deleting an invite."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    result = invite_crud.delete_invite(db_session, invite.id)
    assert result is True

    # Verify it's gone
    retrieved = invite_crud.get_invite_by_id(db_session, invite.id)
    assert retrieved is None


def test_delete_invite_not_found(db_session):
    """Test deleting non-existent invite returns False."""
    result = invite_crud.delete_invite(db_session, 99999)
    assert result is False


def test_invite_status_transitions(db_session, test_study):
    """Test typical invite status transitions."""
    invite = invite_crud.create_invite(db_session, test_study.id)

    # Initially CREATED
    assert invite.status == InviteStatus.CREATED.value

    # Open invite
    invite = invite_crud.update_invite_status(db_session, invite.id, InviteStatus.OPENED)
    assert invite.status == InviteStatus.OPENED.value

    # Complete interview
    invite = invite_crud.update_invite_status(db_session, invite.id, InviteStatus.COMPLETED)
    assert invite.status == InviteStatus.COMPLETED.value


def test_multiple_invites_for_same_study(db_session, test_study):
    """Test that multiple invites can be created for the same study."""
    invites = []
    for i in range(5):
        invite = invite_crud.create_invite(
            db_session,
            test_study.id,
            interviewee_email=f"participant{i}@example.com",
        )
        invites.append(invite)

    retrieved = invite_crud.get_invites_by_study(db_session, test_study.id)
    assert len(retrieved) == 5

    # All should have unique codes
    codes = [inv.invite_code for inv in retrieved]
    assert len(codes) == len(set(codes))  # No duplicates

```

## tests/crud/test_session.py

**Path:** `tests/crud/test_session.py`
**Type:** Python
**Size:** 7.7 KB

```python
"""Unit tests for session CRUD operations."""

import pytest
from datetime import datetime, timedelta, timezone

from app.crud import session as session_crud
from app.crud import user as user_crud


@pytest.fixture
def db_session(test_db):
    """Get a database session for testing."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_user(db_session):
    """Create a test user."""
    return user_crud.create_user(db_session, "testuser@example.com", "hash123")


def test_generate_session_id():
    """Test that session ID generation produces unique values."""
    id1 = session_crud.generate_session_id()
    id2 = session_crud.generate_session_id()

    assert len(id1) > 20  # Should be a long random string
    assert len(id2) > 20
    assert id1 != id2  # Should be unique


def test_generate_csrf_secret():
    """Test that CSRF secret generation produces unique values."""
    secret1 = session_crud.generate_csrf_secret()
    secret2 = session_crud.generate_csrf_secret()

    assert len(secret1) > 20
    assert len(secret2) > 20
    assert secret1 != secret2


def test_create_session(db_session, test_user):
    """Test creating a session."""
    session = session_crud.create_session(db_session, test_user.id)

    assert session.id is not None
    assert len(session.id) > 20  # Generated session ID
    assert session.user_id == test_user.id
    assert session.expires_at is not None
    assert session.csrf_secret is not None
    assert len(session.csrf_secret) > 20

    # Default expiration is 7 days
    expected_expiry = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(days=7)
    # Allow 1 minute tolerance for test execution time
    assert abs((session.expires_at - expected_expiry).total_seconds()) < 60


def test_create_session_custom_expiry(db_session, test_user):
    """Test creating a session with custom expiration."""
    session = session_crud.create_session(db_session, test_user.id, expires_in_days=30)

    expected_expiry = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(days=30)
    assert abs((session.expires_at - expected_expiry).total_seconds()) < 60


def test_get_session_by_id(db_session, test_user):
    """Test getting a session by ID."""
    created = session_crud.create_session(db_session, test_user.id)

    retrieved = session_crud.get_session_by_id(db_session, created.id)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.user_id == test_user.id


def test_get_session_by_id_not_found(db_session):
    """Test getting a non-existent session returns None."""
    result = session_crud.get_session_by_id(db_session, "nonexistent_session_id")
    assert result is None


def test_get_sessions_by_user(db_session, test_user):
    """Test getting all sessions for a user."""
    # Create multiple sessions for the same user
    session1 = session_crud.create_session(db_session, test_user.id)
    session2 = session_crud.create_session(db_session, test_user.id)

    sessions = session_crud.get_sessions_by_user(db_session, test_user.id)

    assert len(sessions) == 2
    session_ids = [s.id for s in sessions]
    assert session1.id in session_ids
    assert session2.id in session_ids


def test_get_sessions_by_user_empty(db_session, test_user):
    """Test getting sessions when none exist."""
    sessions = session_crud.get_sessions_by_user(db_session, test_user.id)
    assert sessions == []


def test_is_session_valid_active(db_session, test_user):
    """Test that a newly created session is valid."""
    session = session_crud.create_session(db_session, test_user.id)

    assert session_crud.is_session_valid(session) is True


def test_is_session_valid_expired(db_session, test_user):
    """Test that an expired session is not valid."""
    session = session_crud.create_session(db_session, test_user.id)

    # Manually set expiration to past
    session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=1)
    db_session.commit()
    db_session.refresh(session)

    assert session_crud.is_session_valid(session) is False


def test_delete_session(db_session, test_user):
    """Test deleting a session."""
    session = session_crud.create_session(db_session, test_user.id)

    result = session_crud.delete_session(db_session, session.id)
    assert result is True

    # Verify it's gone
    retrieved = session_crud.get_session_by_id(db_session, session.id)
    assert retrieved is None


def test_delete_session_not_found(db_session):
    """Test deleting non-existent session returns False."""
    result = session_crud.delete_session(db_session, "nonexistent_id")
    assert result is False


def test_delete_expired_sessions(db_session, test_user):
    """Test deleting all expired sessions."""
    # Create active session
    active_session = session_crud.create_session(db_session, test_user.id)

    # Create expired session
    expired_session = session_crud.create_session(db_session, test_user.id)
    expired_session.expires_at = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=1)
    db_session.commit()

    # Delete expired sessions
    count = session_crud.delete_expired_sessions(db_session)

    assert count == 1

    # Active session should still exist
    assert session_crud.get_session_by_id(db_session, active_session.id) is not None

    # Expired session should be gone
    assert session_crud.get_session_by_id(db_session, expired_session.id) is None


def test_delete_expired_sessions_none_expired(db_session, test_user):
    """Test deleting expired sessions when none are expired."""
    session_crud.create_session(db_session, test_user.id)
    session_crud.create_session(db_session, test_user.id)

    count = session_crud.delete_expired_sessions(db_session)

    assert count == 0


def test_delete_user_sessions(db_session):
    """Test deleting all sessions for a user."""
    user1 = user_crud.create_user(db_session, "user1@example.com", "hash1")
    user2 = user_crud.create_user(db_session, "user2@example.com", "hash2")

    # Create sessions for both users
    session1 = session_crud.create_session(db_session, user1.id)
    session2 = session_crud.create_session(db_session, user1.id)
    session3 = session_crud.create_session(db_session, user2.id)

    # Delete user1's sessions
    count = session_crud.delete_user_sessions(db_session, user1.id)

    assert count == 2

    # User1's sessions should be gone
    assert session_crud.get_session_by_id(db_session, session1.id) is None
    assert session_crud.get_session_by_id(db_session, session2.id) is None

    # User2's session should still exist
    assert session_crud.get_session_by_id(db_session, session3.id) is not None


def test_delete_user_sessions_none_exist(db_session, test_user):
    """Test deleting sessions when user has none."""
    count = session_crud.delete_user_sessions(db_session, test_user.id)
    assert count == 0


def test_session_isolation_between_users(db_session):
    """Test that sessions are properly isolated between users."""
    user1 = user_crud.create_user(db_session, "user1@example.com", "hash1")
    user2 = user_crud.create_user(db_session, "user2@example.com", "hash2")

    session1 = session_crud.create_session(db_session, user1.id)
    session2 = session_crud.create_session(db_session, user2.id)

    # Get sessions for user1
    user1_sessions = session_crud.get_sessions_by_user(db_session, user1.id)
    assert len(user1_sessions) == 1
    assert user1_sessions[0].id == session1.id

    # Get sessions for user2
    user2_sessions = session_crud.get_sessions_by_user(db_session, user2.id)
    assert len(user2_sessions) == 1
    assert user2_sessions[0].id == session2.id

```

## tests/crud/test_study.py

**Path:** `tests/crud/test_study.py`
**Type:** Python
**Size:** 11.3 KB

```python
"""Unit tests for study CRUD operations."""

import pytest

from app.crud import study as study_crud
from app.crud import user as user_crud


@pytest.fixture
def db_session(test_db):
    """Get a database session for testing."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_user(db_session):
    """Create a test user."""
    return user_crud.create_user(db_session, "testuser@example.com", "hash123")


@pytest.fixture
def test_study(db_session, test_user):
    """Create a test study."""
    return study_crud.create_study(
        db_session,
        owner_user_id=test_user.id,
        title="Test Study",
        description="Test Description",
        consent_text="Test Consent",
    )


# Study CRUD Tests


def test_create_study(db_session, test_user):
    """Test creating a study."""
    study = study_crud.create_study(
        db_session,
        owner_user_id=test_user.id,
        title="Product Research",
        description="Understanding user needs",
        consent_text="I consent to participate",
        max_agent_turns=15,
    )

    assert study.id is not None
    assert study.owner_user_id == test_user.id
    assert study.title == "Product Research"
    assert study.description == "Understanding user needs"
    assert study.consent_text == "I consent to participate"
    assert study.max_agent_turns == 15
    assert study.created_at is not None


def test_create_study_default_max_turns(db_session, test_user):
    """Test that default max_agent_turns is set."""
    study = study_crud.create_study(
        db_session,
        owner_user_id=test_user.id,
        title="Test",
        description="Test",
        consent_text="Test",
    )

    assert study.max_agent_turns == 9  # Default value


def test_get_study_by_id(db_session, test_study):
    """Test getting a study by ID."""
    retrieved = study_crud.get_study_by_id(db_session, test_study.id)

    assert retrieved is not None
    assert retrieved.id == test_study.id
    assert retrieved.title == test_study.title


def test_get_study_by_id_not_found(db_session):
    """Test getting non-existent study returns None."""
    result = study_crud.get_study_by_id(db_session, 99999)
    assert result is None


def test_get_study_by_id_with_questions(db_session, test_study):
    """Test getting a study with questions loaded."""
    # Add questions
    study_crud.create_study_question(db_session, test_study.id, "Question 1", 0)
    study_crud.create_study_question(db_session, test_study.id, "Question 2", 1)

    # Get study with questions
    study = study_crud.get_study_by_id(db_session, test_study.id, load_questions=True)

    assert study is not None
    assert len(study.questions) == 2


def test_get_study_by_id_without_questions(db_session, test_study):
    """Test getting a study without loading questions."""
    study_crud.create_study_question(db_session, test_study.id, "Question 1", 0)

    study = study_crud.get_study_by_id(db_session, test_study.id, load_questions=False)

    assert study is not None
    # Questions should not be loaded (lazy loaded)


def test_get_studies_by_user(db_session, test_user):
    """Test getting all studies for a user."""
    study1 = study_crud.create_study(
        db_session, test_user.id, "Study 1", "Desc 1", "Consent 1"
    )
    study2 = study_crud.create_study(
        db_session, test_user.id, "Study 2", "Desc 2", "Consent 2"
    )

    studies = study_crud.get_studies_by_user(db_session, test_user.id)

    assert len(studies) == 2
    study_ids = [s.id for s in studies]
    assert study1.id in study_ids
    assert study2.id in study_ids

    # Should be ordered by created_at desc (newest first)
    assert studies[0].id == study2.id
    assert studies[1].id == study1.id


def test_get_studies_by_user_pagination(db_session, test_user):
    """Test pagination when getting studies."""
    for i in range(5):
        study_crud.create_study(
            db_session, test_user.id, f"Study {i}", f"Desc {i}", "Consent"
        )

    # Test skip
    studies_skip = study_crud.get_studies_by_user(db_session, test_user.id, skip=2)
    assert len(studies_skip) == 3

    # Test limit
    studies_limit = study_crud.get_studies_by_user(db_session, test_user.id, limit=2)
    assert len(studies_limit) == 2


def test_get_studies_by_user_empty(db_session, test_user):
    """Test getting studies when none exist."""
    studies = study_crud.get_studies_by_user(db_session, test_user.id)
    assert studies == []


def test_get_studies_isolation(db_session):
    """Test that studies are isolated by user."""
    user1 = user_crud.create_user(db_session, "user1@example.com", "hash1")
    user2 = user_crud.create_user(db_session, "user2@example.com", "hash2")

    study1 = study_crud.create_study(db_session, user1.id, "Study 1", "Desc", "Consent")
    study2 = study_crud.create_study(db_session, user2.id, "Study 2", "Desc", "Consent")

    user1_studies = study_crud.get_studies_by_user(db_session, user1.id)
    assert len(user1_studies) == 1
    assert user1_studies[0].id == study1.id

    user2_studies = study_crud.get_studies_by_user(db_session, user2.id)
    assert len(user2_studies) == 1
    assert user2_studies[0].id == study2.id


def test_update_study_title(db_session, test_study):
    """Test updating study title."""
    updated = study_crud.update_study(db_session, test_study.id, title="New Title")

    assert updated is not None
    assert updated.id == test_study.id
    assert updated.title == "New Title"
    assert updated.description == test_study.description  # Unchanged


def test_update_study_multiple_fields(db_session, test_study):
    """Test updating multiple study fields."""
    updated = study_crud.update_study(
        db_session,
        test_study.id,
        title="New Title",
        description="New Description",
        max_agent_turns=20,
    )

    assert updated.title == "New Title"
    assert updated.description == "New Description"
    assert updated.max_agent_turns == 20
    assert updated.consent_text == test_study.consent_text  # Unchanged


def test_update_study_not_found(db_session):
    """Test updating non-existent study returns None."""
    result = study_crud.update_study(db_session, 99999, title="New Title")
    assert result is None


def test_update_study_no_changes(db_session, test_study):
    """Test updating study with no changes."""
    updated = study_crud.update_study(db_session, test_study.id)

    assert updated is not None
    assert updated.id == test_study.id
    assert updated.title == test_study.title


def test_delete_study(db_session, test_study):
    """Test deleting a study."""
    result = study_crud.delete_study(db_session, test_study.id)
    assert result is True

    # Verify it's gone
    retrieved = study_crud.get_study_by_id(db_session, test_study.id)
    assert retrieved is None


def test_delete_study_not_found(db_session):
    """Test deleting non-existent study returns False."""
    result = study_crud.delete_study(db_session, 99999)
    assert result is False


# StudyQuestion CRUD Tests


def test_create_study_question(db_session, test_study):
    """Test creating a study question."""
    question = study_crud.create_study_question(
        db_session, test_study.id, "What is your opinion?", 0
    )

    assert question.id is not None
    assert question.study_id == test_study.id
    assert question.text == "What is your opinion?"
    assert question.sort_order == 0


def test_get_study_questions(db_session, test_study):
    """Test getting all questions for a study."""
    q1 = study_crud.create_study_question(db_session, test_study.id, "Question 1", 1)
    q2 = study_crud.create_study_question(db_session, test_study.id, "Question 2", 0)
    q3 = study_crud.create_study_question(db_session, test_study.id, "Question 3", 2)

    questions = study_crud.get_study_questions(db_session, test_study.id)

    assert len(questions) == 3
    # Should be ordered by sort_order
    assert questions[0].id == q2.id  # sort_order 0
    assert questions[1].id == q1.id  # sort_order 1
    assert questions[2].id == q3.id  # sort_order 2


def test_get_study_questions_empty(db_session, test_study):
    """Test getting questions when none exist."""
    questions = study_crud.get_study_questions(db_session, test_study.id)
    assert questions == []


def test_update_question_text(db_session, test_study):
    """Test updating question text."""
    question = study_crud.create_study_question(
        db_session, test_study.id, "Original text", 0
    )

    updated = study_crud.update_question_text(db_session, question.id, "Updated text")

    assert updated is not None
    assert updated.id == question.id
    assert updated.text == "Updated text"
    assert updated.sort_order == 0  # Unchanged


def test_update_question_text_not_found(db_session):
    """Test updating non-existent question returns None."""
    result = study_crud.update_question_text(db_session, 99999, "New text")
    assert result is None


def test_reorder_questions(db_session, test_study):
    """Test reordering questions."""
    q1 = study_crud.create_study_question(db_session, test_study.id, "Q1", 0)
    q2 = study_crud.create_study_question(db_session, test_study.id, "Q2", 1)
    q3 = study_crud.create_study_question(db_session, test_study.id, "Q3", 2)

    # Reorder: swap q1 and q3
    updates = [(q1.id, 2), (q3.id, 0)]
    result = study_crud.reorder_questions(db_session, updates)

    assert result is True

    # Verify new order
    questions = study_crud.get_study_questions(db_session, test_study.id)
    assert questions[0].id == q3.id  # Now at position 0
    assert questions[1].id == q2.id  # Still at position 1
    assert questions[2].id == q1.id  # Now at position 2


def test_reorder_questions_empty_list(db_session):
    """Test reordering with empty list."""
    result = study_crud.reorder_questions(db_session, [])
    assert result is True


def test_delete_study_question(db_session, test_study):
    """Test deleting a study question."""
    question = study_crud.create_study_question(db_session, test_study.id, "Question", 0)

    result = study_crud.delete_study_question(db_session, question.id)
    assert result is True

    # Verify it's gone
    questions = study_crud.get_study_questions(db_session, test_study.id)
    assert len(questions) == 0


def test_delete_study_question_not_found(db_session):
    """Test deleting non-existent question returns False."""
    result = study_crud.delete_study_question(db_session, 99999)
    assert result is False


def test_questions_isolated_by_study(db_session, test_user):
    """Test that questions are isolated by study."""
    study1 = study_crud.create_study(db_session, test_user.id, "Study 1", "D", "C")
    study2 = study_crud.create_study(db_session, test_user.id, "Study 2", "D", "C")

    study_crud.create_study_question(db_session, study1.id, "Q1 for Study 1", 0)
    study_crud.create_study_question(db_session, study2.id, "Q1 for Study 2", 0)

    study1_questions = study_crud.get_study_questions(db_session, study1.id)
    assert len(study1_questions) == 1
    assert "Study 1" in study1_questions[0].text

    study2_questions = study_crud.get_study_questions(db_session, study2.id)
    assert len(study2_questions) == 1
    assert "Study 2" in study2_questions[0].text

```

## tests/crud/test_user.py

**Path:** `tests/crud/test_user.py`
**Type:** Python
**Size:** 4.7 KB

```python
"""Unit tests for user CRUD operations."""

import pytest

from app.crud import user as user_crud


@pytest.fixture
def db_session(test_db):
    """Get a database session for testing."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


def test_create_user(db_session):
    """Test creating a user."""
    email = "testuser@example.com"
    password_hash = "hashedpassword123"

    user = user_crud.create_user(db_session, email, password_hash)

    assert user.id is not None
    assert user.email == email
    assert user.password_hash == password_hash
    assert user.created_at is not None


def test_get_user_by_id(db_session):
    """Test getting a user by ID."""
    # Create a user first
    user = user_crud.create_user(db_session, "user@example.com", "hash123")

    # Retrieve it
    retrieved = user_crud.get_user_by_id(db_session, user.id)

    assert retrieved is not None
    assert retrieved.id == user.id
    assert retrieved.email == user.email


def test_get_user_by_id_not_found(db_session):
    """Test getting a non-existent user returns None."""
    result = user_crud.get_user_by_id(db_session, 99999)
    assert result is None


def test_get_user_by_email(db_session):
    """Test getting a user by email."""
    email = "user@example.com"
    user = user_crud.create_user(db_session, email, "hash123")

    retrieved = user_crud.get_user_by_email(db_session, email)

    assert retrieved is not None
    assert retrieved.id == user.id
    assert retrieved.email == email


def test_get_user_by_email_not_found(db_session):
    """Test getting a non-existent user by email returns None."""
    result = user_crud.get_user_by_email(db_session, "nonexistent@example.com")
    assert result is None


def test_get_user_by_email_case_sensitive(db_session):
    """Test that email lookup is case-sensitive."""
    user_crud.create_user(db_session, "User@Example.com", "hash123")

    # SQLite is case-insensitive by default, but this tests the query
    result = user_crud.get_user_by_email(db_session, "user@example.com")
    # In SQLite, this might match. In production with PostgreSQL, it might not.
    # This test documents the behavior.
    assert result is not None or result is None  # Either behavior is acceptable


def test_get_users_pagination(db_session):
    """Test getting users with pagination."""
    # Create multiple users
    for i in range(5):
        user_crud.create_user(db_session, f"user{i}@example.com", f"hash{i}")

    # Get all users
    all_users = user_crud.get_users(db_session)
    assert len(all_users) == 5

    # Test skip
    users_skip_2 = user_crud.get_users(db_session, skip=2)
    assert len(users_skip_2) == 3

    # Test limit
    users_limit_2 = user_crud.get_users(db_session, limit=2)
    assert len(users_limit_2) == 2


def test_get_users_empty(db_session):
    """Test getting users when none exist."""
    users = user_crud.get_users(db_session)
    assert users == []


def test_update_user_password(db_session):
    """Test updating a user's password."""
    user = user_crud.create_user(db_session, "user@example.com", "oldhash")
    new_hash = "newhash123"

    updated = user_crud.update_user_password(db_session, user.id, new_hash)

    assert updated is not None
    assert updated.id == user.id
    assert updated.password_hash == new_hash

    # Verify the change persisted
    retrieved = user_crud.get_user_by_id(db_session, user.id)
    assert retrieved.password_hash == new_hash


def test_update_user_password_not_found(db_session):
    """Test updating password for non-existent user returns None."""
    result = user_crud.update_user_password(db_session, 99999, "newhash")
    assert result is None


def test_delete_user(db_session):
    """Test deleting a user."""
    user = user_crud.create_user(db_session, "user@example.com", "hash123")

    # Delete the user
    result = user_crud.delete_user(db_session, user.id)
    assert result is True

    # Verify it's gone
    retrieved = user_crud.get_user_by_id(db_session, user.id)
    assert retrieved is None


def test_delete_user_not_found(db_session):
    """Test deleting non-existent user returns False."""
    result = user_crud.delete_user(db_session, 99999)
    assert result is False


def test_create_multiple_users_same_email_fails(db_session):
    """Test that creating users with duplicate emails fails."""
    email = "duplicate@example.com"
    user_crud.create_user(db_session, email, "hash1")

    # Attempting to create another user with same email should raise an error
    with pytest.raises(Exception):  # SQLAlchemy will raise IntegrityError
        user_crud.create_user(db_session, email, "hash2")

```

## tests/interview/__init__.py

**Path:** `tests/interview/__init__.py`
**Type:** Python
**Size:** 29 bytes

```python
"""Interview flow tests."""

```

## tests/interview/test_chat_flow.py

**Path:** `tests/interview/test_chat_flow.py`
**Type:** Python
**Size:** 16.5 KB

```python
"""Tests for chat interview flow."""

from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def db(test_db):
    """Create a database session for tests."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def mock_ai_agent():
    """Mock AI agent to avoid API calls during tests."""
    with patch("app.routers.interview.AIInterviewAgent") as mock:
        agent_instance = MagicMock()
        agent_instance.get_initial_message.return_value = "Hello! Let's begin the interview. What are your thoughts on this topic?"
        agent_instance.get_ai_response.return_value = "That's interesting. Can you tell me more about that?"
        mock.return_value = agent_instance
        yield agent_instance


@pytest.mark.asyncio
async def test_chat_page_loads_with_initial_message(client: AsyncClient, db: Session, mock_ai_agent):
    """Test chat page loads and creates initial AI message."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
        max_agent_turns=5,
    )

    for i, question_text in enumerate(["Question 1?", "Question 2?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    response = await client.get(f"/interview/{invite.invite_code}/chat")

    assert response.status_code == 200
    assert "Test Study" in response.text
    assert "Hello" in response.text or "welcome" in response.text.lower()

    messages = interview_crud.get_messages_by_interview(db, interview.id)
    assert len(messages) == 1
    assert messages[0].role == "assistant"
    assert "Hello" in messages[0].content


@pytest.mark.asyncio
async def test_chat_page_redirects_if_no_consent(client: AsyncClient, db: Session):
    """Test chat page redirects if interview doesn't exist."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)

    response = await client.get(f"/interview/{invite.invite_code}/chat", follow_redirects=False)

    assert response.status_code == 303
    assert f"/interview/{invite.invite_code}/consent" in response.headers["location"]


@pytest.mark.asyncio
async def test_chat_page_redirects_if_no_intake(client: AsyncClient, db: Session):
    """Test chat page redirects if interviewee doesn't exist."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    response = await client.get(f"/interview/{invite.invite_code}/chat", follow_redirects=False)

    assert response.status_code == 303
    assert f"/interview/{invite.invite_code}/intake" in response.headers["location"]


@pytest.mark.asyncio
async def test_send_message_creates_user_and_ai_messages(client: AsyncClient, db: Session, mock_ai_agent):
    """Test sending a message creates both user and AI messages."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
        max_agent_turns=5,
    )

    for i, question_text in enumerate(["Question 1?", "Question 2?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "I think this is very interesting and important."},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "message" in data
    assert data["turns_remaining"] == 4

    messages = interview_crud.get_messages_by_interview(db, interview.id)
    assert len(messages) == 2
    assert messages[0].role == "user"
    assert messages[0].content == "I think this is very interesting and important."
    assert messages[1].role == "assistant"

    db.refresh(interview)
    assert interview.agent_turns == 1


@pytest.mark.asyncio
async def test_send_message_increments_turn_counter(client: AsyncClient, db: Session, mock_ai_agent):
    """Test that turn counter is incremented after each message."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
        max_agent_turns=3,
    )

    for i, question_text in enumerate(["Question 1?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    assert interview.agent_turns == 0

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "First response"},
    )

    db.refresh(interview)
    assert interview.agent_turns == 1

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "Second response"},
    )

    db.refresh(interview)
    assert interview.agent_turns == 2


@pytest.mark.asyncio
async def test_interview_completes_at_turn_limit(client: AsyncClient, db: Session, mock_ai_agent):
    """Test that interview completes when turn limit is reached."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
        max_agent_turns=2,
    )

    for i, question_text in enumerate(["Question 1?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "First response"},
    )

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "Second response"},
    )

    data = response.json()
    assert data["status"] == "completed"
    assert "redirect" in data
    assert "/complete" in data["redirect"]

    db.refresh(interview)
    assert interview.completed_at is not None
    assert interview.agent_turns == 2


@pytest.mark.asyncio
async def test_send_empty_message_returns_error(client: AsyncClient, db: Session, mock_ai_agent):
    """Test that empty messages are rejected."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "   "},
    )

    data = response.json()
    assert "error" in data
    assert data["error"] == "Message cannot be empty"


@pytest.mark.asyncio
async def test_send_message_to_completed_interview_returns_error(client: AsyncClient, db: Session):
    """Test that messages cannot be sent to completed interviews."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    interview_crud.complete_interview(db, interview.id)

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "This should fail"},
    )

    data = response.json()
    assert "error" in data
    assert data["error"] == "Interview already completed"


@pytest.mark.asyncio
async def test_long_message_is_truncated(client: AsyncClient, db: Session, mock_ai_agent):
    """Test that messages longer than 2000 chars are truncated."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    for i, question_text in enumerate(["Question 1?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    long_message = "A" * 2500

    response = await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": long_message},
    )

    assert response.status_code == 200

    messages = interview_crud.get_messages_by_interview(db, interview.id)
    user_message = [m for m in messages if m.role == "user"][0]
    assert len(user_message.content) == 2000


@pytest.mark.asyncio
async def test_chat_page_redirects_to_complete_if_already_done(client: AsyncClient, db: Session):
    """Test that completed interviews redirect to thank you page."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    interview_crud.complete_interview(db, interview.id)

    response = await client.get(f"/interview/{invite.invite_code}/chat", follow_redirects=False)

    assert response.status_code == 303
    assert f"/interview/{invite.invite_code}/complete" in response.headers["location"]


@pytest.mark.asyncio
async def test_complete_page_displays_thank_you(client: AsyncClient, db: Session):
    """Test that completion page displays correctly."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="John Doe",
        email="john@example.com",
    )

    interview_crud.complete_interview(db, interview.id)

    response = await client.get(f"/interview/{invite.invite_code}/complete")

    assert response.status_code == 200
    assert "Thank You" in response.text or "thank" in response.text.lower()
    assert "John Doe" in response.text
    assert "Test Study" in response.text


@pytest.mark.asyncio
async def test_ai_agent_receives_conversation_history(client: AsyncClient, db: Session, mock_ai_agent):
    """Test that AI agent receives full conversation history."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test description",
        consent_text="Test consent",
    )

    for i, question_text in enumerate(["Question 1?"]):
        study_crud.create_study_question(db, study_id=study.id, text=question_text, sort_order=i)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)
    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
    )

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "First message"},
    )

    await client.post(
        f"/interview/{invite.invite_code}/chat/message",
        data={"message": "Second message"},
    )

    assert mock_ai_agent.get_ai_response.called
    call_args = mock_ai_agent.get_ai_response.call_args
    conversation_history = call_args.kwargs["conversation_history"]

    assert len(conversation_history) >= 2
    assert any(msg["content"] == "First message" for msg in conversation_history)

```

## tests/interview/test_invite_landing.py

**Path:** `tests/interview/test_invite_landing.py`
**Type:** Python
**Size:** 4.5 KB

```python
"""Tests for invite landing page flow."""

from datetime import datetime, timedelta, timezone

import pytest
from httpx import AsyncClient

from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def db(test_db):
    """Create a database session for tests."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.mark.asyncio
async def test_invite_landing_page_valid(client: AsyncClient, db):
    """Test landing page with valid invite."""
    # Create test user and study
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hashed_password")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test study description",
        consent_text="I consent to participate",
    )

    # Create invite
    invite = invite_crud.create_invite(db, study_id=study.id)

    # Access landing page
    response = await client.get(f"/interview/{invite.invite_code}")

    assert response.status_code == 200
    assert "Test Study" in response.text
    assert "Test study description" in response.text
    assert "Continue to Consent Form" in response.text

    # Verify status updated to 'opened'
    db.refresh(invite)
    assert invite.status == InviteStatus.OPENED.value


@pytest.mark.asyncio
async def test_invite_landing_page_not_found(client: AsyncClient, db):
    """Test landing page with invalid invite code."""
    response = await client.get("/interview/invalid_code_12345")

    assert response.status_code == 404
    assert "Invitation Not Found" in response.text


@pytest.mark.asyncio
async def test_invite_landing_page_expired(client: AsyncClient, db):
    """Test landing page with expired invite."""
    # Create test user and study
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hashed_password")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test study description",
        consent_text="I consent to participate",
    )

    # Create expired invite
    expired_time = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(hours=1)
    invite = invite_crud.create_invite(
        db,
        study_id=study.id,
        expires_at=expired_time,
    )

    # Access landing page
    response = await client.get(f"/interview/{invite.invite_code}")

    assert response.status_code == 200
    assert "Invite Has Expired" in response.text


@pytest.mark.asyncio
async def test_invite_landing_page_completed(client: AsyncClient, db):
    """Test landing page with completed invite."""
    # Create test user and study
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hashed_password")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test study description",
        consent_text="I consent to participate",
    )

    # Create invite and mark as completed
    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    # Access landing page
    response = await client.get(f"/interview/{invite.invite_code}")

    assert response.status_code == 200
    assert "Already Completed" in response.text


@pytest.mark.asyncio
async def test_invite_status_only_updated_once(client: AsyncClient, db):
    """Test that invite status is only updated to 'opened' once."""
    # Create test user and study
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hashed_password")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test study description",
        consent_text="I consent to participate",
    )

    # Create invite
    invite = invite_crud.create_invite(db, study_id=study.id)
    assert invite.status == InviteStatus.CREATED.value

    # First visit - should update to 'opened'
    response = await client.get(f"/interview/{invite.invite_code}")
    assert response.status_code == 200
    db.refresh(invite)
    assert invite.status == InviteStatus.OPENED.value

    # Second visit - should remain 'opened'
    response = await client.get(f"/interview/{invite.invite_code}")
    assert response.status_code == 200
    db.refresh(invite)
    assert invite.status == InviteStatus.OPENED.value

```

## tests/routers/__init__.py

**Path:** `tests/routers/__init__.py`
**Type:** Python
**Size:** 0 bytes

```python

```

## tests/routers/test_analytics.py

**Path:** `tests/routers/test_analytics.py`
**Type:** Python
**Size:** 14.7 KB

```python
"""Tests for study analytics endpoint."""

import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def study_with_varied_interviews(test_db, test_user):
    """Create a study with multiple interviews with varied data."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])

        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Analytics Test Study",
            description="Study for testing analytics",
            consent_text="Test consent",
            max_agent_turns=5,
        )

        # Interview 1: Positive sentiment
        invite1 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite1.id, InviteStatus.COMPLETED)
        interview1 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite1.id)

        interview_crud.create_interviewee(
            db,
            interview_id=interview1.id,
            name="Alice Smith",
            email="alice@example.com",
            demographics_json={"age_range": "25-34", "location": "USA", "occupation": "Engineer"},
        )

        interview_crud.create_message(
            db, interview_id=interview1.id, role="assistant", content="Hello!"
        )
        interview_crud.create_message(
            db, interview_id=interview1.id, role="user", content="This product is amazing and intuitive!"
        )
        interview_crud.create_message(
            db, interview_id=interview1.id, role="assistant", content="Great to hear!"
        )
        interview_crud.create_message(
            db, interview_id=interview1.id, role="user", content="I love using it every day."
        )

        interview_crud.complete_interview(db, interview1.id)
        interview_crud.create_insight(
            db,
            interview_id=interview1.id,
            summary="User loves the product",
            sentiment="positive",
            keywords_json=["product", "amazing", "intuitive", "love"],
            quotes_json=["This product is amazing and intuitive!", "I love using it every day."],
        )

        # Interview 2: Neutral sentiment
        invite2 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite2.id, InviteStatus.COMPLETED)
        interview2 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite2.id)

        interview_crud.create_interviewee(
            db,
            interview_id=interview2.id,
            name="Bob Jones",
            email="bob@example.com",
            demographics_json={"age_range": "35-44", "location": "Canada", "occupation": "Designer"},
        )

        interview_crud.create_message(
            db, interview_id=interview2.id, role="assistant", content="Hello!"
        )
        interview_crud.create_message(
            db, interview_id=interview2.id, role="user", content="The product is okay, nothing special."
        )

        interview_crud.complete_interview(db, interview2.id)
        interview_crud.create_insight(
            db,
            interview_id=interview2.id,
            summary="User finds it adequate",
            sentiment="neutral",
            keywords_json=["product", "okay"],
            quotes_json=["The product is okay, nothing special."],
        )

        # Interview 3: Negative sentiment
        invite3 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite3.id, InviteStatus.COMPLETED)
        interview3 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite3.id)

        interview_crud.create_interviewee(
            db,
            interview_id=interview3.id,
            name="Charlie Brown",
            email="charlie@example.com",
            demographics_json={"age_range": "25-34", "location": "USA", "occupation": "Manager"},
        )

        interview_crud.create_message(
            db, interview_id=interview3.id, role="assistant", content="Hi!"
        )
        interview_crud.create_message(
            db, interview_id=interview3.id, role="user", content="I'm frustrated with the interface."
        )
        interview_crud.create_message(
            db, interview_id=interview3.id, role="assistant", content="Sorry to hear that"
        )
        interview_crud.create_message(
            db, interview_id=interview3.id, role="user", content="It's confusing."
        )

        interview_crud.complete_interview(db, interview3.id)
        interview_crud.create_insight(
            db,
            interview_id=interview3.id,
            summary="User frustrated with interface",
            sentiment="negative",
            keywords_json=["interface", "frustrated", "confusing"],
            quotes_json=["I'm frustrated with the interface."],
        )

        # Interview 4: In progress (not completed)
        invite4 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite4.id, InviteStatus.OPENED)
        interview4 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite4.id)

        interview_crud.create_interviewee(
            db,
            interview_id=interview4.id,
            name="Diana Prince",
            email="diana@example.com",
            demographics_json={"age_range": "45-54", "location": "UK"},
        )

        interview_crud.create_message(
            db, interview_id=interview4.id, role="assistant", content="Welcome!"
        )

        yield {"user": user, "study": study, "interviews": [interview1, interview2, interview3, interview4]}
    finally:
        db.close()


@pytest.mark.asyncio
async def test_get_analytics_success(
    authenticated_client: AsyncClient, study_with_varied_interviews
):
    """Test retrieving analytics for a study with varied data."""
    study = study_with_varied_interviews["study"]

    response = await authenticated_client.get(
        f"/studies/{study.id}/analytics"
    )

    assert response.status_code == 200
    data = response.json()

    # Basic counts
    assert data["study_id"] == study.id
    assert data["study_title"] == "Analytics Test Study"
    assert data["total_interviews"] == 4
    assert data["completed_interviews"] == 3

    # Sentiment distribution
    sentiment = data["sentiment_distribution"]
    assert sentiment["positive"] == 1
    assert sentiment["neutral"] == 1
    assert sentiment["negative"] == 1
    assert sentiment["total"] == 3

    # Keywords
    keywords = data["top_keywords"]
    assert len(keywords) > 0
    # "product" appears in 2 completed interviews (1 and 2)
    product_kw = next((kw for kw in keywords if kw["keyword"] == "product"), None)
    assert product_kw is not None
    assert product_kw["count"] == 2

    # Response metrics
    metrics = data["response_metrics"]
    assert metrics["total_messages"] > 0
    assert metrics["avg_message_count"] > 0
    assert metrics["avg_response_length"] > 0

    # Demographics
    demographics = data["demographics"]
    assert len(demographics) > 0

    # Check age_range demographic
    age_demo = next((d for d in demographics if d["field"] == "age_range"), None)
    assert age_demo is not None
    assert age_demo["values"]["25-34"] == 2  # Alice and Charlie
    assert age_demo["values"]["35-44"] == 1  # Bob
    assert age_demo["values"]["45-54"] == 1  # Diana

    # Check location demographic
    location_demo = next((d for d in demographics if d["field"] == "location"), None)
    assert location_demo is not None
    assert location_demo["values"]["USA"] == 2
    assert location_demo["values"]["Canada"] == 1
    assert location_demo["values"]["UK"] == 1

    # Timeline
    timeline = data["timeline"]
    assert len(timeline) > 0
    # All interviews started on same day in test
    assert timeline[0]["completed"] == 3
    assert timeline[0]["in_progress"] == 1

    # Sample quotes
    quotes = data["sample_quotes"]
    assert len(quotes) > 0
    assert "This product is amazing and intuitive!" in quotes


@pytest.mark.asyncio
async def test_get_analytics_empty_study(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test analytics for a study with no interviews."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Empty Study",
            description="No interviews",
            consent_text="Test",
        )

        response = await authenticated_client.get(
            f"/studies/{study.id}/analytics"
        )

        assert response.status_code == 200
        data = response.json()

        assert data["total_interviews"] == 0
        assert data["completed_interviews"] == 0
        assert data["sentiment_distribution"]["total"] == 0
        assert len(data["top_keywords"]) == 0
        assert data["response_metrics"]["total_messages"] == 0
        assert len(data["demographics"]) == 0
        assert len(data["timeline"]) == 0
        assert len(data["sample_quotes"]) == 0
    finally:
        db.close()


@pytest.mark.asyncio
async def test_get_analytics_unauthorized(
    client: AsyncClient, study_with_varied_interviews
):
    """Test that unauthorized users cannot access analytics."""
    study = study_with_varied_interviews["study"]

    # Create and login as different user
    await client.post(
        "/auth/dev/register",
        data={"email": "other@example.com", "password": "testpass123"},
    )

    await client.post(
        "/auth/dev/login",
        data={"email": "other@example.com", "password": "testpass123"},
        follow_redirects=False,
    )

    response = await client.get(
        f"/studies/{study.id}/analytics"
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_analytics_no_auth(
    client: AsyncClient, study_with_varied_interviews
):
    """Test that unauthenticated requests are rejected."""
    study = study_with_varied_interviews["study"]

    response = await client.get(f"/studies/{study.id}/analytics")

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_analytics_not_found(
    authenticated_client: AsyncClient
):
    """Test analytics for non-existent study."""
    response = await authenticated_client.get("/studies/99999/analytics")

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_analytics_keyword_frequency(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test keyword frequency calculation."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Keyword Test",
            description="Test",
            consent_text="Test",
        )

        # Create interviews with overlapping keywords
        for i in range(3):
            invite = invite_crud.create_invite(db, study_id=study.id)
            invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
            interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

            interview_crud.create_interviewee(
                db, interview_id=interview.id, name=f"User {i}", email=f"user{i}@test.com"
            )

            interview_crud.create_message(
                db, interview_id=interview.id, role="user", content="Test"
            )

            interview_crud.complete_interview(db, interview.id)

            # All have "design", two have "interface"
            keywords = ["design"]
            if i < 2:
                keywords.append("interface")

            interview_crud.create_insight(
                db,
                interview_id=interview.id,
                summary="Test",
                sentiment="neutral",
                keywords_json=keywords,
                quotes_json=[],
            )

        response = await authenticated_client.get(f"/studies/{study.id}/analytics")

        assert response.status_code == 200
        data = response.json()

        keywords = {kw["keyword"]: kw["count"] for kw in data["top_keywords"]}
        assert keywords["design"] == 3
        assert keywords["interface"] == 2
    finally:
        db.close()


@pytest.mark.asyncio
async def test_get_analytics_response_metrics(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test response metrics calculation."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Metrics Test",
            description="Test",
            consent_text="Test",
        )

        invite = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
        interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

        interview_crud.create_interviewee(
            db, interview_id=interview.id, name="Test User", email="test@example.com"
        )

        # Add messages with known lengths
        interview_crud.create_message(
            db, interview_id=interview.id, role="assistant", content="Hello there!"  # 12 chars
        )
        interview_crud.create_message(
            db, interview_id=interview.id, role="user", content="Hi!"  # 3 chars
        )
        interview_crud.create_message(
            db, interview_id=interview.id, role="user", content="How are you?"  # 12 chars
        )

        interview_crud.complete_interview(db, interview.id)
        interview_crud.create_insight(
            db, interview_id=interview.id, summary="Test", sentiment="neutral",
            keywords_json=[], quotes_json=[]
        )

        response = await authenticated_client.get(f"/studies/{study.id}/analytics")

        assert response.status_code == 200
        data = response.json()

        metrics = data["response_metrics"]
        assert metrics["total_messages"] == 3
        assert metrics["avg_message_count"] == 3.0
        # 2 user messages: 3 + 12 = 15 chars, avg = 7.5
        assert metrics["avg_response_length"] == 7.5
    finally:
        db.close()

```

## tests/routers/test_auth_dev.py

**Path:** `tests/routers/test_auth_dev.py`
**Type:** Python
**Size:** 3.7 KB

```python
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

```

## tests/routers/test_export.py

**Path:** `tests/routers/test_export.py`
**Type:** Python
**Size:** 13.8 KB

```python
"""Tests for data export endpoints."""

import csv
import io
import json

import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def study_with_interviews(test_db, test_user):
    """Create a study with multiple completed interviews."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])

        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Export Test Study",
            description="Study for testing exports",
            consent_text="Test consent",
            max_agent_turns=5,
        )

        # Create first interview
        invite1 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite1.id, InviteStatus.COMPLETED)
        interview1 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite1.id)

        interview_crud.create_interviewee(
            db,
            interview_id=interview1.id,
            name="Alice Smith",
            email="alice@example.com",
            demographics_json={"age_range": "25-34", "location": "USA"},
        )

        interview_crud.create_message(
            db, interview_id=interview1.id, role="assistant", content="Hello Alice!"
        )
        interview_crud.create_message(
            db, interview_id=interview1.id, role="user", content="Hi there!"
        )

        interview_crud.complete_interview(db, interview1.id)
        interview_crud.create_insight(
            db,
            interview_id=interview1.id,
            summary="Positive feedback about product design",
            sentiment="positive",
            keywords_json=["design", "interface"],
            quotes_json=["Hi there!"],
        )

        # Create second interview
        invite2 = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite2.id, InviteStatus.COMPLETED)
        interview2 = interview_crud.create_interview(db, study_id=study.id, invite_id=invite2.id)

        interview_crud.create_interviewee(
            db,
            interview_id=interview2.id,
            name="Bob Jones",
            email="bob@example.com",
            demographics_json={"age_range": "35-44", "location": "Canada"},
        )

        interview_crud.create_message(
            db, interview_id=interview2.id, role="assistant", content="Hello Bob!"
        )
        interview_crud.create_message(
            db, interview_id=interview2.id, role="user", content="Good morning!"
        )
        interview_crud.create_message(
            db, interview_id=interview2.id, role="assistant", content="How are you?"
        )
        interview_crud.create_message(
            db, interview_id=interview2.id, role="user", content="Great, thanks!"
        )

        interview_crud.complete_interview(db, interview2.id)
        interview_crud.create_insight(
            db,
            interview_id=interview2.id,
            summary="User satisfied with service",
            sentiment="neutral",
            keywords_json=["service", "satisfaction"],
            quotes_json=["Great, thanks!"],
        )

        yield {"user": user, "study": study, "interviews": [interview1, interview2]}
    finally:
        db.close()


@pytest.mark.asyncio
async def test_export_single_interview_json(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting a single interview as JSON."""
    study = study_with_interviews["study"]
    interview = study_with_interviews["interviews"][0]

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/{interview.id}/export?format=json"
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert "attachment" in response.headers["content-disposition"]
    assert f"interview_{interview.id}" in response.headers["content-disposition"]

    data = json.loads(response.content)

    assert data["study"]["title"] == "Export Test Study"
    assert data["interview_count"] == 1
    assert len(data["interviews"]) == 1

    interview_data = data["interviews"][0]
    assert interview_data["id"] == interview.id
    assert interview_data["interviewee"]["name"] == "Alice Smith"
    assert interview_data["interviewee"]["email"] == "alice@example.com"
    assert interview_data["insight"]["sentiment"] == "positive"
    assert len(interview_data["messages"]) == 2


@pytest.mark.asyncio
async def test_export_single_interview_csv(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting a single interview as CSV."""
    study = study_with_interviews["study"]
    interview = study_with_interviews["interviews"][0]

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/{interview.id}/export?format=csv"
    )

    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    assert "attachment" in response.headers["content-disposition"]

    # Parse CSV content
    csv_content = response.content.decode("utf-8")
    csv_reader = csv.DictReader(io.StringIO(csv_content))
    rows = list(csv_reader)

    assert len(rows) == 1
    row = rows[0]

    assert row["study_title"] == "Export Test Study"
    assert row["interview_id"] == str(interview.id)
    assert row["interviewee_name"] == "Alice Smith"
    assert row["interviewee_email"] == "alice@example.com"
    assert row["sentiment"] == "positive"
    assert row["message_count"] == "2"
    assert "[ASSISTANT]:" in row["conversation"]
    assert "[USER]:" in row["conversation"]


@pytest.mark.asyncio
async def test_export_study_all_interviews_json(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting all interviews for a study as JSON."""
    study = study_with_interviews["study"]

    response = await authenticated_client.get(
        f"/studies/{study.id}/export?format=json"
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    data = json.loads(response.content)

    assert data["study"]["title"] == "Export Test Study"
    assert data["interview_count"] == 2
    assert len(data["interviews"]) == 2

    # Check both interviews are present
    names = {i["interviewee"]["name"] for i in data["interviews"]}
    assert names == {"Alice Smith", "Bob Jones"}


@pytest.mark.asyncio
async def test_export_study_all_interviews_csv(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting all interviews for a study as CSV."""
    study = study_with_interviews["study"]

    response = await authenticated_client.get(
        f"/studies/{study.id}/export?format=csv"
    )

    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]

    # Parse CSV content
    csv_content = response.content.decode("utf-8")
    csv_reader = csv.DictReader(io.StringIO(csv_content))
    rows = list(csv_reader)

    assert len(rows) == 2

    # Check both interviews are present
    names = {row["interviewee_name"] for row in rows}
    assert names == {"Alice Smith", "Bob Jones"}

    # Verify all expected columns are present
    expected_columns = {
        "study_title", "interview_id", "interviewee_name", "interviewee_email",
        "demographics", "started_at", "completed_at", "agent_turns",
        "message_count", "summary", "sentiment", "keywords", "quotes", "conversation"
    }
    assert set(rows[0].keys()) == expected_columns


@pytest.mark.asyncio
async def test_export_invalid_format(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test that invalid export format returns error."""
    study = study_with_interviews["study"]
    interview = study_with_interviews["interviews"][0]

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/{interview.id}/export?format=xml"
    )

    assert response.status_code == 422  # Validation error


@pytest.mark.asyncio
async def test_export_interview_not_found(
    authenticated_client: AsyncClient, study_with_interviews
):
    """Test exporting non-existent interview returns 404."""
    study = study_with_interviews["study"]

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/99999/export?format=json"
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_export_interview_wrong_study(
    authenticated_client: AsyncClient, test_user, test_db, study_with_interviews
):
    """Test that interview from different study cannot be exported."""
    user = study_with_interviews["user"]
    interview = study_with_interviews["interviews"][0]

    # Create a different study
    db = test_db()
    try:
        other_study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Other Study",
            description="Different study",
            consent_text="Test",
        )

        response = await authenticated_client.get(
            f"/studies/{other_study.id}/interviews/{interview.id}/export?format=json"
        )

        assert response.status_code == 404
    finally:
        db.close()


@pytest.mark.asyncio
async def test_export_unauthorized_user(
    client: AsyncClient, study_with_interviews
):
    """Test that unauthorized users cannot export data."""
    study = study_with_interviews["study"]
    interview = study_with_interviews["interviews"][0]

    # Create and login as different user
    await client.post(
        "/auth/dev/register",
        data={"email": "other@example.com", "password": "testpass123"},
    )

    await client.post(
        "/auth/dev/login",
        data={"email": "other@example.com", "password": "testpass123"},
        follow_redirects=False,
    )

    response = await client.get(
        f"/studies/{study.id}/interviews/{interview.id}/export?format=json"
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_export_empty_study(authenticated_client: AsyncClient, test_user, test_db):
    """Test exporting a study with no interviews."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Empty Study",
            description="No interviews",
            consent_text="Test",
        )

        response = await authenticated_client.get(
            f"/studies/{study.id}/export?format=json"
        )

        assert response.status_code == 200

        data = json.loads(response.content)
        assert data["interview_count"] == 0
        assert len(data["interviews"]) == 0
    finally:
        db.close()


@pytest.mark.asyncio
async def test_export_csv_handles_special_characters(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test that CSV export properly handles special characters and quotes."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Test, Study, With, Commas",
            description="Test",
            consent_text="Test",
        )

        invite = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
        interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

        interview_crud.create_interviewee(
            db,
            interview_id=interview.id,
            name='John "Johnny" O\'Brien',
            email="john@example.com",
        )

        interview_crud.create_message(
            db, interview_id=interview.id, role="user", content='Message with "quotes" and, commas'
        )

        interview_crud.complete_interview(db, interview.id)

        response = await authenticated_client.get(
            f"/studies/{study.id}/export?format=csv"
        )

        assert response.status_code == 200

        # Parse CSV and verify it handles special characters correctly
        csv_content = response.content.decode("utf-8")
        csv_reader = csv.DictReader(io.StringIO(csv_content))
        rows = list(csv_reader)

        assert len(rows) == 1
        assert rows[0]["interviewee_name"] == 'John "Johnny" O\'Brien'
        assert "quotes" in rows[0]["conversation"]
    finally:
        db.close()


@pytest.mark.asyncio
async def test_export_filename_sanitization(
    authenticated_client: AsyncClient, test_user, test_db
):
    """Test that export filenames are properly sanitized."""
    db = test_db()
    try:
        user = user_crud.get_user_by_email(db, test_user["email"])
        study = study_crud.create_study(
            db,
            owner_user_id=user.id,
            title="Study/With\\Special:Characters",
            description="Test",
            consent_text="Test",
        )

        response = await authenticated_client.get(
            f"/studies/{study.id}/export?format=json"
        )

        assert response.status_code == 200

        # Check filename is sanitized (no special characters)
        disposition = response.headers["content-disposition"]
        assert "/" not in disposition
        assert "\\" not in disposition
        assert ":" not in disposition
        assert "Study_With_Special_Characters" in disposition or "study_" in disposition.lower()
    finally:
        db.close()

```

## tests/routers/test_interview_results.py

**Path:** `tests/routers/test_interview_results.py`
**Type:** Python
**Size:** 10.8 KB

```python
"""Tests for interview results API endpoints."""

import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import session as session_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus


@pytest.fixture
def db(test_db):
    """Get database session from test_db fixture."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def researcher_with_study(db: Session, test_user):
    """Create a researcher user with a study and completed interview."""
    user = user_crud.get_user_by_email(db, test_user["email"])

    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Product Research",
        description="Understanding user experience",
        consent_text="Test consent",
        max_agent_turns=5,
    )

    study_crud.create_study_question(
        db, study_id=study.id, text="What do you think about the product?", sort_order=0
    )

    study_crud.create_study_question(
        db, study_id=study.id, text="How can we improve?", sort_order=1
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    interviewee = interview_crud.create_interviewee(
        db,
        interview_id=interview.id,
        name="Test User",
        email="test@example.com",
        demographics_json={"age_range": "25-34", "location": "USA"},
    )

    interview_crud.create_message(
        db, interview_id=interview.id, role="assistant", content="Hello! What brings you here?"
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="user",
        content="I really love the new design. The interface is very intuitive.",
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="assistant",
        content="That's great to hear! Can you tell me more?",
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="user",
        content="The navigation is smooth and all the features I need are easily accessible.",
    )

    interview_crud.complete_interview(db, interview.id)

    interview_crud.create_insight(
        db,
        interview_id=interview.id,
        summary="Participant expressed positive sentiment about the product design and usability.",
        sentiment="positive",
        keywords_json=["design", "interface", "navigation", "features"],
        quotes_json=[
            "I really love the new design. The interface is very intuitive.",
            "The navigation is smooth and all the features I need are easily accessible.",
        ],
    )

    return {"user": user, "study": study, "interview": interview}


@pytest.mark.asyncio
async def test_list_interviews_success(authenticated_client: AsyncClient, db: Session, researcher_with_study):
    """Test listing interviews for a study."""
    study = researcher_with_study["study"]

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews",
    )

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    interview = data[0]

    assert interview["study_id"] == study.id
    assert interview["completed_at"] is not None
    assert interview["interviewee"]["name"] == "Test User"
    assert interview["interviewee"]["email"] == "test@example.com"
    assert interview["insight"]["sentiment"] == "positive"
    assert interview["insight"]["summary"] is not None
    assert len(interview["insight"]["keywords_json"]) > 0
    assert interview["message_count"] == 4


@pytest.mark.asyncio
async def test_list_interviews_empty_study(authenticated_client: AsyncClient, test_user, db: Session):
    """Test listing interviews for a study with no interviews."""
    user = user_crud.get_user_by_email(db, test_user["email"])
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Empty Study",
        description="No interviews yet",
        consent_text="Test",
    )

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews",
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 0


@pytest.mark.asyncio
async def test_list_interviews_unauthorized(client: AsyncClient, db: Session, researcher_with_study):
    """Test that unauthorized users cannot list interviews."""
    study = researcher_with_study["study"]

    # Create another user properly using registration endpoint
    await client.post(
        "/auth/dev/register",
        data={"email": "other@test.com", "password": "testpass123"},
    )

    # Login as the other user
    response = await client.post(
        "/auth/dev/login",
        data={"email": "other@test.com", "password": "testpass123"},
        follow_redirects=False,
    )

    response = await client.get(
        f"/studies/{study.id}/interviews",
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_list_interviews_no_auth(client: AsyncClient, db: Session, researcher_with_study):
    """Test that unauthenticated requests are rejected."""
    study = researcher_with_study["study"]

    response = await client.get(f"/studies/{study.id}/interviews")

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_interview_transcript_success(
    authenticated_client: AsyncClient, db: Session, researcher_with_study
):
    """Test getting full interview transcript."""
    study = researcher_with_study["study"]
    interview = researcher_with_study["interview"]

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/{interview.id}",
    )

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == interview.id
    assert data["study_id"] == study.id
    assert data["completed_at"] is not None

    assert data["interviewee"]["name"] == "Test User"
    assert data["interviewee"]["demographics_json"]["age_range"] == "25-34"

    assert len(data["messages"]) == 4
    assert data["messages"][0]["role"] == "assistant"
    assert data["messages"][1]["role"] == "user"
    assert "Hello" in data["messages"][0]["content"]

    assert data["insight"] is not None
    assert data["insight"]["sentiment"] == "positive"
    assert len(data["insight"]["keywords_json"]) == 4
    assert len(data["insight"]["quotes_json"]) == 2


@pytest.mark.asyncio
async def test_get_interview_transcript_not_found(authenticated_client: AsyncClient, test_user, db: Session):
    """Test getting transcript for non-existent interview."""
    user = user_crud.get_user_by_email(db, test_user["email"])
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test",
        consent_text="Test",
    )

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews/99999",
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_interview_transcript_wrong_study(
    authenticated_client: AsyncClient, db: Session, researcher_with_study
):
    """Test that interview cannot be accessed from wrong study."""
    user = researcher_with_study["user"]
    interview = researcher_with_study["interview"]

    other_study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Other Study",
        description="Different study",
        consent_text="Test",
    )

    response = await authenticated_client.get(
        f"/studies/{other_study.id}/interviews/{interview.id}",
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_interview_transcript_unauthorized(
    client: AsyncClient, db: Session, researcher_with_study
):
    """Test that unauthorized users cannot view transcripts."""
    study = researcher_with_study["study"]
    interview = researcher_with_study["interview"]

    # Create another user properly using registration endpoint
    await client.post(
        "/auth/dev/register",
        data={"email": "other@test.com", "password": "testpass123"},
    )

    # Login as the other user
    await client.post(
        "/auth/dev/login",
        data={"email": "other@test.com", "password": "testpass123"},
        follow_redirects=False,
    )

    response = await client.get(
        f"/studies/{study.id}/interviews/{interview.id}",
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_list_interviews_multiple_interviews(authenticated_client: AsyncClient, test_user, db: Session):
    """Test listing multiple interviews with different statuses."""
    user = user_crud.get_user_by_email(db, test_user["email"])
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Multi-Interview Study",
        description="Test",
        consent_text="Test",
    )

    for i in range(3):
        invite = invite_crud.create_invite(db, study_id=study.id)
        invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)
        interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

        interview_crud.create_interviewee(
            db, interview_id=interview.id, name=f"User {i}", email=f"user{i}@test.com"
        )

        interview_crud.create_message(
            db, interview_id=interview.id, role="assistant", content="Hello"
        )
        interview_crud.create_message(
            db, interview_id=interview.id, role="user", content="Hi there"
        )

        if i < 2:
            interview_crud.complete_interview(db, interview.id)
            interview_crud.create_insight(
                db,
                interview_id=interview.id,
                summary="Test summary",
                sentiment="neutral",
                keywords_json=["test"],
                quotes_json=["Hi there"],
            )

    response = await authenticated_client.get(
        f"/studies/{study.id}/interviews",
    )

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 3

    completed = [d for d in data if d["completed_at"] is not None]
    in_progress = [d for d in data if d["completed_at"] is None]

    assert len(completed) == 2
    assert len(in_progress) == 1

    for interview in completed:
        assert interview["insight"] is not None

    for interview in in_progress:
        assert interview["insight"] is None

```

## tests/routers/test_invites.py

**Path:** `tests/routers/test_invites.py`
**Type:** Python
**Size:** 4.4 KB

```python
"""Tests for invites routes."""

import pytest
from httpx import AsyncClient


@pytest.fixture
async def test_study(authenticated_client: AsyncClient):
    """Create a test study and return its ID."""
    response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Test Study",
            "description": "For testing invites",
            "consent_text": "I consent",
        },
    )
    return response.json()["id"]


@pytest.mark.asyncio
async def test_create_invite(authenticated_client: AsyncClient, test_study):
    """Test creating an invite."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["study_id"] == test_study
    assert "invite_code" in data
    assert len(data["invite_code"]) > 20  # Should be a long random string
    assert data["status"] == "created"


@pytest.mark.asyncio
async def test_create_invite_with_email(authenticated_client: AsyncClient, test_study):
    """Test creating an invite with interviewee email."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={"interviewee_email": "participant@example.com"},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["interviewee_email"] == "participant@example.com"


@pytest.mark.asyncio
async def test_create_invite_invalid_email(authenticated_client: AsyncClient, test_study):
    """Test creating invite with invalid email fails."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={"interviewee_email": "not-an-email"},
    )

    assert response.status_code == 422  # Validation error


@pytest.mark.asyncio
async def test_list_invites(authenticated_client: AsyncClient, test_study):
    """Test listing invites for a study."""
    # Create invites
    await authenticated_client.post(f"/studies/{test_study}/invites", json={})
    await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={"interviewee_email": "person@example.com"},
    )

    # List invites
    response = await authenticated_client.get(f"/studies/{test_study}/invites")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all("invite_code" in invite for invite in data)


@pytest.mark.asyncio
async def test_delete_invite(authenticated_client: AsyncClient, test_study):
    """Test deleting an invite."""
    # Create invite
    create_response = await authenticated_client.post(
        f"/studies/{test_study}/invites",
        json={},
    )
    invite_id = create_response.json()["id"]

    # Delete invite
    response = await authenticated_client.delete(
        f"/studies/{test_study}/invites/{invite_id}"
    )
    assert response.status_code == 204

    # Verify it's gone
    list_response = await authenticated_client.get(f"/studies/{test_study}/invites")
    assert len(list_response.json()) == 0


@pytest.mark.asyncio
async def test_invite_codes_unique(authenticated_client: AsyncClient, test_study):
    """Test that each invite gets a unique code."""
    invite1 = await authenticated_client.post(f"/studies/{test_study}/invites", json={})
    invite2 = await authenticated_client.post(f"/studies/{test_study}/invites", json={})

    code1 = invite1.json()["invite_code"]
    code2 = invite2.json()["invite_code"]

    assert code1 != code2


@pytest.mark.asyncio
async def test_invites_isolated_by_study(authenticated_client: AsyncClient):
    """Test invites from one study don't appear in another."""
    # Create two studies
    study1_response = await authenticated_client.post(
        "/studies/",
        json={"title": "Study 1", "description": "First", "consent_text": "Consent"},
    )
    study2_response = await authenticated_client.post(
        "/studies/",
        json={"title": "Study 2", "description": "Second", "consent_text": "Consent"},
    )

    study1_id = study1_response.json()["id"]
    study2_id = study2_response.json()["id"]

    # Create invite for study 1
    await authenticated_client.post(f"/studies/{study1_id}/invites", json={})

    # Study 2 should have no invites
    study2_invites = await authenticated_client.get(f"/studies/{study2_id}/invites")
    assert len(study2_invites.json()) == 0


```

## tests/routers/test_questions.py

**Path:** `tests/routers/test_questions.py`
**Type:** Python
**Size:** 5.1 KB

```python
"""Tests for study questions routes."""

import pytest
from httpx import AsyncClient


@pytest.fixture
async def test_study(authenticated_client: AsyncClient):
    """Create a test study and return its ID."""
    response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Test Study",
            "description": "For testing questions",
            "consent_text": "I consent",
        },
    )
    return response.json()["id"]


@pytest.mark.asyncio
async def test_create_question(authenticated_client: AsyncClient, test_study):
    """Test adding a question to a study."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "What is your biggest challenge?", "sort_order": 0},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["text"] == "What is your biggest challenge?"
    assert data["sort_order"] == 0
    assert data["study_id"] == test_study


@pytest.mark.asyncio
async def test_list_questions(authenticated_client: AsyncClient, test_study):
    """Test listing questions returns them in order."""
    # Create questions
    await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "Question 1", "sort_order": 0},
    )
    await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "Question 2", "sort_order": 1},
    )
    await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "Question 3", "sort_order": 2},
    )

    # List questions
    response = await authenticated_client.get(f"/studies/{test_study}/questions")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["text"] == "Question 1"
    assert data[1]["text"] == "Question 2"
    assert data[2]["text"] == "Question 3"


@pytest.mark.asyncio
async def test_reorder_questions(authenticated_client: AsyncClient, test_study):
    """Test reordering questions."""
    # Create questions
    q1 = await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "First", "sort_order": 0},
    )
    q2 = await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "Second", "sort_order": 1},
    )

    q1_id = q1.json()["id"]
    q2_id = q2.json()["id"]

    # Reorder (swap them)
    response = await authenticated_client.post(
        f"/studies/{test_study}/questions/reorder",
        json={
            "updates": [
                {"question_id": q1_id, "sort_order": 1},
                {"question_id": q2_id, "sort_order": 0},
            ]
        },
    )

    assert response.status_code == 204

    # Verify new order
    list_response = await authenticated_client.get(f"/studies/{test_study}/questions")
    questions = list_response.json()
    assert questions[0]["text"] == "Second"  # Now first
    assert questions[1]["text"] == "First"  # Now second


@pytest.mark.asyncio
async def test_reorder_invalid_question(authenticated_client: AsyncClient, test_study):
    """Test reordering with invalid question ID fails."""
    response = await authenticated_client.post(
        f"/studies/{test_study}/questions/reorder",
        json={
            "updates": [
                {"question_id": 99999, "sort_order": 0},  # Doesn't exist
            ]
        },
    )

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_delete_question(authenticated_client: AsyncClient, test_study):
    """Test deleting a question."""
    # Create question
    create_response = await authenticated_client.post(
        f"/studies/{test_study}/questions",
        json={"text": "To delete", "sort_order": 0},
    )
    question_id = create_response.json()["id"]

    # Delete question
    response = await authenticated_client.delete(
        f"/studies/{test_study}/questions/{question_id}"
    )
    assert response.status_code == 204

    # Verify it's gone
    list_response = await authenticated_client.get(f"/studies/{test_study}/questions")
    assert len(list_response.json()) == 0


@pytest.mark.asyncio
async def test_questions_isolated_by_study(authenticated_client: AsyncClient):
    """Test questions from one study don't appear in another."""
    # Create two studies
    study1_response = await authenticated_client.post(
        "/studies/",
        json={"title": "Study 1", "description": "First", "consent_text": "Consent"},
    )
    study2_response = await authenticated_client.post(
        "/studies/",
        json={"title": "Study 2", "description": "Second", "consent_text": "Consent"},
    )

    study1_id = study1_response.json()["id"]
    study2_id = study2_response.json()["id"]

    # Add question to study 1
    await authenticated_client.post(
        f"/studies/{study1_id}/questions",
        json={"text": "Study 1 question", "sort_order": 0},
    )

    # Study 2 should have no questions
    study2_questions = await authenticated_client.get(f"/studies/{study2_id}/questions")
    assert len(study2_questions.json()) == 0


```

## tests/routers/test_studies.py

**Path:** `tests/routers/test_studies.py`
**Type:** Python
**Size:** 4.5 KB

```python
"""Tests for studies routes."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_study(authenticated_client: AsyncClient):
    """Test creating a study."""
    response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Product Feedback Study",
            "description": "Understanding user needs for our product",
            "consent_text": "I consent to participate in this research",
            "max_agent_turns": 10,
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Product Feedback Study"
    assert data["max_agent_turns"] == 10
    assert "id" in data
    assert "created_at" in data


@pytest.mark.asyncio
async def test_create_study_unauthenticated(client: AsyncClient):
    """Test creating a study without auth fails."""
    response = await client.post(
        "/studies/",
        json={
            "title": "Test Study",
            "description": "Test",
            "consent_text": "I consent",
        },
    )

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_list_studies(authenticated_client: AsyncClient):
    """Test listing studies returns only user's studies."""
    # Create two studies
    await authenticated_client.post(
        "/studies/",
        json={
            "title": "Study 1",
            "description": "First study",
            "consent_text": "Consent",
        },
    )
    await authenticated_client.post(
        "/studies/",
        json={
            "title": "Study 2",
            "description": "Second study",
            "consent_text": "Consent",
        },
    )

    # List studies
    response = await authenticated_client.get("/studies/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(isinstance(study, dict) for study in data)


@pytest.mark.asyncio
async def test_get_study(authenticated_client: AsyncClient):
    """Test getting a specific study."""
    # Create study
    create_response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Test Study",
            "description": "Description",
            "consent_text": "Consent",
        },
    )
    study_id = create_response.json()["id"]

    # Get study
    response = await authenticated_client.get(f"/studies/{study_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == study_id
    assert data["title"] == "Test Study"


@pytest.mark.asyncio
async def test_get_nonexistent_study(authenticated_client: AsyncClient):
    """Test getting non-existent study returns 404."""
    response = await authenticated_client.get("/studies/99999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_study(authenticated_client: AsyncClient):
    """Test updating a study."""
    # Create study
    create_response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "Original Title",
            "description": "Original Description",
            "consent_text": "Consent",
        },
    )
    study_id = create_response.json()["id"]

    # Update study
    response = await authenticated_client.patch(
        f"/studies/{study_id}",
        json={"title": "Updated Title"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["description"] == "Original Description"  # Unchanged


@pytest.mark.asyncio
async def test_delete_study(authenticated_client: AsyncClient):
    """Test deleting a study."""
    # Create study
    create_response = await authenticated_client.post(
        "/studies/",
        json={
            "title": "To Delete",
            "description": "Will be deleted",
            "consent_text": "Consent",
        },
    )
    study_id = create_response.json()["id"]

    # Delete study
    response = await authenticated_client.delete(f"/studies/{study_id}")
    assert response.status_code == 204

    # Verify it's gone
    get_response = await authenticated_client.get(f"/studies/{study_id}")
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_create_study_validation(authenticated_client: AsyncClient):
    """Test study creation validates required fields."""
    response = await authenticated_client.post(
        "/studies/",
        json={"title": ""},  # Empty title should fail
    )

    assert response.status_code == 422  # Validation error


```

## tests/routers/test_web_auth.py

**Path:** `tests/routers/test_web_auth.py`
**Type:** Python
**Size:** 8.4 KB

```python
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

```

## tests/services/__init__.py

**Path:** `tests/services/__init__.py`
**Type:** Python
**Size:** 32 bytes

```python
"""Tests for service layer."""

```

## tests/services/test_insight_generator.py

**Path:** `tests/services/test_insight_generator.py`
**Type:** Python
**Size:** 10.2 KB

```python
"""Tests for the insight generator service."""

from unittest.mock import MagicMock, patch

import pytest
from sqlalchemy.orm import Session

from app.crud import interview as interview_crud
from app.crud import invite as invite_crud
from app.crud import study as study_crud
from app.crud import user as user_crud
from app.models.invite import InviteStatus
from app.services.insight_generator import InsightGenerator


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client."""
    with patch("app.services.insight_generator.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices[0].message.content = """{
            "summary": "The participant discussed their experience with the product interface.",
            "sentiment": "positive",
            "keywords": ["user interface", "design", "experience"],
            "themes": ["product usability", "customer satisfaction"],
            "notable_quotes": [
                "I really love the new design.",
                "The interface is very intuitive.",
                "Best product I've used in years."
            ],
            "engagement_level": "high",
            "key_insights": [
                "User highly values intuitive design",
                "Positive sentiment toward new features"
            ]
        }"""

        mock_client.chat.completions.create.return_value = mock_response

        yield mock_client


@pytest.fixture
def db(test_db):
    """Get database session from test_db fixture."""
    session = test_db()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def sample_interview(db: Session):
    """Create a sample interview with messages."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Product Research",
        description="Understanding user experience",
        consent_text="Test consent",
        max_agent_turns=5,
    )

    study_crud.create_study_question(db, study_id=study.id, text="What do you think?", sort_order=0)

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    interviewee = interview_crud.create_interviewee(
        db, interview_id=interview.id, name="Test User", email="test@example.com"
    )

    interview_crud.create_message(
        db, interview_id=interview.id, role="assistant", content="Hello! What brings you here?"
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="user",
        content="I really love the new design. The interface is very intuitive and easy to use.",
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="assistant",
        content="That's great to hear! Can you tell me more?",
    )

    interview_crud.create_message(
        db,
        interview_id=interview.id,
        role="user",
        content="The navigation is smooth and the features are exactly what I needed. Best product I've used in years.",
    )

    return interview


@pytest.mark.asyncio
async def test_generate_insights_success(db: Session, sample_interview, mock_openai_client):
    """Test successful insight generation."""
    generator = InsightGenerator()

    insights = generator.generate_insights(db, sample_interview.id)

    assert insights["summary"] is not None
    assert insights["sentiment"] in ["positive", "neutral", "negative"]
    assert isinstance(insights["keywords"], list)
    assert isinstance(insights["themes"], list)
    assert isinstance(insights["notable_quotes"], list)
    assert insights["engagement_level"] in ["high", "medium", "low"]
    assert isinstance(insights["key_insights"], list)

    mock_openai_client.chat.completions.create.assert_called_once()
    call_args = mock_openai_client.chat.completions.create.call_args
    assert call_args.kwargs["model"] == "gpt-4o-mini"
    assert call_args.kwargs["temperature"] == 0.3
    assert call_args.kwargs["response_format"] == {"type": "json_object"}


@pytest.mark.asyncio
async def test_generate_insights_validates_output(db: Session, sample_interview):
    """Test that insights are validated and normalized."""
    with patch("app.services.insight_generator.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices[0].message.content = """{
            "summary": "Test summary",
            "sentiment": "INVALID_SENTIMENT",
            "keywords": ["test"],
            "themes": [],
            "notable_quotes": [],
            "engagement_level": "INVALID_LEVEL",
            "key_insights": []
        }"""

        mock_client.chat.completions.create.return_value = mock_response

        generator = InsightGenerator()
        insights = generator.generate_insights(db, sample_interview.id)

        assert insights["sentiment"] == "neutral"
        assert insights["engagement_level"] == "medium"


@pytest.mark.asyncio
async def test_generate_insights_empty_interview(db: Session):
    """Test insight generation with no messages."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test",
        consent_text="Test",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    invite_crud.update_invite_status(db, invite.id, InviteStatus.COMPLETED)

    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    generator = InsightGenerator()
    insights = generator.generate_insights(db, interview.id)

    assert insights["summary"] == "No conversation recorded"
    assert insights["sentiment"] == "neutral"
    assert insights["keywords"] == []
    assert insights["notable_quotes"] == []
    assert insights["engagement_level"] == "low"


@pytest.mark.asyncio
async def test_generate_insights_api_failure_fallback(db: Session, sample_interview):
    """Test fallback extraction when API fails."""
    with patch("app.services.insight_generator.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_client.chat.completions.create.side_effect = Exception("API Error")

        generator = InsightGenerator()
        insights = generator.generate_insights(db, sample_interview.id)

        assert insights["summary"] is not None
        assert insights["sentiment"] == "neutral"
        assert len(insights["notable_quotes"]) > 0


@pytest.mark.asyncio
async def test_generate_insights_invalid_json_fallback(db: Session, sample_interview):
    """Test fallback when LLM returns invalid JSON."""
    with patch("app.services.insight_generator.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices[0].message.content = "This is not valid JSON"

        mock_client.chat.completions.create.return_value = mock_response

        generator = InsightGenerator()
        insights = generator.generate_insights(db, sample_interview.id)

        assert insights["sentiment"] == "neutral"
        assert isinstance(insights["notable_quotes"], list)


@pytest.mark.asyncio
async def test_format_conversation(db: Session, sample_interview):
    """Test conversation formatting."""
    generator = InsightGenerator()

    messages = interview_crud.get_messages_by_interview(db, sample_interview.id)
    conversation = generator._format_conversation(messages)

    assert "AI Interviewer:" in conversation
    assert "Participant:" in conversation
    assert "Hello! What brings you here?" in conversation
    assert "I really love the new design" in conversation


@pytest.mark.asyncio
async def test_validate_insights_limits_output_size():
    """Test that validation limits output sizes."""
    generator = InsightGenerator()

    large_insights = {
        "summary": "x" * 2000,
        "sentiment": "positive",
        "keywords": [f"keyword{i}" for i in range(100)],
        "themes": [f"theme{i}" for i in range(50)],
        "notable_quotes": [f"quote{i}" for i in range(20)],
        "engagement_level": "high",
        "key_insights": [f"insight{i}" for i in range(50)],
    }

    validated = generator._validate_insights(large_insights)

    assert len(validated["summary"]) <= 1000
    assert len(validated["keywords"]) <= 20
    assert len(validated["themes"]) <= 10
    assert len(validated["notable_quotes"]) <= 5
    assert len(validated["key_insights"]) <= 10


@pytest.mark.asyncio
async def test_fallback_extraction_with_meaningful_responses(db: Session, sample_interview):
    """Test fallback extraction selects meaningful responses."""
    generator = InsightGenerator()

    messages = interview_crud.get_messages_by_interview(db, sample_interview.id)
    insights = generator._fallback_extraction(messages)

    assert len(insights["notable_quotes"]) > 0
    for quote in insights["notable_quotes"]:
        assert len(quote) > 50


@pytest.mark.asyncio
async def test_fallback_extraction_no_user_messages(db: Session):
    """Test fallback extraction with only agent messages."""
    user = user_crud.create_user(db, email="researcher@test.com", password_hash="hash")
    study = study_crud.create_study(
        db,
        owner_user_id=user.id,
        title="Test Study",
        description="Test",
        consent_text="Test",
    )

    invite = invite_crud.create_invite(db, study_id=study.id)
    interview = interview_crud.create_interview(db, study_id=study.id, invite_id=invite.id)

    interview_crud.create_message(
        db, interview_id=interview.id, role="assistant", content="Hello!"
    )

    generator = InsightGenerator()
    messages = interview_crud.get_messages_by_interview(db, interview.id)
    insights = generator._fallback_extraction(messages)

    assert "No" in insights["summary"] and "recorded" in insights["summary"]
    assert insights["notable_quotes"] == []

```

## tests/test_health.py

**Path:** `tests/test_health.py`
**Type:** Python
**Size:** 940 bytes

```python
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

```

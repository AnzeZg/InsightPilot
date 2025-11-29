# InsightPilot

[![CI](https://github.com/AnzeZg/InsightPilot/actions/workflows/ci.yml/badge.svg)](https://github.com/AnzeZg/InsightPilot/actions/workflows/ci.yml)
[![CD](https://github.com/AnzeZg/InsightPilot/actions/workflows/cd.yml/badge.svg)](https://github.com/AnzeZg/InsightPilot/actions/workflows/cd.yml)

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
- ✅ **Well Tested** - 265 comprehensive tests (unit + integration)
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
| **Testing** | Pytest, HTTPX, pytest-asyncio (265 tests, 74%+ coverage) |
| **Code Quality** | Ruff, isort, pre-commit hooks |
| **CI/CD** | GitHub Actions (separate CI/CD workflows) |
| **Deployment** | Docker, Azure App Service, Azure Container Registry |
| **Monitoring** | Prometheus, Grafana, Azure Application Insights |

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
├── tests/                        # Test suite (265 tests)
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

The project includes comprehensive test coverage across **265 tests** covering unit tests, integration tests, and end-to-end workflows, with **74%+ code coverage**.

### Test Architecture

- **Unit Tests (163 tests)** - Test individual functions in isolation (CRUD operations, auth utilities)
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

**Total: 265 tests passing** ✅

#### Unit Tests (163 tests)

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
# Lint with Ruff
ruff check app tests

# Format code with Ruff
ruff format app tests

# Sort imports with isort
isort app tests

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
- **ruff** - Fast Python linter with auto-fix
- **ruff-format** - Code formatting (replaces Black)
- **isort** - Import sorting
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

### Production Deployment

The application is deployed to **Azure App Service** with full CI/CD automation:

- **Live URL**: https://azgonc-insightpilot.azurewebsites.net
- **CI/CD**: GitHub Actions with separate CI and CD workflows
- **Container Registry**: Azure Container Registry (ACR)
- **Database**: Azure Database for PostgreSQL (Flexible Server)
- **Monitoring**: Azure Application Insights + Prometheus metrics at `/metrics`

For detailed deployment information, see [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).

### Production Considerations

- **Environment**: Set `APP_ENV=prod`
- **Secret Key**: Use strong, unique secret key
- **Database**: Use managed PostgreSQL service with SSL
- **Monitoring**: Prometheus metrics exposed at `/metrics`, Azure Application Insights for APM
- **Health Checks**: `/healthz` endpoint for load balancer and orchestration
- **HTTPS**: Enabled by default on Azure App Service
- **Scaling**: Azure App Service supports horizontal and vertical scaling

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

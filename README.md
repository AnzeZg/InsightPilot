# InsightPilot

An AI-powered market research platform that conducts intelligent interviews with participants and automatically generates actionable insights.

## Overview

InsightPilot enables researchers to create studies, generate interview links, and conduct AI-driven interviews with participants. The system automatically analyzes responses and provides comprehensive analytics including sentiment analysis, keyword extraction, demographics breakdowns, and data export capabilities.

## Features

### 🔐 **Authentication & User Management**
- User registration and login with secure password hashing (Argon2)
- Server-side session management with signed cookies
- Protected routes with automatic redirect to login
- Development quick-auth for testing

### 📊 **Study Management**
- Create and manage research studies
- Configure seed questions and consent forms
- Generate unique interview invitation links
- Track interview completion status

### 🤖 **AI-Powered Interviews**
- Conversational AI agent conducts natural interviews
- Dynamic follow-up questions based on responses
- Configurable turn limits
- Real-time chat interface with HTMX

### 📈 **Analytics & Insights**
- **Sentiment Distribution**: Positive, neutral, and negative sentiment analysis
- **Top Keywords**: Frequency analysis of key themes
- **Demographics Breakdown**: Participant demographic insights
- **Interview Timeline**: Track completion over time
- **Response Metrics**: Average message counts and conversation length
- **Notable Quotes**: Automatically extracted significant responses

### 💾 **Data Export**
- Export individual interviews or entire studies
- CSV and JSON formats
- Complete transcripts with metadata
- Demographics and sentiment data included

### 🎨 **Modern UI**
- Clean, responsive design with Tailwind CSS
- Interactive dashboards with Chart.js visualizations
- HTMX-powered dynamic updates
- Mobile-friendly interface

## Tech Stack

- **Backend**: FastAPI + Uvicorn
- **Frontend**: Jinja2 templates + HTMX + Tailwind CSS + Chart.js
- **Database**: PostgreSQL + SQLAlchemy 2.0 + Alembic migrations
- **Auth**: Server-side sessions with signed cookies (Argon2 password hashing)
- **AI/LLM**: OpenAI API (configurable provider)
- **Testing**: Pytest + HTTPX + pytest-asyncio
- **Code Quality**: Pre-commit hooks (black, isort, ruff)
- **Deployment**: Docker + Docker Compose

## Prerequisites

- **Python 3.11+** (Python 3.13 recommended)
- **Docker and Docker Compose** (for containerized setup)
- **OpenAI API Key** (or compatible LLM provider)
- **PostgreSQL** (runs in Docker, not needed locally)

## Quick Start

### Option 1: Docker (Recommended for Production)

```bash
# 1. Clone the repository
git clone <repo-url>
cd InsightPilot

# 2. Create environment file
cp .env.example .env

# 3. Edit .env with required settings (see Environment Variables section)
# At minimum, set:
#   - SECRET_KEY (generate with: python -c "import secrets; print(secrets.token_urlsafe(32))")
#   - OPENAI_API_KEY (your OpenAI API key)

# 4. Build and start services
docker compose up --build

# 5. Access the application
open http://localhost:8000

# 6. Create your first account
# Visit http://localhost:8000/register
```

### Option 2: Local Development

```bash
# 1. Clone the repository
git clone <repo-url>
cd InsightPilot

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies (includes dev tools)
pip install -e ".[dev]"

# 4. Set up environment variables
cp .env.example .env

# 5. Edit .env with your configuration:
#   - DATABASE_URL=postgresql://user:password@localhost:5432/insightpilot
#   - SECRET_KEY=<generate-secure-key>
#   - OPENAI_API_KEY=<your-api-key>

# 6. Start PostgreSQL (if not using Docker for DB)
# Or use Docker just for the database:
docker compose up -d db

# 7. Run database migrations
alembic upgrade head

# 8. Start the development server
uvicorn app.main:app --reload

# 9. Access the application
open http://localhost:8000
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# Application Settings
ENVIRONMENT=development  # development, staging, or production
SECRET_KEY=your-secret-key-here  # Generate: python -c "import secrets; print(secrets.token_urlsafe(32))"

# Database Configuration
DATABASE_URL=postgresql://postgres:password@db:5432/insightpilot  # Docker
# DATABASE_URL=postgresql://user:password@localhost:5432/insightpilot  # Local

# OpenAI Configuration (Required for AI interviews)
OPENAI_API_KEY=sk-your-openai-api-key
OPENAI_MODEL=gpt-4  # or gpt-3.5-turbo for lower costs

# Server Configuration
HOST=0.0.0.0
PORT=8000

# Logging
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
```

### Generating a Secure Secret Key

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## First-Time Setup

### 1. Create Database Schema

```bash
# Apply all migrations
alembic upgrade head

# Verify migrations were applied
alembic current
```

### 2. Create Your First Account

**Option A: Via Web Interface**
1. Visit http://localhost:8000
2. Click "Get Started" or navigate to http://localhost:8000/register
3. Fill in email and password (min 8 characters)
4. Login at http://localhost:8000/login

**Option B: Quick Development Auth**
```bash
# Creates test@example.com / password123 and logs you in
open http://localhost:8000/auth/dev/quick-auth
```

### 3. Create Your First Study

1. Navigate to http://localhost:8000/app/studies
2. Click "Create New Study"
3. Fill in:
   - **Title**: e.g., "Product Feedback Survey"
   - **Description**: Study purpose and goals
   - **Consent Text**: Required consent for participants
   - **Max Agent Turns**: Limit AI responses (e.g., 10)
4. Add seed questions to guide the AI interviewer
5. Generate invitation links to share with participants

## Testing

### Run All Tests

```bash
# Local environment
pytest -v

# With coverage report
pytest --cov=app --cov-report=html

# Docker environment
docker compose exec app pytest -v
```

### Run Specific Test Suites

```bash
# Authentication tests
pytest tests/routers/test_auth_dev.py -v
pytest tests/routers/test_web_auth.py -v

# Analytics tests
pytest tests/routers/test_analytics.py -v

# Export functionality
pytest tests/routers/test_export.py -v

# Interview flow tests
pytest tests/interview/ -v
```

### Test Coverage

Current test coverage: **100 tests passing** ✅

- Authentication (API + Web): 24 tests
- Study management: 12 tests
- Interview flow: 15 tests
- Analytics: 7 tests
- Data export: 11 tests
- Health checks: 3 tests
- Others: 28 tests

## Development Workflow

### 1. Set Up Pre-commit Hooks

```bash
# Install hooks (recommended)
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

### 2. Code Quality Tools

The project uses several code quality tools:

- **Black**: Code formatting (line length: 100)
- **isort**: Import sorting
- **Ruff**: Fast Python linter
- **Pytest**: Testing framework

### 3. Running Development Server

```bash
# Standard mode
uvicorn app.main:app --reload

# Custom port
uvicorn app.main:app --reload --port 8080

# With debug logging
LOG_LEVEL=DEBUG uvicorn app.main:app --reload
```

## Project Structure

```
InsightPilot/
├── app/
│   ├── auth/              # Authentication and session management
│   │   ├── dependencies.py    # Auth dependencies for routes
│   │   └── sessions.py        # Session cookie management
│   ├── crud/              # Database operations (Create, Read, Update, Delete)
│   │   ├── interview.py
│   │   ├── study.py
│   │   └── user.py
│   ├── db/                # Database configuration
│   │   ├── base.py
│   │   └── session.py
│   ├── models/            # SQLAlchemy ORM models
│   │   ├── interview.py
│   │   ├── study.py
│   │   ├── user.py
│   │   └── invite.py
│   ├── routers/           # FastAPI route handlers
│   │   ├── auth_dev.py        # Dev authentication endpoints
│   │   ├── web_auth.py        # Web auth pages (login/register)
│   │   ├── studies.py         # API routes for studies
│   │   ├── web_studies.py     # Web pages for studies
│   │   ├── interview.py       # Interview endpoints
│   │   └── health.py          # Health check endpoint
│   ├── schemas/           # Pydantic models for validation
│   │   ├── interview.py
│   │   ├── study.py
│   │   └── invite.py
│   ├── services/          # Business logic and external services
│   │   ├── ai_agent.py        # LLM conversation wrapper
│   │   └── insight_generator.py  # AI-powered insight generation
│   ├── templates/         # Jinja2 HTML templates
│   │   ├── auth/              # Login, register pages
│   │   ├── interview/         # Interview chat interface
│   │   ├── studies/           # Study management, analytics
│   │   └── base.html
│   ├── static/            # CSS, JavaScript, images
│   │   ├── css/app.css
│   │   └── js/app.js
│   ├── utils/             # Utilities and helpers
│   │   └── logging.py
│   ├── middleware.py      # Custom middleware (request ID, logging)
│   ├── settings.py        # Configuration and environment variables
│   └── main.py            # FastAPI application entry point
├── tests/                 # Pytest test suite
│   ├── routers/           # API route tests
│   ├── interview/         # Interview flow tests
│   ├── services/          # Service layer tests
│   └── conftest.py        # Pytest fixtures
├── alembic/               # Database migrations
│   ├── versions/          # Migration files
│   └── env.py
├── docker-compose.yml     # Container orchestration
├── Dockerfile             # Application container
├── pyproject.toml         # Project metadata and dependencies
├── alembic.ini            # Alembic configuration
└── README.md              # This file
```

## API Documentation

Once the server is running, interactive API documentation is available at:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key API Endpoints

#### Authentication
- `POST /auth/dev/register` - Create new user account
- `POST /auth/dev/login` - Login and get session cookie
- `POST /auth/dev/logout` - Clear session and logout
- `GET /auth/dev/quick-auth` - Quick dev auth (test@example.com)

#### Studies
- `GET /studies` - List all studies for authenticated user
- `POST /studies` - Create a new study
- `GET /studies/{id}` - Get study details
- `GET /studies/{id}/analytics` - Get study analytics
- `GET /studies/{id}/export` - Export study data (CSV/JSON)

#### Interviews
- `GET /interview/{invite_code}` - Start interview from invite
- `POST /interview/{invite_code}/message` - Send message in interview
- `GET /studies/{id}/interviews` - List study interviews
- `GET /studies/{id}/interviews/{interview_id}/transcript` - View transcript

## Database Management

### Alembic Migrations

Alembic manages database schema changes. When you modify ORM models, generate and apply migrations.

#### Common Commands

```bash
# Check current database version
alembic current

# View migration history
alembic history --verbose

# Generate migration from model changes
alembic revision --autogenerate -m "describe your changes"

# Apply all pending migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# Rollback to specific revision
alembic downgrade <revision_id>

# Reset database (WARNING: deletes all data)
alembic downgrade base
alembic upgrade head
```

#### Migration Workflow

1. **Modify Models**: Edit SQLAlchemy models in `app/models/`
2. **Generate Migration**: `alembic revision --autogenerate -m "add user avatar field"`
3. **Review**: Check the generated file in `alembic/versions/`
4. **Apply**: `alembic upgrade head`
5. **Commit**: Add migration file to git

### Database Backup and Restore

```bash
# Backup (Docker)
docker compose exec db pg_dump -U postgres insightpilot > backup.sql

# Restore (Docker)
docker compose exec -T db psql -U postgres insightpilot < backup.sql

# Backup (Local)
pg_dump -U user insightpilot > backup.sql

# Restore (Local)
psql -U user insightpilot < backup.sql
```

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 8000 (macOS/Linux)
lsof -ti:8000

# Kill the process
kill -9 $(lsof -ti:8000)

# Windows
netstat -ano | findstr :8000
taskkill /PID <process_id> /F
```

### Database Connection Issues

```bash
# Check if PostgreSQL is running (Docker)
docker compose ps

# View database logs
docker compose logs db

# Verify DATABASE_URL in .env
echo $DATABASE_URL

# Test connection manually
psql $DATABASE_URL -c "SELECT version();"
```

### Migration Issues

```bash
# Check current migration state
alembic current

# If migrations are out of sync
alembic stamp head  # Mark current DB as up-to-date

# If you need to reset everything (DANGER: deletes data)
alembic downgrade base
alembic upgrade head
```

### OpenAI API Errors

```bash
# Verify API key is set
echo $OPENAI_API_KEY

# Test API key directly
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"

# Check rate limits in logs
grep -i "rate limit" logs/app.log
```

### Import Errors After Adding Dependencies

```bash
# Reinstall in development mode
pip install -e ".[dev]"

# Or reinstall specific package
pip install package-name
```

### HTMX Not Working

1. Check browser console for errors
2. Verify `/static/js/app.js` is loading
3. Check network tab for HTMX requests
4. Ensure HTMX CDN is accessible

### Session/Authentication Issues

```bash
# Clear browser cookies
# In Chrome: DevTools > Application > Cookies

# Check if SECRET_KEY is set
echo $SECRET_KEY

# Verify session creation in logs
grep "session" logs/app.log
```

## License

MIT License - see LICENSE file for details

## Acknowledgments

Built with:
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [HTMX](https://htmx.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Chart.js](https://www.chartjs.org/)
- [OpenAI](https://openai.com/)

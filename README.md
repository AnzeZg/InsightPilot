# InsightPilot

A market research tool that uses LLMs to conduct market research interviews.

## Overview

InsightPilot enables researchers to create studies, generate interview links, and conduct AI-driven interviews with participants. The system automatically generates insights including summaries, sentiment analysis, keywords, and notable quotes.

## Tech Stack

- **Backend**: FastAPI + Uvicorn
- **Frontend**: Jinja2 templates + HTMX + Tailwind CSS
- **Database**: PostgreSQL + SQLAlchemy 2.0 + Alembic
- **Auth**: Server-side sessions with signed cookies (researchers only)
- **LLM**: Provider API via httpx wrapper
- **Deployment**: Docker + Docker Compose

## Quick Start

### Prerequisites

- Python 3.11+ (for local development)
- Docker and Docker Compose (for containerized setup)
- **Note**: PostgreSQL is NOT required locally - it runs in Docker

### Option 1: Docker (Recommended)

```bash
# Clone and navigate
git clone <repo-url>
cd InsightPilot

# Copy environment file
cp .env.example .env
# Edit .env with your SECRET_KEY and other settings

# Build and run
docker compose up --build

# Access the app
open http://localhost:8000
```

### Option 2: Local Development

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (editable mode with dev tools)
pip install -e ".[dev]"

# Set up environment
cp .env.example .env
# Edit .env with your DATABASE_URL and SECRET_KEY

# Run migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload

# Access the app
open http://localhost:8000
```

### Running Tests

```bash
# With Docker
docker compose exec app pytest -v

# Local
pytest -v
```

### Pre-commit Hooks

```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

## Project Structure

```
InsightPilot/
├── app/
│   ├── auth/          # Authentication and session management
│   ├── db/            # Database configuration and base
│   ├── models/        # SQLAlchemy ORM models
│   ├── routers/       # FastAPI route handlers
│   ├── services/      # Business logic and LLM wrapper
│   ├── templates/     # Jinja2 HTML templates
│   ├── static/        # CSS, JS, and static assets
│   ├── utils/         # Logging and utilities
│   └── main.py        # FastAPI application entry point
├── tests/             # Pytest test suite
├── alembic/           # Database migrations
├── docker-compose.yml # Container orchestration
├── Dockerfile         # Application container
└── pyproject.toml     # Project metadata and dependencies
```

## Development Workflow

1. Create a feature branch: `git checkout -b day1/feature-name`
2. Make changes and commit using conventional commits:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `chore:` for tooling/config
   - `docs:` for documentation
   - `test:` for tests
3. Run tests and linters: `pytest && pre-commit run --all-files`
4. Push and open a PR

## Troubleshooting

### Database Connection Issues

- Ensure PostgreSQL is running: `docker compose ps`
- Check `DATABASE_URL` in `.env` matches your setup
- Verify network connectivity: `docker compose logs db`

### Migration Issues

```bash
# Check current migration status
alembic current

# View migration history
alembic history

# Reset (WARNING: drops all data)
alembic downgrade base
alembic upgrade head
```

### Port Already in Use

```bash
# Find process using port 8000
lsof -ti:8000

# Kill the process (macOS/Linux)
kill -9 $(lsof -ti:8000)
```

## Alembic: quick guide

Alembic manages database schema changes (migrations). You change ORM models, generate a migration, review it, and apply it to the database.

Key files:
- `alembic.ini`: Alembic config. We keep the DB URL commented here and set it dynamically in `alembic/env.py` using app settings.
- `alembic/env.py`: Wires Alembic to our app. It imports `Base` and all models, sets `sqlalchemy.url` from `settings.database_url`, and defines how to run migrations online/offline.
- `alembic/script.py.mako`: Template used when creating new migration files. It fills in `upgrade()` and `downgrade()` blocks.
- `alembic/versions/*.py`: Actual migration scripts. Each has `revision`, `down_revision`, and the `upgrade()`/`downgrade()` functions with `op.create_table(...)`, `op.add_column(...)`, etc.

Common commands:
```bash
# Generate a migration from model changes (review the new file in alembic/versions)
alembic revision --autogenerate -m "describe change"

# Apply all pending migrations
alembic upgrade head

# Step back one migration
alembic downgrade -1

# Show current DB revision
alembic current
```

Workflow:
1) Edit SQLAlchemy models in `app/models/*`.
2) Run `alembic revision --autogenerate -m "..."`.
3) Review the generated file under `alembic/versions/`.
4) Run `alembic upgrade head` to apply.

## Environment Variables

See `.env.example` for all available configuration options.


## License

MIT


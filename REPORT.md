# InsightPilot DevOps Report

**Project:** InsightPilot - AI-Powered Market Research Platform
**Author:** Anže Zgornik
**Date:** November 2025
**Course:** DevOps - Year 3, Semester 1

---

## 1. Executive Summary

### Project Overview

InsightPilot is an AI-powered market research platform that enables researchers to conduct intelligent interviews with participants and automatically generate actionable insights. The platform combines conversational AI (OpenAI GPT models) with automated analysis to streamline qualitative research workflows.

### Key Achievements

This DevOps project successfully transformed InsightPilot from a functional prototype into a production-grade application with:

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Test Count** | 254 | 265 | +4.3% |
| **Code Coverage** | ~65% | 74%+ | Exceeds 70% target |
| **Linter Violations** | 928 | 4 | 99.6% reduction |
| **Long Methods (>50 LOC)** | 1 (131 lines) | 0 | 100% eliminated |
| **Hardcoded Values** | ~15 | 0 | 100% extracted |
| **CI/CD Automation** | None | Full pipeline | Automated deployment |
| **Monitoring** | None | Prometheus + Grafana + Azure App Insights | Full observability |

### Final System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PRODUCTION (Azure)                           │
│  ┌────────────┐    ┌────────────────────┐    ┌─────────────────┐   │
│  │   GitHub   │───►│  Azure Container   │───►│  Azure App      │   │
│  │   Actions  │    │  Registry (ACR)    │    │  Service        │   │
│  │  (CI/CD)   │    └────────────────────┘    │  (Container)    │   │
│  └────────────┘                              └────────┬────────┘   │
│                                                       │            │
│                                              ┌────────▼────────┐   │
│  ┌────────────────────────┐                  │  PostgreSQL     │   │
│  │  Application Insights  │◄─────────────────│  (Azure DB)     │   │
│  │  (APM + Logs)          │                  └─────────────────┘   │
│  └────────────────────────┘                                        │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                    LOCAL DEVELOPMENT (Docker)                       │
│  ┌─────────────┐    ┌────────────┐    ┌────────────┐               │
│  │  FastAPI    │───►│ Prometheus │───►│  Grafana   │               │
│  │  App:8000   │    │   :9090    │    │   :3001    │               │
│  └──────┬──────┘    └────────────┘    └────────────┘               │
│         │                                                           │
│  ┌──────▼──────┐                                                   │
│  │ PostgreSQL  │                                                   │
│  │   :5432     │                                                   │
│  └─────────────┘                                                   │
└─────────────────────────────────────────────────────────────────────┘
```

**Production URL:** https://azgonc-insightpilot.azurewebsites.net

---

## 2. Code Quality Improvements

### 2.1 Initial Assessment

The project began with a comprehensive code quality baseline analysis revealing several areas for improvement:

- **928 linter violations** across the codebase
- **Critical SRP violation** in `get_study_analytics()` (131 lines)
- **15+ hardcoded values** scattered throughout
- **Code duplication** in 4 distinct areas
- **Mixed documentation styles** and inconsistent type hints

### 2.2 SOLID Principles Applied

**Single Responsibility Principle (SRP):**

The most significant refactoring addressed the `get_study_analytics()` function, which violated SRP by handling 7 different responsibilities in 131 lines.

*Before:*
```python
# app/routers/studies.py - 131 lines doing everything
async def get_study_analytics(study_id: int, db: Session):
    # Fetches data, calculates sentiment, aggregates keywords,
    # computes metrics, processes demographics, builds timeline,
    # extracts quotes - all in one function
```

*After:*
```python
# app/services/analytics_service.py - Clean separation
class StudyAnalyticsService:
    def generate_analytics(self, interviews) -> dict
    def _calculate_sentiment(self, insights) -> dict
    def _aggregate_keywords(self, insights) -> list
    def _calculate_metrics(self, messages) -> dict
    def _process_demographics(self, interviews) -> dict
    def _build_timeline(self, interviews) -> list
    def _extract_quotes(self, insights) -> list
```

**Dependency Inversion Principle (DIP):**

Created `app/services/openai_factory.py` to centralize OpenAI client creation, enabling easier testing and future flexibility to swap AI providers.

### 2.3 Code Duplication Eliminated

| Area | Before | After |
|------|--------|-------|
| Study ownership verification | Duplicated in 2 routers | Centralized in `crud/study.py` |
| Date/JSON formatting | Duplicated formatters | Single `utils/formatters.py` |
| OpenAI client creation | Repeated in 2 services | Factory pattern in `openai_factory.py` |

### 2.4 Constants Extraction

Created `app/constants.py` with 16 named constants replacing magic numbers:

```python
# Session configuration
SESSION_MAX_AGE_SECONDS = 60 * 60 * 24 * 7  # 7 days

# AI Agent configuration
DEFAULT_AI_MODEL = "gpt-4o-mini"
AI_MAX_TOKENS = 300
AI_TEMPERATURE = 0.75
AI_MAX_TURNS = 25

# Analytics configuration
TOP_KEYWORDS_LIMIT = 20
SAMPLE_QUOTES_LIMIT = 10
```

### 2.5 New Modules Created

| Module | Purpose | Lines |
|--------|---------|-------|
| `app/constants.py` | Centralized configuration values | 45 |
| `app/services/analytics_service.py` | Business logic for analytics | 178 |
| `app/services/openai_factory.py` | Factory for OpenAI clients | 50 |
| `app/utils/formatters.py` | Common formatting utilities | 37 |
| `app/metrics.py` | Prometheus metric definitions | 120 |

---

## 3. Testing Strategy

### 3.1 Test Architecture

The project employs a comprehensive testing strategy following the test pyramid:

```
                    ┌───────────────┐
                    │    E2E (2)    │  ← Health check, smoke tests
                    ├───────────────┤
                    │Integration(100)│  ← API endpoints, workflows
                    ├───────────────┤
                    │  Unit (163)   │  ← CRUD, auth, services
                    └───────────────┘
                    Total: 265 tests
```

### 3.2 Test Categories

**Unit Tests (163 tests):**
- **CRUD Operations (116 tests):** User, session, study, invite, interview management
- **Authentication (38 tests):** Session cookies, auth dependencies, security validation
- **Services (9 tests):** AI insight generation, analytics service

**Integration Tests (100 tests):**
- **API Routes:** Full request/response cycles for all endpoints
- **Authentication Flows:** Login, registration, session management
- **Interview Workflows:** Complete participant journey from invite to completion
- **Analytics & Export:** CSV/JSON export functionality

### 3.3 Coverage Achievement

```
Coverage Report Summary:
------------------------
app/crud/          95%  (exceeds 95% target)
app/auth/          88%  (exceeds 80% target)
app/routers/       78%  (exceeds 75% target)
app/services/      72%  (exceeds 70% target)
------------------------
Overall:           74%  (exceeds 70% requirement)
```

### 3.4 Testing Tools

| Tool | Purpose |
|------|---------|
| `pytest` | Test framework with fixtures |
| `pytest-cov` | Coverage reporting |
| `pytest-asyncio` | Async test support |
| `httpx` | Async HTTP client for API tests |
| `unittest.mock` | Mocking external services (OpenAI) |

### 3.5 Test Execution

```bash
# Run all tests with coverage
pytest --cov=app --cov-report=term --cov-report=html

# Run specific test categories
pytest tests/crud/ -v      # Unit tests
pytest tests/routers/ -v   # Integration tests
pytest tests/auth/ -v      # Security tests
```

---

## 4. CI/CD Pipeline

### 4.1 Pipeline Architecture

The project uses a **two-workflow design** for clear separation of concerns:

```
┌────────────────────────────────────────────────────────────────┐
│                     CI WORKFLOW (ci.yml)                       │
│  Triggers: Push to main, Pull Requests to main                │
├────────────────────────────────────────────────────────────────┤
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌────────────┐  │
│  │  Ruff    │──►│  Ruff    │──►│  isort   │──►│  pytest    │  │
│  │  Lint    │   │  Format  │   │  Check   │   │ + Coverage │  │
│  └──────────┘   └──────────┘   └──────────┘   └────────────┘  │
│                                                     │          │
│                                     Coverage ≥70% check        │
│                                     Artifacts uploaded         │
└────────────────────────────────────────────────────────────────┘
                              │
                              │ (on success, main branch only)
                              ▼
┌────────────────────────────────────────────────────────────────┐
│                     CD WORKFLOW (cd.yml)                       │
│  Trigger: workflow_run (after CI succeeds on main)            │
├────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐   ┌──────────────┐   ┌────────────────────┐ │
│  │ Docker Build │──►│ Push to ACR  │──►│ Deploy to Azure    │ │
│  │ + Cache      │   │              │   │ App Service        │ │
│  └──────────────┘   └──────────────┘   └─────────┬──────────┘ │
│                                                   │            │
│                               ┌───────────────────▼──────────┐ │
│                               │ Health Check + Smoke Tests   │ │
│                               └──────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
```

### 4.2 CI Workflow Details

**File:** `.github/workflows/ci.yml`

**Quality Gates:**
1. **Ruff Linter** - Static code analysis with GitHub-formatted output
2. **Ruff Format** - Code formatting verification
3. **isort** - Import sorting check
4. **pytest** - Full test suite with coverage
5. **Coverage Threshold** - Fails if coverage < 70%

**Artifacts Generated:**
- `coverage.xml` - Codecov-compatible coverage report
- `htmlcov/` - Human-readable HTML coverage
- `test-results.xml` - JUnit-format test results

### 4.3 CD Workflow Details

**File:** `.github/workflows/cd.yml`

**Trigger Conditions:**
- Runs automatically after CI succeeds on `main` branch
- Manual trigger available via `workflow_dispatch` for hotfixes

**Jobs:**
1. **Build:** Docker image with BuildKit caching → Push to ACR
2. **Deploy:** Configure Azure App Service → Deploy container
3. **Smoke Tests:** Verify `/docs` and `/openapi.json` endpoints

### 4.4 Branch Protection

The CI/CD setup enforces quality through GitHub branch protection:
- PRs require passing CI before merge
- Direct pushes to `main` are discouraged
- All changes go through code quality checks

### 4.5 Secrets Management

| Secret | Purpose |
|--------|---------|
| `AZURE_CREDENTIALS` | Service Principal for Azure login |
| `ACR_USERNAME/PASSWORD` | Container Registry authentication |
| `DATABASE_URL` | Production PostgreSQL connection |
| `OPENAI_API_KEY` | AI service authentication |
| `SECRET_KEY` | Application session signing |
| `APPINSIGHTS_INSTRUMENTATION_KEY` | Azure monitoring |

---

## 5. Deployment & Containerization

### 5.1 Docker Strategy

**Multi-Stage Optimization:**

```dockerfile
FROM python:3.11-slim

# Security: Non-root user
RUN useradd -m -u 1000 appuser
USER appuser

# Health check for orchestration
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8000/healthz || exit 1

# Migrations + Server startup
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
```

**Image Characteristics:**
- Base: `python:3.11-slim` (minimal footprint)
- Size: ~250MB (optimized)
- Security: Non-root user execution
- Health: Built-in container health check

### 5.2 Azure Infrastructure

| Resource | Type | Configuration |
|----------|------|---------------|
| **App Service** | Web App for Containers | B1 Basic tier, Linux |
| **Container Registry** | ACR Basic | Private image storage |
| **PostgreSQL** | Flexible Server B1ms | 1 vCore, 2GB RAM, SSL required |
| **Application Insights** | Standard | APM + log aggregation |

### 5.3 Environment Configuration

**Production Environment Variables:**
```
ENVIRONMENT=production
DATABASE_URL=postgresql://...?sslmode=require
SECRET_KEY=<secure-random>
OPENAI_API_KEY=sk-...
APPINSIGHTS_INSTRUMENTATION_KEY=<instrumentation-key>
```

### 5.4 Deployment Verification

The CD pipeline includes automated verification:

1. **Health Check:** Polls `/healthz` up to 10 times with 10s intervals
2. **Smoke Tests:** Validates `/docs` and `/openapi.json` endpoints
3. **Rollback Ready:** Previous images retained in ACR for quick rollback

---

## 6. Monitoring & Observability

### 6.1 Monitoring Architecture

**Local Development:** Prometheus + Grafana stack via Docker Compose
**Production:** Azure Application Insights (native APM)

Both environments expose the same `/metrics` endpoint in Prometheus format.

### 6.2 Metrics Implemented

**HTTP Metrics (Automatic):**
- `http_requests_total` - Request count by method, endpoint, status
- `http_request_duration_seconds` - Latency histogram (p50, p95, p99)
- `http_request_size_bytes` / `http_response_size_bytes`

**Business Metrics (Custom):**
- `studies_total` / `studies_active` - Study tracking
- `interviews_total` / `interviews_active` - Interview lifecycle
- `ai_requests_total` - AI API call tracking with success/error labels
- `ai_request_duration_seconds` - AI latency monitoring

### 6.3 Health Check Endpoints

| Endpoint | Purpose | Response |
|----------|---------|----------|
| `/healthz` | Comprehensive health | Status, DB connectivity, latency |
| `/metrics` | Prometheus scraping | All metrics in Prometheus format |

**Health Check Response:**
```json
{
  "ok": true,
  "status": "healthy",
  "service": "insightpilot",
  "version": "0.1.0",
  "checks": {
    "database": {
      "status": "healthy",
      "latency_ms": 12.5
    }
  }
}
```

### 6.4 Pre-Configured Alerts

| Alert | Condition | Severity |
|-------|-----------|----------|
| HighErrorRate | >5% HTTP 5xx for 2min | Warning |
| SlowResponseTime | P95 >2s for 5min | Warning |
| DatabaseConnectionError | >10 errors in 5min | Critical |
| HighAIRequestFailureRate | >10% AI failures for 3min | Warning |
| ServiceDown | App unreachable for 1min | Critical |

### 6.5 Grafana Dashboard

The pre-built "InsightPilot Overview" dashboard includes 8 panels:
1. HTTP Request Rate (time series)
2. Error Rate (gauge with thresholds)
3. Response Time Percentiles (P50/P95/P99)
4. Interview Activity (by status)
5. Active Studies (stat)
6. Active Interviews (stat)
7. Active Sessions (stat)
8. AI P95 Latency (stat)

---

## 7. Lessons Learned

### 7.1 Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| OpenAI mocking in tests | Factory pattern with dependency injection |
| Pre-commit hook conflicts | Removed Black (redundant with Ruff-format) |
| Azure App Service metrics | Separate `/metrics` endpoint + App Insights |
| CI/CD separation | Two-workflow design with `workflow_run` trigger |
| SQLAlchemy type hints | Per-file mypy ignores for forward references |

### 7.2 Key Takeaways

1. **Automation is Essential:** Pre-commit hooks and CI pipelines catch issues before they reach production
2. **Observability First:** Prometheus metrics should be implemented early, not as an afterthought
3. **Test Coverage Matters:** The 70% threshold forced us to test edge cases we might have missed
4. **Separation of Concerns:** Splitting CI and CD workflows made the pipeline easier to understand and debug
5. **Documentation as Code:** Keeping docs in the repository ensures they stay synchronized with the code

### 7.3 Future Improvements

1. **Blue-Green Deployments:** Use Azure deployment slots for zero-downtime updates
2. **Database Backups:** Implement automated backup strategy with point-in-time restore
3. **Performance Testing:** Add load testing with Locust in CI pipeline
4. **Security Scanning:** Integrate Trivy for container vulnerability scanning
5. **Infrastructure as Code:** Migrate Azure resources to Terraform/Bicep

---

## 8. Conclusion

This DevOps project successfully transformed InsightPilot into a production-ready application with:

✅ **99.6% reduction** in code quality issues
✅ **74%+ test coverage** exceeding the 70% requirement
✅ **Fully automated CI/CD** with quality gates and deployment verification
✅ **Comprehensive monitoring** with Prometheus, Grafana, and Azure Application Insights
✅ **Secure containerized deployment** on Azure App Service
✅ **Clear documentation** for future maintainers

The application is now accessible at https://azgonc-insightpilot.azurewebsites.net with automated deployments triggered by merges to the `main` branch.

---

## References

### Repository Links
- **GitHub:** https://github.com/AnzeZg/InsightPilot
- **Production:** https://azgonc-insightpilot.azurewebsites.net
- **API Docs:** https://azgonc-insightpilot.azurewebsites.net/docs

### Documentation
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Monitoring Guide](docs/MONITORING.md)
- [CI/CD Configuration](docs/CI-CD.md)

### Technologies
- [FastAPI](https://fastapi.tiangolo.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/)

---

**Word Count:** ~2,800 words
**Page Estimate:** ~5-6 A4 pages

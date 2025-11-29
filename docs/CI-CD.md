# CI/CD Pipeline Documentation

## Overview

InsightPilot uses a two-workflow GitHub Actions setup for Continuous Integration and Continuous Deployment.

---

## Workflow Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    CI WORKFLOW                              │
│  File: .github/workflows/ci.yml                             │
│  Triggers: Push to main, PRs to main                        │
│                                                             │
│  Jobs:                                                      │
│  └── test (Lint & Test)                                     │
│      ├── Ruff linter                                        │
│      ├── Ruff format check                                  │
│      ├── isort import check                                 │
│      ├── pytest + coverage                                  │
│      └── Coverage threshold (70%)                           │
└─────────────────────────────────────────────────────────────┘
                         │
                         │ (on success, main branch only)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    CD WORKFLOW                              │
│  File: .github/workflows/cd.yml                             │
│  Trigger: workflow_run (after CI succeeds on main)          │
│                                                             │
│  Jobs:                                                      │
│  ├── build (Build & Push Docker Image)                      │
│  │   ├── Docker Buildx setup                                │
│  │   ├── ACR login                                          │
│  │   ├── Build with caching                                 │
│  │   └── Push to Azure Container Registry                   │
│  │                                                          │
│  ├── deploy (Deploy to Azure)                               │
│  │   ├── Azure login                                        │
│  │   ├── Configure App Service settings                     │
│  │   ├── Deploy container                                   │
│  │   └── Health check (10 retries)                          │
│  │                                                          │
│  └── smoke-tests (Post-Deployment Validation)               │
│      ├── Test /docs endpoint                                │
│      └── Test /openapi.json endpoint                        │
└─────────────────────────────────────────────────────────────┘
```

---

## CI Workflow (`ci.yml`)

### Triggers

- **Push to `main`** - Runs on every push (excluding docs changes)
- **Pull Request to `main`** - Validates before merge

### Quality Gates

| Check | Tool | Failure Condition |
|-------|------|-------------------|
| Linting | Ruff | Any lint errors |
| Formatting | Ruff format | Any format violations |
| Import Sorting | isort | Incorrect import order |
| Tests | pytest | Any failing tests |
| Coverage | pytest-cov | Coverage < 70% |

### Artifacts

| Artifact | Contents |
|----------|----------|
| `coverage-report` | `coverage.xml`, `htmlcov/` |
| `test-results` | `test-results.xml` (JUnit format) |

---

## CD Workflow (`cd.yml`)

### Triggers

- **`workflow_run`** - Automatically after CI succeeds on `main`
- **`workflow_dispatch`** - Manual trigger for hotfixes/rollbacks

### Build Job

```yaml
- name: Build and push Docker image
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: |
      azgoncinsightpilotacr.azurecr.io/insightpilot:sha-<short>
      azgoncinsightpilotacr.azurecr.io/insightpilot:latest
    cache-from: type=registry,ref=...:buildcache
    cache-to: type=registry,ref=...:buildcache,mode=max
```

### Deploy Job

1. Logs into Azure using Service Principal
2. Configures App Service environment variables
3. Deploys the `latest` Docker image
4. Performs health check with retry logic

### Smoke Tests

Validates the deployment by checking:
- `/docs` - API documentation accessible
- `/openapi.json` - OpenAPI schema available

---

## GitHub Secrets Required

| Secret | Description | Where to Get |
|--------|-------------|--------------|
| `AZURE_CREDENTIALS` | Service Principal JSON | `az ad sp create-for-rbac --sdk-auth` |
| `ACR_USERNAME` | Registry username | Azure Portal → ACR → Access Keys |
| `ACR_PASSWORD` | Registry password | Azure Portal → ACR → Access Keys |
| `DATABASE_URL` | PostgreSQL connection | Azure Portal → PostgreSQL → Connection strings |
| `OPENAI_API_KEY` | OpenAI API key | platform.openai.com |
| `SECRET_KEY` | App secret | `python -c "import secrets; print(secrets.token_urlsafe(32))"` |
| `APPINSIGHTS_INSTRUMENTATION_KEY` | Monitoring key | Azure Portal → App Insights |

---

## Workflow Badges

Add to README.md:

```markdown
[![CI](https://github.com/AnzeZg/InsightPilot/actions/workflows/ci.yml/badge.svg)](https://github.com/AnzeZg/InsightPilot/actions/workflows/ci.yml)
[![CD](https://github.com/AnzeZg/InsightPilot/actions/workflows/cd.yml/badge.svg)](https://github.com/AnzeZg/InsightPilot/actions/workflows/cd.yml)
```

---

## Common Operations

### Manually Trigger Deployment

1. Go to GitHub → Actions → "CD - Build & Deploy to Azure"
2. Click "Run workflow"
3. Select `main` branch
4. Click "Run workflow"

### View Pipeline Logs

1. GitHub → Actions
2. Select workflow run
3. Click on job name
4. Expand step for details

### Rollback to Previous Version

```bash
# Find previous image tag
az acr repository show-tags \
  --name azgoncinsightpilotacr \
  --repository insightpilot \
  --orderby time_desc

# Deploy specific version
az webapp config container set \
  --name azgonc-insightpilot \
  --resource-group BCSAI2025-DEVOPS-STUDENTS-A \
  --docker-custom-image-name azgoncinsightpilotacr.azurecr.io/insightpilot:<tag>

# Restart
az webapp restart --name azgonc-insightpilot --resource-group BCSAI2025-DEVOPS-STUDENTS-A
```

---

## Troubleshooting

### CI Fails on Coverage

```bash
# Run locally to debug
pytest --cov=app --cov-report=term-missing

# Check which lines are missing
open htmlcov/index.html
```

### CD Fails on ACR Login

- Verify `ACR_USERNAME` and `ACR_PASSWORD` secrets are correct
- Check ACR admin access is enabled in Azure Portal

### Health Check Fails

- Check App Service logs: `az webapp log tail --name azgonc-insightpilot`
- Verify environment variables are configured
- Test `/healthz` endpoint manually

### Smoke Tests Fail

- App may still be starting - wait 30-60 seconds
- Check container logs for startup errors
- Verify database migrations ran successfully

---

## Best Practices

1. **Never commit secrets** - Use GitHub Secrets
2. **Test locally first** - Run `pytest` and `docker build` before pushing
3. **Use PR workflow** - Don't push directly to main
4. **Monitor deployments** - Check App Insights after each deploy
5. **Keep dependencies updated** - Regular security patches

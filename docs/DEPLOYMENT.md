# Deployment Documentation

## Overview

InsightPilot is deployed to Azure using a GitHub Actions CI/CD pipeline. The application runs as a containerized FastAPI service with PostgreSQL database backend, using Azure's managed services for scalability, reliability, and ease of maintenance.

---

## Architecture

### Azure Resources

The deployment uses the following Azure services:

#### 1. **Azure Container Registry (ACR)**
- **Purpose**: Stores Docker images for the application
- **Resource**: `azgoncinsightpilotacr.azurecr.io`
- **Why ACR?**
  - Native integration with Azure App Service
  - Secure private registry for Docker images
  - Supports automated image scanning and security
  - Geo-replication for high availability

#### 2. **Azure App Service (Web App for Containers)**
- **Purpose**: Hosts the containerized FastAPI application
- **Resource**: `azgonc-insightpilot.azurewebsites.net`
- **Configuration**:
  - **SKU**: B1 (Basic tier, scalable to higher tiers)
  - **Runtime**: Docker container
  - **Platform**: Linux
- **Why App Service?**
  - Managed platform (PaaS) - no server management needed
  - Built-in load balancing and auto-scaling
  - Continuous deployment support
  - Built-in monitoring and diagnostics
  - Custom domain and SSL support

#### 3. **Azure Database for PostgreSQL (Flexible Server)**
- **Purpose**: Managed PostgreSQL database
- **Configuration**:
  - **SKU**: Burstable B1ms (1 vCore, 2GB RAM)
  - **Version**: PostgreSQL 16
  - **Storage**: 32GB with auto-grow enabled
- **Why PostgreSQL Flexible Server?**
  - Fully managed database service
  - Automatic backups and point-in-time restore
  - High availability options
  - Automatic patching and updates
  - Cost-effective for development and production

#### 4. **Resource Group**
- **Name**: `BCSAI2025-DEVOPS-STUDENTS-A`
- **Purpose**: Logical container for all Azure resources
- **Location**: West Europe

---

## CI/CD Pipeline

The deployment uses **two separate GitHub Actions workflows** for clear separation of concerns:

| Workflow | File | Trigger | Purpose |
|----------|------|---------|---------|
| **CI** | `.github/workflows/ci.yml` | Push to main, PRs | Code quality & tests |
| **CD** | `.github/workflows/cd.yml` | After CI succeeds on main | Build, deploy, validate |

---

### CI Workflow (`ci.yml`)

**Triggers**: Push to `main`, Pull Requests to `main`

**Jobs**:
1. **Lint & Test**
   - Ruff linter (code quality)
   - Ruff format (formatting check)
   - isort (import sorting)
   - pytest with coverage (minimum 70%)

**Artifacts**: Coverage reports, test results (uploaded for review)

---

### CD Workflow (`cd.yml`)

**Trigger**: Automatically runs after CI succeeds on `main` (via `workflow_run`)

**Jobs**:

| Job | Purpose | Key Steps |
|-----|---------|-----------|
| **Build** | Create Docker image | Build → Push to ACR (`latest` + SHA tag) |
| **Deploy** | Update Azure App Service | Configure settings → Deploy image → Health check |
| **Smoke Tests** | Validate deployment | Test `/docs` and `/openapi.json` endpoints |

**Manual Trigger**: `workflow_dispatch` available for hotfixes/rollbacks (bypasses CI).

---

### Workflow Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                        CI WORKFLOW                           │
├──────────────────────────────────────────────────────────────┤
│  PR to main ──┬──► Lint & Test ──► ✅ PR Ready to merge      │
│               │                                              │
│  Push to main ┘                                              │
└──────────────────────────────────────────────────────────────┘
                              │
                              │ (on success, main branch only)
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                        CD WORKFLOW                           │
├──────────────────────────────────────────────────────────────┤
│  Build ──► Deploy ──► Smoke Tests ──► ✅ Live in Production  │
└──────────────────────────────────────────────────────────────┘
```

---

## Environment Variables

### Required GitHub Secrets

Configure in GitHub: `Settings → Secrets and variables → Actions`

| Secret | Description |
|--------|-------------|
| `AZURE_CREDENTIALS` | Service Principal JSON (`az ad sp create-for-rbac --sdk-auth`) |
| `ACR_USERNAME` | ACR username (from Azure Portal → ACR → Access Keys) |
| `ACR_PASSWORD` | ACR password |
| `SECRET_KEY` | App secret (`openssl rand -hex 32`) |
| `DATABASE_URL` | PostgreSQL connection string |
| `OPENAI_API_KEY` | OpenAI API key |
| `APPINSIGHTS_INSTRUMENTATION_KEY` | Application Insights key (optional) |

### Application Environment Variables

These are configured in Azure App Service (`Configuration → Application settings`):

```bash
SECRET_KEY=<your-secret-key>
DATABASE_URL=postgresql://username:password@servername.postgres.database.azure.com/insightpilot?sslmode=require
OPENAI_API_KEY=sk-...
ENVIRONMENT=production
```

---

## Security Considerations

### 1. **Secrets Management**
- All sensitive data stored in GitHub Secrets (encrypted at rest)
- Environment variables injected at runtime
- No secrets committed to repository

### 2. **Container Registry**
- Private ACR (requires authentication)
- Admin access enabled for deployment
- Regular image scanning for vulnerabilities

### 3. **Database Security**
- SSL/TLS required for connections (`sslmode=require`)
- Firewall rules to restrict access
- Automatic backups enabled
- Encrypted at rest

### 4. **Application Security**
- HTTPS enforced on App Service
- CORS configured for specific origins
- Session management with secure cookies
- Input validation and sanitization

---

## Monitoring and Logging

### Application Insights
- Automatic monitoring enabled on App Service
- Tracks:
  - Request rates and response times
  - Failure rates and exceptions
  - Dependency calls (database, external APIs)
  - Custom events and metrics

### Log Streaming
Available through Azure Portal or Azure CLI:
```bash
az webapp log tail --name azgonc-insightpilot --resource-group BCSAI2025-DEVOPS-STUDENTS-A
```

### Health Endpoint
- URL: `https://azgonc-insightpilot.azurewebsites.net/healthz`
- Returns: `{"ok": true, "status": "healthy", ...}`
- Used for monitoring and load balancer health checks

---

## Rollback Strategy

### Manual Rollback
If issues occur after deployment:

1. **Revert to previous image**:
   ```bash
   az webapp config container set \
     --name azgonc-insightpilot \
     --resource-group BCSAI2025-DEVOPS-STUDENTS-A \
     --docker-custom-image-name azgoncinsightpilotacr.azurecr.io/insightpilot:<previous-commit-sha>
   ```

2. **Restart the app**:
   ```bash
   az webapp restart \
     --name azgonc-insightpilot \
     --resource-group BCSAI2025-DEVOPS-STUDENTS-A
   ```

### Automated Rollback
- GitHub Actions can be configured to rollback on health check failure
- Database migrations use Alembic for version control and rollback capability

---

## Cost Optimization

### Current Configuration (Estimated Monthly Costs)

| Resource | SKU | Estimated Cost |
|----------|-----|----------------|
| App Service | B1 Basic | ~€13/month |
| Container Registry | Basic | ~€5/month |
| PostgreSQL | B1ms Burstable | ~€15/month |
| **Total** | | **~€33/month** |

### Cost-Saving Recommendations
1. **Development**: Use B1ms for PostgreSQL (can be stopped when not in use)
2. **Production**: Upgrade to Standard tier for auto-scaling and slots
3. **Storage**: Enable auto-grow only if needed
4. **ACR**: Use Basic tier for small teams

---

## Scalability Considerations

### Horizontal Scaling
- App Service can scale out to multiple instances
- Configure in Azure Portal: `Scale out (App Service plan)`
- Supports auto-scaling based on metrics (CPU, memory, requests)

### Vertical Scaling
- Upgrade App Service plan to higher SKU (S1, P1V2, etc.)
- Upgrade PostgreSQL tier for more CPU/memory

### Database Optimization
- Connection pooling in application (SQLAlchemy)
- Read replicas for read-heavy workloads
- Query optimization and indexing

---

## Troubleshooting

### Common Issues

#### 1. **Container fails to start**
- **Check logs**: `az webapp log tail`
- **Verify environment variables** in App Service Configuration
- **Test locally**: `docker run -e SECRET_KEY=test -e DATABASE_URL=sqlite:///./test.db <image>`

#### 2. **Database connection fails**
- **Check connection string** format
- **Verify firewall rules** allow App Service IP
- **Ensure SSL mode** is set to `require`

#### 3. **Health check fails**
- **Check application logs** for errors
- **Verify `/healthz` endpoint** is accessible
- **Restart App Service** if needed

#### 4. **Pipeline fails**
- **Check GitHub Actions logs** for specific errors
- **Verify secrets** are configured correctly
- **Test locally** before pushing

---

## Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality before commits:

### Configured Hooks
- **Ruff**: Linting with auto-fix
- **Ruff-format**: Code formatting
- **isort**: Import organization
- **General**: Trailing whitespace, EOF fixes, YAML validation, large file detection

### Usage
```bash
pre-commit install          # Install hooks (one-time)
pre-commit run --all-files  # Run manually
```

Hooks run automatically on `git commit`.

---

## Manual Deployment Steps

If you need to deploy manually (without GitHub Actions):

### 1. Build and Push Docker Image
```bash
# Login to ACR
az acr login --name azgoncinsightpilotacr

# Build image
docker build -t azgoncinsightpilotacr.azurecr.io/insightpilot:latest .

# Push to ACR
docker push azgoncinsightpilotacr.azurecr.io/insightpilot:latest
```

### 2. Update App Service
```bash
# Configure container
az webapp config container set \
  --name azgonc-insightpilot \
  --resource-group BCSAI2025-DEVOPS-STUDENTS-A \
  --docker-custom-image-name azgoncinsightpilotacr.azurecr.io/insightpilot:latest

# Restart
az webapp restart \
  --name azgonc-insightpilot \
  --resource-group BCSAI2025-DEVOPS-STUDENTS-A
```

### 3. Run Database Migrations
```bash
# SSH into container (if needed)
az webapp ssh --name azgonc-insightpilot --resource-group BCSAI2025-DEVOPS-STUDENTS-A

# Run migrations
alembic upgrade head
```

---

## Continuous Improvement

### Future Enhancements

1. **Blue-Green Deployment**
   - Use deployment slots for zero-downtime deployments
   - Test in staging slot before swapping to production

2. **Database Backups**
   - Automated daily backups
   - Point-in-time restore capability
   - Backup retention policy

3. **Performance Monitoring**
   - Application Performance Monitoring (APM)
   - Custom metrics and alerts
   - Performance profiling

4. **Infrastructure as Code**
   - Terraform or Bicep templates
   - Version-controlled infrastructure
   - Reproducible environments

5. **Security Scanning**
   - Container image scanning (Trivy, Snyk)
   - Dependency vulnerability scanning
   - Secret scanning in repository

---

## Conclusion

The InsightPilot deployment architecture leverages Azure's managed services to provide a scalable, secure, and maintainable production environment. The GitHub Actions CI/CD pipeline ensures code quality through automated testing and enables rapid, reliable deployments with minimal manual intervention.

### Key Benefits
- ✅ **Automated CI/CD**: Push to main triggers full deployment
- ✅ **Infrastructure as Code**: Reproducible environment setup
- ✅ **Quality Gates**: Linting, testing, and coverage checks
- ✅ **Security**: Secrets management and encrypted connections
- ✅ **Monitoring**: Built-in logging and health checks
- ✅ **Scalability**: Can scale horizontally and vertically as needed
- ✅ **Cost-Effective**: Basic tier suitable for development/small production

### Resources
- **Production URL**: https://azgonc-insightpilot.azurewebsites.net
- **Health Check**: https://azgonc-insightpilot.azurewebsites.net/healthz
- **API Docs**: https://azgonc-insightpilot.azurewebsites.net/docs
- **GitHub Repository**: Contains full pipeline configuration

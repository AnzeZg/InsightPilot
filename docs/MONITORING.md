# InsightPilot Monitoring Guide

Complete guide to monitoring InsightPilot in development and production environments.

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Quick Start (5 Minutes)](#quick-start-5-minutes)
4. [Metrics Reference](#metrics-reference)
5. [Health Checks](#health-checks)
6. [Prometheus](#prometheus)
7. [Grafana](#grafana)
8. [Azure Application Insights (Production)](#azure-application-insights-production)
9. [Alert Rules](#alert-rules)
10. [Instrumenting Your Code](#instrumenting-your-code)
11. [Troubleshooting](#troubleshooting)
12. [Best Practices](#best-practices)

---

## Overview

InsightPilot uses a comprehensive monitoring stack with different tools for development and production:

**Local Development:**
- **Prometheus** - Metrics collection and storage
- **Grafana** - Visualization and dashboards
- **Custom metrics** - Business and application metrics

**Production (Azure):**
- **Prometheus metrics endpoint** - `/metrics` (industry-standard format)
- **Azure Application Insights** - Native Azure monitoring and APM
- **Health checks** - `/healthz` for Azure App Service

**Key Features:**
✅ Automatic HTTP metrics collection
✅ Custom business metrics (studies, interviews, AI)
✅ Pre-built Grafana dashboard with 8 panels
✅ 5 production-ready alert rules
✅ Real-time visualization
✅ 30-day metric retention
✅ Zero-configuration setup

---

## Architecture

### Local Development Architecture

```
┌─────────────────────────────────────────────────┐
│  Docker Compose (localhost)                     │
│                                                  │
│  ┌──────────────┐                               │
│  │ FastAPI App  │  Exposes /metrics             │
│  │   :8000      │                               │
│  └──────┬───────┘                               │
│         │                                        │
│         │ HTTP GET /metrics (every 15s)         │
│         │                                        │
│         ▼                                        │
│  ┌──────────────┐                               │
│  │  Prometheus  │  Scrapes, stores, queries     │
│  │    :9090     │  30-day retention             │
│  └──────┬───────┘                               │
│         │                                        │
│         │ PromQL queries                         │
│         │                                        │
│         ▼                                        │
│  ┌──────────────┐                               │
│  │   Grafana    │  Dashboards & visualization   │
│  │    :3001     │  admin/admin                  │
│  └──────────────┘                               │
└─────────────────────────────────────────────────┘
```

### Production Architecture (Azure)

```
┌────────────────────────────────────────────────────┐
│  Azure App Service                                 │
│                                                    │
│  ┌──────────────────────┐                         │
│  │   FastAPI App        │                         │
│  │   (Container)        │                         │
│  │                      │                         │
│  │   GET /metrics ◄─────┼── Prometheus format    │
│  │   GET /healthz       │    (external scraping) │
│  └──────────┬───────────┘                         │
│             │                                      │
│             │ Telemetry (logs, metrics, traces)   │
│             │                                      │
│             ▼                                      │
│  ┌──────────────────────┐                         │
│  │ Application Insights │                         │
│  │  (Azure Monitor)     │                         │
│  └──────────────────────┘                         │
└────────────────────────────────────────────────────┘
```

**Why Two Monitoring Approaches?**

- **Local (Prometheus + Grafana)**: Full-featured monitoring for development, testing, and demonstrations. Runs everything locally via Docker Compose.
- **Production (Azure App Insights)**: Native Azure monitoring that doesn't require deploying separate infrastructure. Azure App Service only deploys a single container (your app), not the full Docker Compose stack.

---

## Quick Start (5 Minutes)

### Step 1: Install Dependencies

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

# Install monitoring dependencies
pip install -e .[dev]
```

**Dependencies installed:**
- `prometheus-client==0.21.0` - Metrics exposition
- `prometheus-fastapi-instrumentator==7.0.0` - Automatic FastAPI instrumentation

### Step 2: Start Monitoring Stack

```bash
# Start all services (app + database + monitoring)
docker-compose up -d

# Verify all services are running
docker-compose ps

# Expected output:
# NAME                       STATUS
# insightpilot_app           Up
# insightpilot_db            Up (healthy)
# insightpilot_prometheus    Up
# insightpilot_grafana       Up
```

### Step 3: Verify Metrics Endpoint

```bash
# Check application metrics
curl http://localhost:8000/metrics

# You should see Prometheus-formatted metrics:
# http_requests_total{method="GET",endpoint="/healthz",status_code="200"} 5.0
# insightpilot_app_info{service="insightpilot",version="0.1.0"} 1.0
# http_request_duration_seconds_bucket{le="0.1",method="GET",endpoint="/healthz"} 5.0
```

### Step 4: Access Prometheus

1. Open http://localhost:9090
2. Go to **Status → Targets**
3. Verify `insightpilot-app` shows as **UP** ✅
4. Go to **Graph** tab and try a query:
```promql
   rate(http_requests_total[5m])
   ```

### Step 5: Access Grafana Dashboard

1. Open http://localhost:3001
2. Login: **admin** / **admin**
3. Skip password change (or set a new one)
4. Navigate to: **Dashboards → InsightPilot → Overview Dashboard**
5. You should see the pre-configured dashboard!

### Step 6: Generate Traffic

```bash
# Generate requests to populate metrics
for i in {1..20}; do
  curl http://localhost:8000/healthz
  sleep 0.5
done

# Or open in browser
open http://localhost:8000/
```

### Step 7: Watch Real-Time Updates

1. Go back to Grafana (http://localhost:3001)
2. Set auto-refresh to **10s** (top right)
3. Watch metrics update in real-time! 📊

---

## Metrics Reference

### HTTP Metrics (Automatic)

#### `http_requests_total`
- **Type**: Counter
- **Labels**: `method`, `endpoint`, `status_code`
- **Description**: Total HTTP requests

**Example:**
```promql
http_requests_total{method="GET", endpoint="/api/studies", status_code="200"}
```

#### `http_request_duration_seconds`
- **Type**: Histogram
- **Labels**: `method`, `endpoint`
- **Buckets**: 0.01s, 0.05s, 0.1s, 0.5s, 1s, 2s, 5s, 10s
- **Description**: Request latency

**Example queries:**
```promql
# P95 latency
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# Average response time
sum(rate(http_request_duration_seconds_sum[5m])) / sum(rate(http_request_duration_seconds_count[5m]))
```

#### `http_request_size_bytes` / `http_response_size_bytes`
- **Type**: Histogram
- **Labels**: `method`, `endpoint`
- **Description**: Request/response payload sizes

---

### Business Metrics (Custom)

#### Studies
```promql
studies_total{status="active"}     # Total studies created
studies_active                      # Current active studies
```

#### Interviews
```promql
interviews_total{status="completed"}   # Total interviews
interviews_active                      # Ongoing interviews
interview_duration_seconds             # Interview duration
interview_turns_total                  # Conversation turns
interview_messages_total{role="user"}  # Messages by role
```

#### Sessions
```promql
active_sessions                     # Currently logged-in users
auth_requests_total{type="login", status="success"}  # Login tracking
```

---

### AI/LLM Metrics (Custom)

```promql
ai_requests_total{service="openai", status="success"}  # AI API calls
ai_request_duration_seconds{service="openai"}          # AI latency
ai_tokens_total{type="prompt"}                         # Token usage
```

**Instrumentation example:**
```python
from app.metrics import ai_requests_total, ai_request_duration_seconds
import time

start = time.time()
try:
    response = await openai_client.chat.completions.create(...)
    ai_requests_total.labels(service="openai", status="success").inc()
except Exception:
    ai_requests_total.labels(service="openai", status="error").inc()
finally:
    duration = time.time() - start
    ai_request_duration_seconds.labels(service="openai").observe(duration)
```

---

### Database Metrics (Custom)

```promql
db_connections_active                              # Active connections
db_query_duration_seconds{operation="select"}      # Query latency
db_errors_total{error_type="connection"}           # Database errors
```

---

### Error Metrics (Custom)

```promql
errors_total{type="http", severity="error"}         # Categorized errors
exceptions_unhandled_total{exception_type="ValueError"}  # Exceptions
```

---

## Health Checks

### `/healthz` - Comprehensive Health Check

**Purpose**: Full application health status including database connectivity

**Response (healthy):**
```json
{
  "status": "healthy",
  "service": "insightpilot",
  "version": "0.1.0",
  "environment": "dev",
  "timestamp": "2025-11-24T10:30:00",
  "checks": {
    "database": {
      "status": "healthy",
      "latency_ms": 12.5,
      "error": null
    }
  }
}
```

**Response (unhealthy):**
- HTTP 503 Service Unavailable
- Includes error details

**Usage:**
```bash
# Local
curl http://localhost:8000/healthz

# Production
curl https://azgonc-insightpilot.azurewebsites.net/healthz
```

**Use case:** Azure App Service health checks, load balancer health probes

---

## Prometheus

### Access
- **URL**: http://localhost:9090
- **Configuration**: `monitoring/prometheus.yml`
- **Data retention**: 30 days
- **Scrape interval**: 15 seconds

### Common Queries

**Request rate (per second):**
```promql
rate(http_requests_total[5m])
```

**Error rate percentage:**
```promql
(
sum(rate(http_requests_total{status_code=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
) * 100
```

**P50, P95, P99 latency:**
```promql
histogram_quantile(0.50, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))
histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))
```

**Active interviews:**
```promql
interviews_active
```

**AI request success rate:**
```promql
(
  sum(rate(ai_requests_total{status="success"}[5m]))
/
sum(rate(ai_requests_total[5m]))
) * 100
```

**Database latency:**
```promql
histogram_quantile(0.95, sum(rate(db_query_duration_seconds_bucket[5m])) by (le))
```

### Viewing Targets

1. Go to **Status → Targets**
2. Check `insightpilot-app` is **UP** (green)
3. Shows last scrape time and duration

### Viewing Alerts

1. Go to **Alerts**
2. See configured alert rules and their status
3. **Pending** = condition met but not for full duration
4. **Firing** = alert is active

---

## Grafana

### Access
- **URL**: http://localhost:3001
- **Username**: `admin`
- **Password**: `admin` (change on first login)
- **Configuration**: `monitoring/grafana/`

### Pre-Built Dashboard: "InsightPilot Overview"

**Location**: Dashboards → InsightPilot → Overview Dashboard

**Panels:**

1. **HTTP Request Rate** - Requests/second across all endpoints
2. **Error Rate (5xx)** - Gauge showing percentage of server errors
   - Green (<5%): Healthy ✅
   - Red (>5%): Problem! ⚠️
3. **Response Time Percentiles** - P50, P95, P99 latency
4. **Interviews per Second** - Interview activity by status
5. **Active Studies** - Current research studies (stat panel)
6. **Active Interviews** - Ongoing conversations (stat panel)
7. **Active Sessions** - Logged-in users (stat panel)
8. **AI P95 Latency** - OpenAI API response time (stat panel)

### Dashboard Tips

**Auto-refresh:**
- Click time range (top right)
- Set refresh: 5s, 10s, 30s, or 1m

**Time range:**
- Last 5 minutes (default)
- Last 15 minutes
- Last 1 hour
- Custom range

**Panel controls:**
- Hover over panel → three dots (⋮) → View
- Edit panel to customize queries
- Click legend items to toggle series

### Creating Custom Dashboards

1. Click **+ → Dashboard**
2. **Add panel**
3. Select **Prometheus** datasource
4. Write PromQL query
5. Choose visualization type
6. Configure display options
7. **Save dashboard**

**Export dashboard:**
1. Dashboard settings (gear icon)
2. **JSON Model** → Copy
3. Save to `monitoring/grafana/dashboards/your-dashboard.json`

---

## Azure Application Insights (Production)

Azure Application Insights provides native Azure monitoring without deploying separate infrastructure.

### Features

✅ **Application Performance Monitoring (APM)**
✅ **Automatic request tracking**
✅ **Dependency tracking** (database, external APIs)
✅ **Exception tracking**
✅ **Log aggregation**
✅ **Built-in dashboards**
✅ **Custom alerts**
✅ **Live metrics stream**

### Access

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to your Application Insights resource: `insightpilot-appinsights`
3. Explore:
   - **Application Map** - Visual dependency graph
   - **Performance** - Request latency and throughput
   - **Failures** - Exceptions and failed requests
   - **Metrics** - Custom and automatic metrics
   - **Logs** - Query application logs with KQL

### Configuration

Application Insights is configured via environment variable:

```bash
# In Azure App Service Configuration
APPINSIGHTS_INSTRUMENTATION_KEY=your-instrumentation-key-here
```

**Where to find instrumentation key:**
```bash
az monitor app-insights component show \
  --app insightpilot-appinsights \
  --resource-group BCSAI2025-DEVOPS-STUDENTS-A \
  --query instrumentationKey -o tsv
```

### Viewing Metrics in Azure Portal

**Application Map:**
- Visual representation of your app and dependencies
- Shows request rates and failure rates
- Click components to see details

**Performance:**
- Request duration statistics
- Slowest requests
- Dependency call latency
- Drill into specific operations

**Failures:**
- Exception count and types
- Failed request analysis
- Stack traces
- Affected users

**Live Metrics:**
- Real-time request rate
- Real-time failure rate
- Live server performance
- Streaming logs

### Creating Alerts in Azure

1. Go to **Alerts** in Application Insights
2. Click **+ New alert rule**
3. Define condition (e.g., "Failed requests > 10")
4. Set action group (email, SMS, webhook)
5. Configure alert details
6. **Create**

**Example alert conditions:**
- Response time > 2 seconds
- Failed requests > 5% of total
- Exception count > 10 in 5 minutes
- Availability < 99%

### Query Application Insights Logs

Use **Kusto Query Language (KQL)** in the Logs section:

**Request rate:**
```kql
requests
| summarize count() by bin(timestamp, 5m)
| render timechart
```

**Error rate:**
```kql
requests
| where success == false
| summarize failureRate = (count() * 100.0) / toint(countif(true))
```

**Slowest endpoints:**
```kql
requests
| summarize avg(duration) by name
| top 10 by avg_duration desc
```

**Exception breakdown:**
```kql
exceptions
| summarize count() by type
| render piechart
```

---

## Alert Rules

### Configuration

**File**: `monitoring/alerts.yml`

**How alerts work:**
1. Prometheus evaluates rules every 15 seconds
2. If condition is `true` for the `for` duration, alert fires
3. Alert annotations can include values and context

### Pre-configured Alerts

#### 1. High Error Rate
**Condition**: >5% of requests return 5xx errors for 2+ minutes
**Severity**: Warning ⚠️

```yaml
- alert: HighErrorRate
  expr: |
(
  sum(rate(http_requests_total{status_code=~"5.."}[5m]))
  /
  sum(rate(http_requests_total[5m]))
    ) > 0.05
  for: 2m
  labels:
    severity: warning
  annotations:
    summary: "High HTTP error rate (>5%)"
    description: "{{ $value | humanizePercentage }} of requests are failing"
```

#### 2. Slow Response Time
**Condition**: P95 latency >2s for 5+ minutes
**Severity**: Warning ⚠️

```yaml
- alert: SlowResponseTime
  expr: |
histogram_quantile(0.95,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
    ) > 2.0
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "High response time (P95 >2s)"
    description: "95th percentile response time is {{ $value }}s"
```

#### 3. Database Connection Errors
**Condition**: >10 database errors in 5 minutes
**Severity**: Critical 🔥

```yaml
- alert: DatabaseConnectionError
  expr: sum(increase(db_errors_total[5m])) > 10
  for: 1m
  labels:
    severity: critical
  annotations:
    summary: "Database connection errors detected"
    description: "{{ $value }} database errors in the last 5 minutes"
```

#### 4. High AI Request Failure Rate
**Condition**: >10% of AI requests fail for 3+ minutes
**Severity**: Warning ⚠️

```yaml
- alert: HighAIRequestFailureRate
  expr: |
    (
      sum(rate(ai_requests_total{status="error"}[5m]))
  /
  sum(rate(ai_requests_total[5m]))
    ) > 0.1
  for: 3m
  labels:
    severity: warning
  annotations:
    summary: "High AI request failure rate (>10%)"
    description: "{{ $value | humanizePercentage }} of AI requests are failing"
```

#### 5. Service Down
**Condition**: App not responding for 1+ minute
**Severity**: Critical 🔥

```yaml
- alert: ServiceDown
  expr: up{job="insightpilot-app"} == 0
  for: 1m
  labels:
    severity: critical
  annotations:
    summary: "InsightPilot service is down"
    description: "The application has been unreachable for over 1 minute"
```

### Testing Alerts

**Simulate high error rate:**
```bash
# Generate 5xx errors (if you have an endpoint that can fail)
for i in {1..100}; do curl http://localhost:8000/api/fail || true; done
```

**Check alert status:**
1. Go to http://localhost:9090/alerts
2. Look for **Pending** or **Firing** status
3. **Pending** = condition met, waiting for `for` duration
4. **Firing** = alert is active

---

## Instrumenting Your Code

### Adding Business Metrics

**Location**: Import from `app/metrics.py`

#### Example: Track Interview Lifecycle

```python
from app.metrics import interviews_active, interviews_total, interview_duration_seconds
import time

# When interview starts
async def start_interview(interview_id: int):
    interviews_active.inc()  # Increment active count
    # ... create interview in database ...

# When interview completes
async def complete_interview(interview_id: int, started_at: datetime):
    interviews_total.labels(status="completed").inc()  # Increment total
    interviews_active.dec()  # Decrement active count

    # Record duration
    duration = (datetime.now() - started_at).total_seconds()
    interview_duration_seconds.observe(duration)
```

#### Example: Track Study Creation

```python
from app.metrics import studies_total, studies_active

async def create_study(study_data: dict):
    # ... create study in database ...

    studies_total.labels(status="active").inc()
    studies_active.inc()
```

#### Example: Track AI Requests

```python
from app.metrics import ai_requests_total, ai_request_duration_seconds, ai_tokens_total
import time

async def generate_response(prompt: str):
    start_time = time.time()

    try:
        response = await openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        # Record success
        ai_requests_total.labels(service="openai", status="success").inc()

        # Record token usage
        ai_tokens_total.labels(type="prompt").inc(response.usage.prompt_tokens)
        ai_tokens_total.labels(type="completion").inc(response.usage.completion_tokens)

        return response

    except Exception as e:
        # Record failure
        ai_requests_total.labels(service="openai", status="error").inc()
        raise

    finally:
        # Always record duration
        duration = time.time() - start_time
        ai_request_duration_seconds.labels(service="openai").observe(duration)
```

#### Example: Track Database Operations

```python
from app.metrics import db_query_duration_seconds, db_errors_total
import time

async def execute_query(query: str, operation: str):
start_time = time.time()

try:
        result = await db.execute(query)
        return result

except Exception as e:
        db_errors_total.labels(error_type=type(e).__name__).inc()
        raise

finally:
    duration = time.time() - start_time
        db_query_duration_seconds.labels(operation=operation).observe(duration)
```

### Creating New Metrics

Edit `app/metrics.py`:

```python
from prometheus_client import Counter, Gauge, Histogram

# Counter (always increases)
custom_events_total = Counter(
    'custom_events_total',
    'Total custom events',
    ['event_type', 'status']
)

# Gauge (can go up or down)
current_users = Gauge(
    'current_users',
    'Currently active users'
)

# Histogram (for distributions)
processing_duration_seconds = Histogram(
    'processing_duration_seconds',
    'Processing duration in seconds',
    ['operation'],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
)

# Usage
custom_events_total.labels(event_type="signup", status="success").inc()
current_users.set(42)
processing_duration_seconds.labels(operation="export").observe(1.5)
```

---

## Troubleshooting

### Issue: Metrics Endpoint Returns 404

**Symptoms:**
```bash
curl http://localhost:8000/metrics
# {"detail":"Not Found"}
```

**Solutions:**

1. **Check app is running:**
```bash
docker-compose ps app
   # Should show "Up"
   ```

2. **Check logs for errors:**
   ```bash
   docker-compose logs app
   ```

3. **Verify instrumentation is enabled:**
   - Check `app/main.py` for `instrumentator.instrument(app).expose(app)`
   - Ensure no environment variable is disabling metrics

4. **Restart app:**
   ```bash
   docker-compose restart app
   ```

---

### Issue: Prometheus Target is DOWN

**Symptoms:**
- Prometheus shows `insightpilot-app` as **DOWN** (red)

**Solutions:**

1. **Check if app is reachable:**
   ```bash
   # From host machine
curl http://localhost:8000/metrics

   # From Prometheus container
   docker-compose exec prometheus wget -O- http://app:8000/metrics
   ```

2. **Check Prometheus logs:**
   ```bash
docker-compose logs prometheus
   # Look for scrape errors
   ```

3. **Verify network connectivity:**
   ```bash
docker-compose exec prometheus ping app
```

4. **Check Prometheus configuration:**
   ```bash
   cat monitoring/prometheus.yml
   # Verify target is 'app:8000'
   ```

---

### Issue: Grafana Shows "No Data"

**Symptoms:**
- Dashboard panels show "No data"

**Solutions:**

1. **Check time range** (top right corner):
   - Set to "Last 15 minutes" or "Last 1 hour"

2. **Generate traffic:**
```bash
   for i in {1..10}; do curl http://localhost:8000/healthz; done
   ```

3. **Verify Prometheus has data:**
   - Go to http://localhost:9090
   - Run query: `http_requests_total`
   - Should show results

4. **Test datasource connection:**
   - Grafana → Configuration → Data Sources → Prometheus
   - Click **Test** button
   - Should show "Data source is working"

5. **Check Prometheus target is UP:**
   - http://localhost:9090/targets
   - `insightpilot-app` should be green

6. **Wait for first scrape:**
   - Takes up to 15 seconds after app starts
   - Refresh Grafana after waiting

---

### Issue: Grafana Can't Connect to Prometheus

**Symptoms:**
- Datasource test fails
- "Bad Gateway" or "Connection refused"

**Solutions:**

1. **Check Prometheus is running:**
   ```bash
   docker-compose ps prometheus
curl http://localhost:9090/-/ready
   ```

2. **Check Grafana logs:**
   ```bash
docker-compose logs grafana
   ```

3. **Verify datasource URL:**
   - Should be `http://prometheus:9090` (Docker internal network)
   - NOT `http://localhost:9090`

4. **Restart Grafana:**
   ```bash
   docker-compose restart grafana
   ```

5. **Check Docker network:**
   ```bash
   docker network inspect insightpilot_default
   # Both grafana and prometheus should be listed
   ```

---

### Issue: Services Won't Start

**Symptoms:**
- `docker-compose up` fails
- Port conflicts

**Solutions:**

1. **Check for port conflicts:**
   ```bash
   # Check which ports are in use
   lsof -i :8000   # App
   lsof -i :9090   # Prometheus
   lsof -i :3001   # Grafana
   lsof -i :5432   # PostgreSQL
   ```

2. **Kill conflicting processes:**
   ```bash
   # Find process ID
   lsof -i :9090
   # Kill it
   kill -9 <PID>
   ```

3. **Stop all containers and restart:**
   ```bash
   docker-compose down
   docker-compose up -d
   ```

4. **Check Docker daemon is running:**
   ```bash
   docker ps
   # Should not error
   ```

5. **View detailed logs:**
   ```bash
   docker-compose logs
   # or specific service:
   docker-compose logs prometheus
   ```

---

### Issue: High Prometheus Memory Usage

**Symptoms:**
- Prometheus container using >2GB RAM
- System slowdown

**Solutions:**

1. **Reduce retention period:**
   Edit `docker-compose.yml`:
```yaml
   prometheus:
command:
  - '--storage.tsdb.retention.time=7d'  # Reduce from 30d
```

2. **Limit scrape frequency:**
   Edit `monitoring/prometheus.yml`:
   ```yaml
   global:
     scrape_interval: 30s  # Increase from 15s
   ```

3. **Remove high-cardinality metrics:**
   - Avoid labels with many unique values (user IDs, timestamps, etc.)

4. **Restart with new settings:**
   ```bash
   docker-compose down
   docker-compose up -d
   ```

---

### Issue: Azure Application Insights Not Receiving Data

**Symptoms:**
- No data in Azure Portal
- Application Map is empty

**Solutions:**

1. **Verify instrumentation key is set:**
   ```bash
   # Check Azure App Service configuration
   az webapp config appsettings list \
     --name azgonc-insightpilot \
     --resource-group BCSAI2025-DEVOPS-STUDENTS-A \
     --query "[?name=='APPINSIGHTS_INSTRUMENTATION_KEY']"
   ```

2. **Check app logs for errors:**
   - Go to Azure Portal → App Service → Log stream
   - Look for Application Insights connection errors

3. **Test instrumentation key locally:**
   ```bash
   # Set in .env
   APPINSIGHTS_INSTRUMENTATION_KEY=your-key-here

   # Restart app
   docker-compose restart app

   # Check logs for Application Insights connection
   docker-compose logs app | grep -i "insights"
   ```

4. **Wait for data propagation:**
   - Application Insights can take 2-5 minutes to show data
   - Refresh Azure Portal after waiting

---

## Best Practices

### Metric Naming Conventions

✅ **Use descriptive names:**
- Good: `interviews_total`, `ai_request_duration_seconds`
- Bad: `int_cnt`, `ai_time`

✅ **Follow Prometheus conventions:**
- Counters: `_total` suffix (e.g., `requests_total`)
- Durations: `_seconds` suffix (e.g., `duration_seconds`)
- Sizes: `_bytes` suffix (e.g., `response_size_bytes`)

✅ **Use consistent label names:**
- `status` not `result`, `state`, or `outcome`
- `endpoint` not `path`, `route`, or `url`
- `method` not `verb` or `http_method`

❌ **Avoid:**
- CamelCase (use `snake_case`)
- Abbreviations that aren't obvious
- Changing naming style mid-project

---

### Label Cardinality

✅ **Keep label values bounded:**
- Status codes (200, 404, 500) - Low cardinality ✅
- HTTP methods (GET, POST, PUT) - Low cardinality ✅
- Endpoint groups (/api/studies, /api/interviews) - Medium cardinality ✅

❌ **Avoid high-cardinality labels:**
- User IDs - Every user is a unique value ❌
- Timestamps - Every second is unique ❌
- Request IDs - Every request is unique ❌
- Full URLs with query params - Infinite combinations ❌

**Why?** Each unique combination of labels creates a new time series. Too many series can overwhelm Prometheus.

**Rule of thumb:** Keep total unique label combinations under 100,000 per metric.

---

### Alert Design

✅ **Set appropriate thresholds:**
- Base on historical data
- Allow for normal variance
- Consider business impact

✅ **Use `for` duration:**
- Prevents flapping (alerts firing/resolving rapidly)
- Allows temporary spikes
- Example: `for: 5m` means condition must be true for 5 minutes

✅ **Write actionable annotations:**
```yaml
annotations:
  summary: "High error rate on {{ $labels.endpoint }}"
  description: "{{ $value | humanizePercentage }} of requests failing. Check logs: kubectl logs -l app=insightpilot"
  runbook: "https://wiki.company.com/runbooks/high-error-rate"
```

✅ **Use severity levels:**
- **Critical**: Immediate action required, affects users
- **Warning**: Needs attention, might affect users soon
- **Info**: FYI, no action needed

❌ **Avoid:**
- Alerting on metrics that don't require action
- Too many alerts (alert fatigue)
- Alerts without clear remediation steps

---

### Dashboard Design

✅ **One clear purpose per dashboard:**
- "Overview" - High-level health
- "Performance" - Detailed latency/throughput
- "Business" - KPIs and user activity

✅ **Use appropriate visualizations:**
- **Time series graph** - Trends over time (request rate, latency)
- **Gauge** - Current value vs threshold (error rate, CPU%)
- **Stat panel** - Single current value (active users, total requests)
- **Table** - Multiple related values (top endpoints, error breakdown)

✅ **Include context:**
- Show time range prominently
- Add environment label (dev/staging/prod)
- Include units (%, ms, req/s)

✅ **Keep it actionable:**
- Focus on metrics you'll act on
- Remove "nice to have" but unused panels
- Group related panels together

---

### Performance Optimization

✅ **Use recording rules for expensive queries:**
```yaml
# In prometheus.yml
rules:
  - record: job:http_requests:rate5m
    expr: sum(rate(http_requests_total[5m])) by (job)
```

✅ **Limit dashboard query complexity:**
- Use recording rules for complex aggregations
- Cache dashboard variables
- Use shorter time ranges when possible

✅ **Monitor Prometheus resource usage:**
```promql
prometheus_tsdb_head_series          # Number of series
prometheus_tsdb_head_samples_appended_total  # Sample rate
rate(prometheus_tsdb_compaction_duration_seconds_sum[5m])  # Compaction time
```

---

### Security Considerations

✅ **Restrict metrics endpoint access:**
- Don't expose `/metrics` publicly without authentication
- Use firewall rules or API gateway
- Consider IP whitelisting

✅ **Rotate credentials:**
- Change Grafana admin password on first login
- Don't commit passwords to Git
- Use Azure Key Vault for production secrets

✅ **Use HTTPS in production:**
- Enable HTTPS for Grafana
- Use TLS for Prometheus if exposed externally
- Azure Application Insights uses HTTPS by default ✅

✅ **Sanitize metric labels:**
- Don't include PII (names, emails) in labels
- Don't include secrets in labels
- Validate user input before using in labels

---

## Summary

### What You Have Now

✅ **Full monitoring stack** for local development
✅ **Prometheus** for metrics collection (30-day retention)
✅ **Grafana** with pre-built dashboard (8 panels)
✅ **Azure Application Insights** for production monitoring
✅ **5 alert rules** for proactive monitoring
✅ **3 health check endpoints** for orchestration
✅ **Comprehensive metrics** (HTTP, business, AI, database, errors)
✅ **Zero-configuration setup** via Docker Compose
✅ **Production-ready** metrics endpoint

### Quick Reference

**Services:**
- Application: http://localhost:8000
- Metrics: http://localhost:8000/metrics
- Health: http://localhost:8000/healthz
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3001 (admin/admin)
- Azure Portal: https://portal.azure.com

**Key Files:**
- Metrics definitions: `app/metrics.py`
- Middleware: `app/middleware.py`
- Prometheus config: `monitoring/prometheus.yml`
- Alert rules: `monitoring/alerts.yml`
- Grafana dashboard: `monitoring/grafana/dashboards/insightpilot-overview.json`

**Commands:**
```bash
# Start everything
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f app

# Restart service
docker-compose restart app

# Stop everything
docker-compose down
```

---

## Additional Resources

### Documentation
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [PromQL Guide](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

### Tutorials
- [Prometheus Query Examples](https://prometheus.io/docs/prometheus/latest/querying/examples/)
- [PromQL Cheat Sheet](https://promlabs.com/promql-cheat-sheet/)
- [Grafana Dashboards](https://grafana.com/grafana/dashboards/)

### Community
- [Prometheus Community](https://prometheus.io/community/)
- [Grafana Community](https://community.grafana.com/)

---

**You're now ready to monitor InsightPilot like a pro! 🎉📊**

# Monitoring Configuration

This directory contains Prometheus and Grafana configuration files for InsightPilot monitoring.

## Directory Structure

```
monitoring/
├── prometheus.yml          # Prometheus scrape configuration
├── alerts.yml             # Prometheus alerting rules
├── grafana/
│   ├── datasources/
│   │   └── prometheus.yml # Grafana Prometheus datasource config
│   └── dashboards/
│       ├── dashboards.yml # Dashboard provisioning config
│       └── insightpilot-overview.json  # Main dashboard
└── README.md              # This file
```

## Quick Start

### 1. Start Monitoring Stack

```bash
# From project root
docker-compose up -d prometheus grafana

# Verify services are running
docker-compose ps
```

### 2. Access Services

- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3001 (admin/admin)
- **Application Metrics**: http://localhost:8000/metrics

### 3. View Dashboard

1. Open Grafana at http://localhost:3001
2. Login with default credentials (admin/admin)
3. Navigate to Dashboards → InsightPilot → Overview Dashboard

## Configuration Files

### prometheus.yml
Main Prometheus configuration defining:
- Scrape intervals (15s)
- Target applications to monitor
- Data retention settings

### alerts.yml
Alert rules for:
- High error rates (>5%)
- Slow response times (P95 >2s)
- Database connection errors
- AI request failures
- Service downtime

### grafana/datasources/prometheus.yml
Automatic Prometheus datasource configuration for Grafana.

### grafana/dashboards/
- `dashboards.yml`: Dashboard provisioning configuration
- `insightpilot-overview.json`: Pre-built overview dashboard with:
  - HTTP request rate
  - Error rate gauge
  - Response time percentiles
  - Active studies/interviews/sessions
  - AI request latency

## Customization

### Adding New Alert Rules

Edit `alerts.yml`:

```yaml
- alert: YourAlertName
  expr: your_promql_query > threshold
  for: 2m
  labels:
    severity: warning
  annotations:
    summary: "Alert description"
    description: "Detailed description with {{ $value }}"
```

### Modifying Scrape Configuration

Edit `prometheus.yml`:

```yaml
scrape_configs:
  - job_name: 'your-service'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['your-service:port']
```

### Creating New Dashboards

1. Create dashboard in Grafana UI
2. Export as JSON
3. Save to `grafana/dashboards/`
4. Restart Grafana to load: `docker-compose restart grafana`

## Troubleshooting

### Prometheus Not Scraping

```bash
# Check Prometheus logs
docker-compose logs prometheus

# Verify app metrics endpoint
curl http://localhost:8000/metrics

# Check Prometheus targets
# Open http://localhost:9090/targets
```

### Grafana Shows No Data

```bash
# Test Prometheus datasource
# Grafana → Configuration → Data Sources → Prometheus → Test

# Verify Prometheus has data
# Open http://localhost:9090 and run: http_requests_total

# Check time range in Grafana (top right corner)
```

### Update Retention Period

Edit `docker-compose.yml`:

```yaml
prometheus:
  command:
    - '--storage.tsdb.retention.time=7d'  # Change from 30d
```

## For More Information

See the main [MONITORING.md](../MONITORING.md) documentation in the project root.

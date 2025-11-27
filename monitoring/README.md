# Monitoring Configuration Files

This directory contains Prometheus and Grafana configuration files for InsightPilot.

📖 **For complete monitoring documentation, see [docs/MONITORING.md](../docs/MONITORING.md)**

---

## Directory Structure

```
monitoring/
├── prometheus.yml          # Prometheus scrape configuration
├── alerts.yml             # Alert rules
├── grafana/
│   ├── datasources/
│   │   └── prometheus.yml # Auto-provisioned Prometheus datasource
│   └── dashboards/
│       ├── dashboards.yml # Dashboard provisioning config
│       └── insightpilot-overview.json  # Pre-built dashboard
└── README.md              # This file
```

---

## Configuration Files

### `prometheus.yml`
Main Prometheus configuration:
- **Scrape interval**: 15 seconds
- **Evaluation interval**: 15 seconds
- **Targets**: `app:8000/metrics`
- **Data retention**: 30 days (configured in docker-compose.yml)

### `alerts.yml`
Pre-configured alert rules:
1. **HighErrorRate** - >5% 5xx errors for 2+ minutes
2. **SlowResponseTime** - P95 >2s for 5+ minutes
3. **DatabaseConnectionError** - >10 DB errors in 5 minutes
4. **HighAIRequestFailureRate** - >10% AI failures for 3+ minutes
5. **ServiceDown** - App not responding for 1+ minute

### `grafana/datasources/prometheus.yml`
Grafana datasource configuration:
- **URL**: `http://prometheus:9090` (Docker internal)
- **Access**: Proxy (Grafana queries Prometheus)
- **Auto-provisioned**: No manual setup needed

### `grafana/dashboards/`
Dashboard configuration:
- **dashboards.yml**: Tells Grafana where to find dashboards
- **insightpilot-overview.json**: Pre-built dashboard with 8 panels
  - HTTP Request Rate
  - Error Rate (5xx)
  - Response Time Percentiles
  - Interviews per Second
  - Active Studies/Interviews/Sessions
  - AI Request P95 Latency

---

## Quick Reference

### Start Monitoring Stack

```bash
# From project root
docker-compose up -d

# Check services are running
docker-compose ps
```

### Access Services

- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3001 (admin/admin)
- **Application Metrics**: http://localhost:8000/metrics

### Verify Setup

```bash
# Check metrics endpoint
curl http://localhost:8000/metrics

# Check Prometheus targets (should be UP)
open http://localhost:9090/targets

# View Grafana dashboard
open http://localhost:3001
# Navigate to: Dashboards → InsightPilot → Overview Dashboard
```

---

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
    summary: "Brief description"
    description: "Detailed description with {{ $value }}"
```

Then restart Prometheus:
```bash
docker-compose restart prometheus
```

### Modifying Scrape Targets

Edit `prometheus.yml`:

```yaml
scrape_configs:
  - job_name: 'your-new-service'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['service-name:port']
```

Then restart Prometheus:
```bash
docker-compose restart prometheus
```

### Adding Custom Dashboards

1. Create dashboard in Grafana UI
2. Dashboard settings (⚙️) → JSON Model
3. Copy JSON
4. Save to `grafana/dashboards/your-dashboard.json`
5. Add provisioning entry in `grafana/dashboards/dashboards.yml`:
   ```yaml
   providers:
     - name: 'InsightPilot'
       options:
         path: /etc/grafana/provisioning/dashboards
         foldersFromFilesStructure: true
   ```
6. Restart Grafana: `docker-compose restart grafana`

---

## Troubleshooting

### Prometheus Not Scraping

```bash
# Check app is accessible
curl http://localhost:8000/metrics

# Check Prometheus logs
docker-compose logs prometheus

# Check targets status
open http://localhost:9090/targets
```

### Grafana Shows No Data

```bash
# Test Prometheus connection from Grafana
# Grafana → Configuration → Data Sources → Prometheus → Test

# Verify Prometheus has data
open http://localhost:9090
# Run query: http_requests_total

# Check time range in Grafana (top right)
# Generate traffic to create metrics
for i in {1..10}; do curl http://localhost:8000/healthz; done
```

### Alerts Not Firing

```bash
# Check alert rules loaded
open http://localhost:9090/alerts

# Check alerts.yml syntax
docker-compose exec prometheus promtool check rules /etc/prometheus/alerts.yml

# View Prometheus logs
docker-compose logs prometheus | grep -i alert
```

---

## For More Information

📖 **Complete documentation**: [docs/MONITORING.md](../docs/MONITORING.md)

**Covers:**
- Architecture overview
- Metrics reference
- Health checks
- Prometheus and Grafana usage
- Azure Application Insights
- Instrumenting your code
- Best practices
- Troubleshooting

**External resources:**
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [PromQL Guide](https://prometheus.io/docs/prometheus/latest/querying/basics/)

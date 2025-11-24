"""Prometheus metrics for application monitoring."""

from prometheus_client import Counter, Gauge, Histogram, Info

# =============================================================================
# Application Info
# =============================================================================

app_info = Info("insightpilot_app", "InsightPilot application information")
app_info.info(
    {
        "version": "0.1.0",
        "service": "insightpilot",
        "description": "AI-driven market research interview platform",
    }
)

# =============================================================================
# HTTP Request Metrics
# =============================================================================

http_requests_total = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status_code"],
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"],
    buckets=(0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0),
)

http_request_size_bytes = Histogram(
    "http_request_size_bytes",
    "HTTP request size in bytes",
    ["method", "endpoint"],
    buckets=(100, 1000, 10000, 100000, 1000000, 10000000),
)

http_response_size_bytes = Histogram(
    "http_response_size_bytes",
    "HTTP response size in bytes",
    ["method", "endpoint"],
    buckets=(100, 1000, 10000, 100000, 1000000, 10000000),
)

# =============================================================================
# Business Metrics - Studies
# =============================================================================

studies_total = Counter(
    "studies_total",
    "Total number of studies created",
    ["status"],
)

studies_active = Gauge(
    "studies_active",
    "Number of currently active studies",
)

# =============================================================================
# Business Metrics - Interviews
# =============================================================================

interviews_total = Counter(
    "interviews_total",
    "Total number of interviews conducted",
    ["status"],
)

interviews_active = Gauge(
    "interviews_active",
    "Number of currently active interviews",
)

interview_duration_seconds = Histogram(
    "interview_duration_seconds",
    "Interview duration in seconds",
    buckets=(60, 120, 300, 600, 900, 1800, 3600),
)

interview_turns_total = Counter(
    "interview_turns_total",
    "Total number of interview conversation turns",
)

interview_messages_total = Counter(
    "interview_messages_total",
    "Total number of interview messages",
    ["role"],  # user, assistant
)

# =============================================================================
# Business Metrics - AI/LLM
# =============================================================================

ai_requests_total = Counter(
    "ai_requests_total",
    "Total number of AI/LLM requests",
    ["service", "status"],  # service: openai, status: success, error
)

ai_request_duration_seconds = Histogram(
    "ai_request_duration_seconds",
    "AI/LLM request duration in seconds",
    ["service"],
    buckets=(0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 15.0, 30.0),
)

ai_tokens_total = Counter(
    "ai_tokens_total",
    "Total number of AI tokens used",
    ["type"],  # prompt, completion
)

# =============================================================================
# Database Metrics
# =============================================================================

db_connections_active = Gauge(
    "db_connections_active",
    "Number of active database connections",
)

db_query_duration_seconds = Histogram(
    "db_query_duration_seconds",
    "Database query duration in seconds",
    ["operation"],  # select, insert, update, delete
    buckets=(0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0),
)

db_errors_total = Counter(
    "db_errors_total",
    "Total number of database errors",
    ["error_type"],
)

# =============================================================================
# Authentication Metrics
# =============================================================================

auth_requests_total = Counter(
    "auth_requests_total",
    "Total number of authentication requests",
    ["type", "status"],  # type: login, register, status: success, failure
)

active_sessions = Gauge(
    "active_sessions",
    "Number of active user sessions",
)

# =============================================================================
# Insight Generation Metrics
# =============================================================================

insights_generated_total = Counter(
    "insights_generated_total",
    "Total number of insights generated",
    ["status"],  # success, fallback, error
)

insights_generation_duration_seconds = Histogram(
    "insights_generation_duration_seconds",
    "Insight generation duration in seconds",
    buckets=(1.0, 2.0, 5.0, 10.0, 15.0, 30.0, 60.0),
)

# =============================================================================
# Error Metrics
# =============================================================================

errors_total = Counter(
    "errors_total",
    "Total number of errors",
    ["type", "severity"],  # type: http, db, ai, etc., severity: warning, error, critical
)

exceptions_unhandled_total = Counter(
    "exceptions_unhandled_total",
    "Total number of unhandled exceptions",
    ["exception_type"],
)

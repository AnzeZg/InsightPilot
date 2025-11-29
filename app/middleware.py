"""Custom middleware for request tracking and logging."""

import logging
import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.metrics import (
    http_request_duration_seconds,
    http_request_size_bytes,
    http_requests_total,
    http_response_size_bytes,
)

logger = logging.getLogger(__name__)


class RequestIDMiddleware(BaseHTTPMiddleware):
    """Middleware to add unique request ID to each request."""

    async def dispatch(self, request: Request, call_next) -> Response:
        # Generate or extract request ID
        request_id = request.headers.get("x-request-id") or str(uuid.uuid4())

        # Store request ID in request state for access in route handlers
        request.state.request_id = request_id

        # Track request timing
        start_time = time.time()

        # Process request
        try:
            response: Response = await call_next(request)
        except Exception as exc:
            # Log unhandled exceptions with request ID
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                f"Request failed | request_id={request_id} | "
                f"method={request.method} | path={request.url.path} | "
                f"duration={duration_ms:.2f}ms | error={exc}"
            )
            raise

        # Add request ID to response headers
        response.headers["x-request-id"] = request_id

        # Log successful request
        duration_ms = (time.time() - start_time) * 1000
        logger.info(
            f"Request completed | request_id={request_id} | "
            f"method={request.method} | path={request.url.path} | "
            f"status={response.status_code} | duration={duration_ms:.2f}ms"
        )

        return response


class MetricsMiddleware(BaseHTTPMiddleware):
    """Middleware to collect Prometheus metrics for requests."""

    async def dispatch(self, request: Request, call_next) -> Response:
        # Skip metrics collection for metrics endpoint itself
        if request.url.path == "/metrics":
            return await call_next(request)

        # Get endpoint path (template, not actual path)
        endpoint = request.url.path
        method = request.method

        # Track request size
        content_length = request.headers.get("content-length")
        if content_length:
            http_request_size_bytes.labels(method=method, endpoint=endpoint).observe(
                int(content_length)
            )

        # Track request duration
        start_time = time.time()

        try:
            response: Response = await call_next(request)
            status_code = response.status_code
        except Exception as exc:
            # Record error metrics
            status_code = 500
            logger.error(f"Request failed: {exc}")
            raise
        finally:
            # Record duration
            duration = time.time() - start_time
            http_request_duration_seconds.labels(method=method, endpoint=endpoint).observe(duration)

            # Record request count
            http_requests_total.labels(
                method=method, endpoint=endpoint, status_code=status_code
            ).inc()

        # Track response size
        response_content_length = response.headers.get("content-length")
        if response_content_length:
            http_response_size_bytes.labels(method=method, endpoint=endpoint).observe(
                int(response_content_length)
            )

        # Add response time header for debugging
        response.headers["X-Response-Time"] = f"{duration:.3f}s"

        return response

"""Custom middleware for request tracking and logging."""

import logging
import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

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


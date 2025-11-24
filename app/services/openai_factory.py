"""OpenAI client factory."""

import os

from openai import OpenAI


def get_openai_api_key() -> str | None:
    """
    Get OpenAI API key from environment or settings.

    Returns:
        API key string or None if not configured
    """
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key

    try:
        from app.settings import settings

        return settings.openai_api_key
    except Exception:
        return None


def create_openai_client(api_key: str | None = None) -> OpenAI:
    """
    Create OpenAI client with proper error handling.

    Args:
        api_key: Optional API key (defaults to environment)

    Returns:
        Configured OpenAI client

    Raises:
        ValueError: If API key is not configured
    """
    key = api_key or get_openai_api_key()

    if not key:
        raise ValueError(
            "OpenAI API key required. Set OPENAI_API_KEY environment variable "
            "in your .env file or pass api_key parameter."
        )

    return OpenAI(api_key=key)

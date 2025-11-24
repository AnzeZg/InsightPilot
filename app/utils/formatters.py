"""Formatting utilities."""

import json
from datetime import datetime


def format_datetime(dt: datetime | None, format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format datetime to string, handling None gracefully.

    Args:
        dt: Datetime object or None
        format: strftime format string

    Returns:
        Formatted datetime string or empty string if None
    """
    if dt is None:
        return ""
    return dt.strftime(format)


def format_json_field(data: dict | list | None) -> str:
    """
    Format JSON field for display, handling None.

    Args:
        data: Dictionary, list, or None

    Returns:
        JSON string or empty string if None
    """
    if data is None:
        return ""
    return json.dumps(data, indent=2)

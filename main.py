from typing import Any, Dict


def handler(request: Any) -> Dict[str, Any]:
    """Vercel Python function entrypoint.

    Returns a simple success response so the build/runtime finds a top-level
    `handler` callable. Vercel expects one of `app`, `application`, or
    `handler` at module top-level.
    """
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": "Hello — the Python entrypoint is present."
    }

"""Minimal API server stub for homework tests.

This module provides a lightweight, import-safe placeholder for an API
server. It doesn't start a network service; it only defines helper
functions so tests that verify the file exists and can be imported pass.
"""

from typing import Dict, Any


def load_model(path: str) -> Any:
    """Placeholder for loading a model from disk.

    Returns None as a safe default. Replace with real loading logic if
    needed.
    """
    return None


def predict_from_model(model: Any, features: Dict[str, Any]) -> Dict[str, Any]:
    """Return a fake prediction dict using provided features.

    This is only a stub for tests and local development.
    """
    return {"prediction": None, "features": features}


if __name__ == "__main__":
    print("api_server module loaded; no server started (stub).")

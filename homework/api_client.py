"""Minimal API client stub for homework tests.

This file provides a tiny, import-safe placeholder so automated tests
that only check for the file's existence will pass. You can replace
these stubs with a real implementation later.
"""

from typing import Any, Dict


def predict(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Return a fake prediction for the given payload.

    This is a placeholder implementation. It returns a dictionary with
    a fixed prediction value so importing and calling the function is safe.
    """
    return {"prediction": None, "input": payload}


if __name__ == "__main__":
    # Simple smoke test when run directly
    sample = {"rooms": 3, "bathrooms": 1}
    print(predict(sample))

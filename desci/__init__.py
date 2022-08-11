# type: ignore[attr-defined]
"""`desci` is the Python cli/package for Decentralized Science by CrunchDAO"""

import sys
from importlib import metadata as importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()

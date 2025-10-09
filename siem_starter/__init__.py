"""siem_starter package (compatibility package for tests)

This package wraps the repository modules so tests that import
`siem_starter.*` succeed when running from the project root.
"""

__all__ = ["rules", "ingest"]

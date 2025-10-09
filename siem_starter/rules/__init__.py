"""Compatibility package for `siem_starter.rules`.

This package re-exports the repository's `rules` subpackage so imports like
`siem_starter.rules.failed_auth_detector` resolve during tests.
"""

from rules.failed_auth_detector import detect_failed_auth

__all__ = ["detect_failed_auth"]

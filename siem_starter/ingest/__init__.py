"""Compatibility package for `siem_starter.ingest`.

Re-exports modules from the repository-level `ingest` package so tests
and scripts can import via the `siem_starter.ingest` namespace.
"""

from ingest.parse_and_index import parse_apache_line, parse_file
from ingest.index_to_es import post_doc, stream_docs_from_stdin

__all__ = [
    "parse_apache_line",
    "parse_file",
    "post_doc",
    "stream_docs_from_stdin",
]

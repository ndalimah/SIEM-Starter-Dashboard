#!/usr/bin/env python3
"""Simple Apache log parser that emits JSON lines for each access log entry.

Usage: python3 parse_and_index.py sample_logs/sample_access.log > parsed.jsonl
"""

import sys
import json
import re
from datetime import datetime

APACHE_PATTERN = (
    r"(?P<host>\S+) \S+ \S+ \[(?P<time>[^]]+)\] "
    r'"(?P<request>[^\"]+)" (?P<status>\d{3}) (?P<size>\S+)'
)
APACHE_RE = re.compile(APACHE_PATTERN)


def parse_apache_line(line):
    m = APACHE_RE.match(line)
    if not m:
        return None
    d = m.groupdict()
    try:
        t = datetime.strptime(d['time'].split()[0], "%d/%b/%Y:%H:%M:%S")
        ts = t.isoformat() + 'Z'
    except Exception:
        ts = None
    return {
        'host': d.get('host'),
        'timestamp': ts,
        'request': d.get('request'),
        'status': int(d.get('status') or 0),
        'size': None if d.get('size') == '-' else int(d.get('size'))
    }


def parse_file(path):
    with open(path, 'r', encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rec = parse_apache_line(line)
            if rec:
                yield rec


def main():
    if len(sys.argv) < 2:
        print('Usage: parse_and_index.py <logfile>')
        return
    path = sys.argv[1]
    for r in parse_file(path):
        print(json.dumps(r))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys
import json
import argparse
from urllib import request, error


def post_doc(es_url, index, doc):
    url = f"{es_url}/{index}/_doc"
    data = json.dumps(doc).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = request.Request(url, data=data, method="POST", headers=headers)
    try:
        with request.urlopen(req, timeout=5) as resp:
            return resp.status
    except error.HTTPError as e:
        return e.code


def stream_docs_from_stdin():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        yield json.loads(line)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--es', default='http://localhost:9200')
    parser.add_argument('--index', default='siem-starter')
    args = parser.parse_args()
    for doc in stream_docs_from_stdin():
        status = post_doc(args.es, args.index, doc)
        print(f'doc -> status={status}')


if __name__ == '__main__':
    main()

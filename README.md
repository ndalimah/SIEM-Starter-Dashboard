# SIEM Starter — Ingest, Index, Dashboard, Detections

This project is a compact, interview-friendly SIEM starter kit demonstrating:

- Log ingestion (parser + indexer)
- Example detection rule (failed authentication detector)
- Sample logs and unit tests
- Kibana saved-objects placeholder and dashboard guidance
- CI to run tests

Quick start (local demo):

```bash
# From repo root
cd siem-starter
docker compose up -d
python3 ingest/parse_and_index.py sample_logs/sample_access.log > parsed.jsonl
cat parsed.jsonl | python3 ingest/index_to_es.py --index siem-starter-sample --bulk
```

Open Kibana at http://localhost:5601 and create an index pattern for `siem-starter-sample`.

What employers look for
- Clear README & architecture
- Demo data + one-click demo
- Tests & CI
- Detection-as-code with tests
- Safety notes where applicable

CI / Coverage
----------------

![Codecov](https://codecov.io/gh/<OWNER>/<REPO>/branch/main/graph/badge.svg)

To enable Codecov uploads from CI for private repositories, add a `CODECOV_TOKEN` secret in GitHub and uncomment the Codecov step in `.github/workflows/ci.yml`.

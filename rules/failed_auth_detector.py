from collections import defaultdict
from datetime import datetime


def detect_failed_auth(events, threshold=3, window_seconds=30):
    """Detect IPs with >= threshold 401 responses within window_seconds."""
    ips = defaultdict(list)
    alerts = []
    for e in events:
        ip = e.get('host')
        ts = e.get('timestamp')
        try:
            t = datetime.fromisoformat(ts.replace('Z', ''))
        except Exception:
            continue
        status = e.get('status')
        if status == 401:
            ips[ip].append(t)
            # remove old
            ips[ip] = [x for x in ips[ip] if (t - x).total_seconds() <= window_seconds]
            if len(ips[ip]) >= threshold:
                alerts.append({'ip': ip, 'count': len(ips[ip]), 'time': t.isoformat()})
    return alerts

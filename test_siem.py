from siem_starter.rules.failed_auth_detector import detect_failed_auth


def test_failed_auth_detection():
    events = [
        {'host': '192.0.2.1', 'timestamp': '2025-10-01T12:00:00Z', 'status': 401},
        {'host': '192.0.2.1', 'timestamp': '2025-10-01T12:00:05Z', 'status': 401},
        {'host': '192.0.2.1', 'timestamp': '2025-10-01T12:00:10Z', 'status': 401},
    ]
    alerts = detect_failed_auth(events, threshold=3, window_seconds=30)
    assert len(alerts) == 1
    assert alerts[0]['ip'] == '192.0.2.1'

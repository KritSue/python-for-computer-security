"""Summarize synthetic JSON security events by severity."""

import json
from pathlib import Path

path = Path(__file__).parent / "data" / "events.json"
events = json.loads(path.read_text(encoding="utf-8"))
counts = {}
for event in events:
    severity = event.get("severity", "unspecified")
    counts[severity] = counts.get(severity, 0) + 1
print("Events by severity:", counts)

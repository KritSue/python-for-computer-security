"""Summarize synthetic JSON events without displaying user identifiers."""

import json
import sys
from pathlib import Path

if len(sys.argv) > 2:
    raise SystemExit("Usage: python defensive_monitor.py [EVENTS.json]")
path = Path(sys.argv[1]) if len(sys.argv) == 2 else Path(__file__).parent / "data" / "events.json"
events = json.loads(path.read_text(encoding="utf-8"))
severity_counts = {}
failed = 0
for event in events:
    if not isinstance(event, dict):
        continue
    severity = event.get("severity", "unspecified")
    severity_counts[severity] = severity_counts.get(severity, 0) + 1
    if event.get("result") == "failed":
        failed += 1
print("Total events:", len(events))
print("Events by severity:", severity_counts)
print("Failed outcomes:", failed)
print("Counts support review; they do not establish an incident.")

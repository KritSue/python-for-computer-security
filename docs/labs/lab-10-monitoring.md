# Lab 10 — Defensive log monitoring

Run `python examples/defensive_monitor.py examples/data/events.json`. This small tool summarizes synthetic event severity and counts failed outcomes. It produces an aggregate report rather than printing every identifier.

**Extend it:** add a command-line threshold; count malformed records; write a summary JSON report; explain one limitation of the rule. Keep your inputs synthetic. A monitor raises review signals; it does not prove an incident.

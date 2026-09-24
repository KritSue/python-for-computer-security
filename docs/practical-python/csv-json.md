# CSV and JSON

**Goal:** read tabular CSV and structured JSON using Python's standard library.

CSV is a simple table format. DictReader accesses columns by header name. JSON stores objects and lists and is common in web services and event exports.

~~~python
import csv
from pathlib import Path

with Path("examples/data/failed_logins.csv").open(newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["username"], row["result"])
~~~

~~~python
import json
from pathlib import Path

events = json.loads(Path("examples/data/events.json").read_text(encoding="utf-8"))
for event in events:
    print(event.get("event_id"), event.get("result", "unknown"))
~~~

json.loads parses JSON text in memory; json.load reads an open file. CSV values are text, so convert numeric fields after handling invalid input.

**Security connection:** structured formats simplify parsing, but data may still be missing or malformed. Check required fields and report bad rows.

**Common mistakes:** treating CSV strings as integers; expecting JSON objects to have every key; confusing JSON null with Python None; malformed JSON raises JSONDecodeError.

**Exercises:** count failed rows; print event IDs with warning level high; report malformed rows with their line number. Guidance: compare text exactly and use get for optional JSON fields.

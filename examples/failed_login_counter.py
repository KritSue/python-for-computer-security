"""Count synthetic failed login events per username."""

import csv
from pathlib import Path

path = Path(__file__).parent / "data" / "failed_logins.csv"
counts = {}
with path.open(newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if row.get("result") == "failed":
            username = row.get("username", "unknown")
            counts[username] = counts.get(username, 0) + 1

for username, count in sorted(counts.items()):
    print(username, count)

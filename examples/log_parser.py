"""Count outcomes in the course's synthetic sample log."""

from pathlib import Path

path = Path(__file__).parent / "data" / "sample.log"
counts = {"failed": 0, "success": 0}
malformed = 0

for line in path.read_text(encoding="utf-8").splitlines():
    fields = dict(part.split("=", 1) for part in line.split() if "=" in part)
    result = fields.get("result")
    if result in counts:
        counts[result] += 1
    else:
        malformed += 1

print("Outcome counts:", counts)
print("Unrecognized records:", malformed)

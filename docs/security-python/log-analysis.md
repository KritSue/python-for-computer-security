# Defensive log analysis

**Goal:** count events in a small, synthetic log without treating a count as proof.

A log is a time-ordered record of events. Formats vary by system. This course sample uses invented lines with a timestamp, result, username, and documentation-only source address. A simple parser can summarize one known format:

~~~python
from pathlib import Path

failed = 0
for line in Path("examples/data/sample.log").read_text(encoding="utf-8").splitlines():
    if " result=failed " in line:
        failed += 1
print("Failed events:", failed)
~~~

This counts matching text only. It does not identify an attacker or establish cause. For more reliable analysis, parse fields explicitly, validate timestamps, handle malformed rows, and preserve a record of what was skipped.

**Privacy:** use synthetic data for practice. If working with real logs, follow your institution's authorization, privacy, retention, and access rules. Print aggregate summaries where individual identifiers are unnecessary.

**Common mistakes:** counting substring matches in unrelated fields; assuming every system shares the same log format; hiding malformed lines without reporting them.

**Exercises:** count successes separately; count failures per synthetic username; skip and report a malformed line. Guidance: use a dictionary for per-user counts.

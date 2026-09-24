# Files and pathlib

**Goal:** read a text file using paths that work across operating systems.

A file path is an address. pathlib.Path represents paths and avoids hard-coding slash styles. This example reads the course's small sample file:

~~~python
from pathlib import Path

log_path = Path("examples") / "data" / "sample.log"
if log_path.exists():
    for line in log_path.read_text(encoding="utf-8").splitlines():
        print(line)
else:
    print("Sample log was not found")
~~~

The path is relative to the current working folder, usually where you started the program. Use with when opening a file so Python closes it automatically:

~~~python
with Path("notes.txt").open(encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
~~~

**Security connection:** use synthetic or authorized logs. Do not expose personal data in a printed or uploaded report.

**Common mistakes:** running from a different folder; wrong capitalization; forgetting a file may be missing; omitting text encoding.

**Exercises:** read examples/data/sample.log; count its lines; write a summary file. Guidance: use Path, exists, and write_text for small files.

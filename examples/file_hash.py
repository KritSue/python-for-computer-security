"""Print a SHA-256 digest for a specified file."""

import hashlib
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("Usage: python file_hash.py PATH")

path = Path(sys.argv[1])
hasher = hashlib.sha256()
with path.open("rb") as file:
    for block in iter(lambda: file.read(4096), b""):
        hasher.update(block)
print(hasher.hexdigest())

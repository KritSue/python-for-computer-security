# Cheat sheets

## Python syntax and types

~~~python
name = "text"       # str
count = 3            # int
ratio = 0.5          # float
ready = True         # bool
print(name, count)
~~~

## Conditions and loops

~~~python
if count >= 3:
    print("review")
for item in items:
    print(item)
~~~

## Functions and collections

~~~python
def double(value):
    return value * 2

items = ["a", "b"]
record = {"result": "failed"}
unique = set(items)
~~~

Lists preserve order and duplicates; sets keep unique items; dictionaries map keys to values; tuples are ordered groups commonly treated as fixed.

## Files and exceptions

~~~python
from pathlib import Path

try:
    text = Path("sample.txt").read_text(encoding="utf-8")
except FileNotFoundError:
    print("File not found")
~~~

## Regex, networking, and HTTP

~~~python
import re
from ipaddress import ip_address

match = re.search(r"user=(\w+)", line)
address = ip_address("127.0.0.1")
~~~

An IP address identifies an interface; a port selects a service endpoint. HTTP requests and responses carry methods/status codes, headers, and sometimes bodies. Use localhost for course networking labs.

## Hashing

~~~python
import hashlib

digest = hashlib.sha256(b"sample").hexdigest()
~~~

SHA-256 supports integrity comparison, not encryption or password storage. Base64 is encoding, not encryption.

## Git basics

~~~console
git status
git add filename.py
git commit -m "Describe the change"
git log --oneline
~~~

Git records project history. Stage only files you intend to include. Never commit secrets; `.gitignore` helps keep local environments out of version control.

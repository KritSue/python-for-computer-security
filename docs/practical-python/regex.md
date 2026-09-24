# Regular expressions

**Goal:** find simple text patterns with Python's re module.

A regular expression describes a pattern in text. It helps when a format is consistent, but ordinary string methods are simpler for exact matches.

~~~python
import re

line = "2026-09-24 failed user=casey source=192.0.2.25"
match = re.search(r"user=(\w+)", line)
if match:
    print(match.group(1))
~~~

The r prefix makes backslashes easier to read. \w+ matches one or more word characters; parentheses capture the matched part. Output is casey. A pattern such as \d{4}-\d{2}-\d{2} checks the shape of a date, not whether the date exists.

**Security connection:** extract fields from a known synthetic log format. Regex is not a substitute for a proper parser or input validation.

**Common mistakes:** using match when a pattern can occur later in a line (search); assuming a match proves the value is valid; making patterns so broad they capture unintended text.

**Exercises:** find a 4-digit year; extract a user field; count lines containing the word failed. Guidance: test normal, missing, and unusual input.

# Secure coding habits

**Goal:** make beginner scripts safer and easier to review.

- Validate external data with standard-library parsers where available. Validation answers a narrow question; it does not make every later operation safe.
- Handle expected failures specifically, such as a missing file or invalid integer. Do not hide all exceptions.
- Use timeouts for network operations and restrict examples to loopback or authorized services.
- Keep secrets out of code and Git. Use environment variables for local configuration; do not print secret values. For example, Python's os.environ.get("SERVICE_TOKEN") reads a variable that you set outside the source file.
- Avoid building shell commands from untrusted text. Prefer Python APIs and pass arguments separately when a subprocess is genuinely needed.
- Minimize personal data in outputs. Use invented test records.
- For passwords, use a maintained password-hashing library in a real application. A general-purpose hash is not adequate password storage.

~~~python
import os

token = os.environ.get("SERVICE_TOKEN")
if token is None:
    print("Set SERVICE_TOKEN before running this tool")
else:
    print("Configuration is present")
~~~

**Practice:** review a script and ask: what input can vary, what happens on missing or malformed input, what data is printed, and what network destinations can it contact?

"""Inspect selected metadata from the course's local HTTP service."""

from urllib.request import Request, urlopen

request = Request("http://127.0.0.1:8000/", method="GET")
with urlopen(request, timeout=3) as response:
    print("Status:", response.status)
    print("Content-Type:", response.headers.get("Content-Type", "unknown"))

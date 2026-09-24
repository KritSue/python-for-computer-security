# HTTP requests and responses

**Goal:** understand what a basic web request contains and inspect an authorized response.

HTTP defines requests and responses. A request has a method (often GET to retrieve), a URL, headers, and sometimes a body. A response has a status code, headers, and possibly a body. Headers carry metadata such as content type. HTTPS wraps HTTP in encrypted transport; this lesson focuses on the message concepts.

Use Python's built-in urllib to fetch a public documentation page only when you choose to, or run against a local test service. Always set a timeout:

~~~python
from urllib.request import Request, urlopen

request = Request("http://127.0.0.1:8000/", method="GET")
with urlopen(request, timeout=3) as response:
    print(response.status)
    print(response.headers.get("Content-Type", "unknown"))
~~~

This example expects a service on your own machine. A status code is context: 404 means the requested resource was not found; it does not imply an attack. Avoid sending secrets in URLs or printing authorization headers.

**Common mistakes:** no service is listening; confusing response status with request method; printing sensitive headers; waiting forever without a timeout.

**Exercises:** explain method, status, and header; inspect only Content-Type from a local service; explain why a 200 response does not prove content is trustworthy.

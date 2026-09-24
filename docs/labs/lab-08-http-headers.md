# Lab 08 — HTTP header inspector

This lab contacts only a local service. In one terminal run `python examples/local_http_server.py`. In a second terminal run `python examples/http_header_inspector.py`. Stop the server with Ctrl+C when finished.

The client displays the response status and `Content-Type` header only. A header describes a response; it may not be trustworthy just because it exists. The server binds to loopback only.

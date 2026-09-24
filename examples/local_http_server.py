"""A tiny HTTP service bound to loopback for a local learning lab."""

from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"Local training service only\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print("Serving on http://127.0.0.1:8000; Ctrl+C stops the service")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()

# Lab 09 — Simple socket client

In one terminal start `python examples/local_socket_server.py`. In another run `python examples/socket_client.py`. Both programs bind/connect only to 127.0.0.1. Stop the server with Ctrl+C.

Observe the server's reply. TCP transfers bytes; the client decodes those bytes as text. Try stopping the server first and see the connection error. Never retarget this beginner lab at a host you do not own or have permission to use.

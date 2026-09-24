"""Connect to the paired course server on this computer only."""

import socket

with socket.create_connection(("127.0.0.1", 8001), timeout=3) as connection:
    connection.sendall(b"hello from the local client\n")
    reply = connection.recv(1024)
    print(reply.decode("utf-8", errors="replace"))

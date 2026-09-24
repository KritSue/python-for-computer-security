# Sockets

**Goal:** understand how a Python program exchanges bytes with a service.

A socket is a software endpoint for sending or receiving network data. TCP provides a connection-oriented byte stream. The client below connects only to this computer's loopback interface and one port entered by the learner.

~~~python
import socket

host = "127.0.0.1"
port = 8000
with socket.create_connection((host, port), timeout=3) as connection:
    connection.sendall(b"hello\n")
    reply = connection.recv(1024)
    print(reply.decode("utf-8", errors="replace"))
~~~

This works only when you intentionally start a compatible local service on port 8000. Bytes are the data sent across a socket; decode turns received bytes into text. A timeout prevents waiting forever. `recv(1024)` reads at most 1024 bytes, not necessarily a whole message.

**Safety:** keep host set to 127.0.0.1. Do not change it to a public or campus system without permission.

**Common mistakes:** no server is listening; client and server expect different formats; assuming one recv returns the full message; forgetting to handle connection errors.

**Exercises:** explain what a port does; add a try/except for ConnectionRefusedError; change the displayed request only after confirming the local server's expected format.

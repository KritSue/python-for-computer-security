"""A one-client TCP server bound only to the local loopback interface."""

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 8001))
    server.listen(1)
    print("Waiting on 127.0.0.1:8001; Ctrl+C stops the server")
    connection, _address = server.accept()
    with connection:
        message = connection.recv(1024)
        print("Received bytes:", message)
        connection.sendall(b"Local training reply\n")

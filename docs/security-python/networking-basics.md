# Networking foundations

**Goal:** learn the words needed to understand a simple network client.

A network lets computers exchange data. An IP address identifies a network interface for communication. A port is a numbered endpoint used by a program. TCP establishes an ordered connection; UDP sends individual datagrams without the same delivery guarantee. DNS looks up names such as example.org to find network addresses.

An application such as a browser uses protocols: agreed formats and rules. HTTP is a common protocol for requesting web resources. A URL identifies a resource and may include a scheme, host, port, path, and query.

~~~text
http://127.0.0.1:8000/status
scheme: http | host: 127.0.0.1 | port: 8000 | path: /status
~~~

The loopback address 127.0.0.1 refers to this computer. A port number does not itself say whether an application is safe. A client can connect only if a service is listening and local/network rules allow it.

**Safety:** this course's socket activities use loopback. Only connect to other systems when you have explicit authorization.

**Common misconception:** formatting an IP address correctly does not prove that a computer is reachable. DNS names and IP addresses are different kinds of identifiers.

**Exercises:** identify the scheme and port in a URL; explain the difference between an IP and a port; describe why a browser needs HTTP rules.

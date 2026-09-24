# Dictionaries

**Goal:** associate a named key with each value.

A dictionary stores key/value pairs. It is useful when each record has named fields.

~~~python
event = {
    "username": "casey",
    "source_ip": "192.0.2.25",
    "result": "failed",
}
print(event["username"])
print(event.get("status", "unknown"))
~~~

Square brackets look up a required key. get can provide a default when a key is absent. Keys are commonly strings; values can be different types. A missing key accessed with brackets raises KeyError.

~~~python
for key, value in event.items():
    print(key, "=", value)
~~~

**Security connection:** JSON objects become Python dictionaries. Keep only fields needed for the task, especially when records might contain personal data.

**Common mistakes:** misspelling a key; assuming get changes the dictionary; expecting a dictionary to sort its records automatically.

**Exercises:** make a dictionary for a synthetic HTTP event; safely print an optional user_agent; count dictionaries with result equal to failed. Guidance: use get and a loop.

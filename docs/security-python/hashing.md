# Encoding and hashing

**Goal:** distinguish encoding from hashing and calculate a file's SHA-256 digest.

Encoding represents data in another form. Base64 changes binary/text representation so it can travel through text-only systems; it is not encryption and offers no secrecy. A cryptographic hash maps data to a fixed-size digest. SHA-256 can help compare file integrity, but does not reveal or restore the original content.

~~~python
import hashlib
from pathlib import Path

hasher = hashlib.sha256()
with Path("examples/data/sample.log").open("rb") as file:
    for block in iter(lambda: file.read(4096), b""):
        hasher.update(block)
print(hasher.hexdigest())
~~~

The file is opened in binary mode so its exact bytes are hashed. Compare a digest to a value from a trusted source; if both came from the same untrusted place, that comparison proves little.

**Password note:** do not store passwords as plain text or use fast SHA-256 directly for password storage. Real systems use a purpose-built password hashing function such as Argon2id, scrypt, or bcrypt with a salt and suitable cost settings.

**Common mistakes:** calling Base64 encryption; hashing text without deciding its encoding; assuming equal-looking filenames imply equal content.

**Exercises:** calculate SHA-256 for a sample file; change one byte and compare; explain why a digest cannot decrypt the file.

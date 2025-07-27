ba = bytearray(b'Hello')
ba[0] = 72
print(ba)
print(type(ba))
immutable_bytes = bytes(ba)
print(immutable_bytes)
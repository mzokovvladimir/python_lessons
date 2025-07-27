import struct

b1 = bytes("Hello, world!", encoding='utf-8')
print(b1)
print(type(b1))

b2 = bytes([72, 101, 108, 108, 111])
print(b2)
print(type(b2))
text = "Hello, world!"
tmp = text[0]
print(tmp)
print(type(tmp))
my_tmp = ord(tmp)
print(my_tmp)
print(type(my_tmp))
print(chr(my_tmp))


print(b1[0])
print(b2[:5])
print(b1 + b' Python!')
print(b"Hello" in b1)

num = 1024
byte_repr = num.to_bytes(4, byteorder='big')
print(byte_repr)

restored_num = int.from_bytes(byte_repr, byteorder='big')
print(restored_num)

data = struct.pack('i', num)
print(data)

unpacked_data = struct.unpack('i', data)
print(unpacked_data)
print(type(unpacked_data))
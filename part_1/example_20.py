s = "Вітаю!"

print(type(s))
print(len(s))

b = s.encode("utf-8")

print(type(b))
print(len(b))
print(b)

s = b.decode("utf-8")

print(type(s))
print(len(s))
print(s)

print(b.decode('windows-1251'))
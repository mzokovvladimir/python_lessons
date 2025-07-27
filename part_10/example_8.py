import re

result = re.findall(r'\w{2}', 'Qwerty Admin')
print(result)
# Вилучення 2х послідовних символів
result = re.findall(r'\b\w.', 'qwerty a.dmin')
print(result)

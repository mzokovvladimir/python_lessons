import re

string = 'Hello1 Hello2 Hello3 Hello4 Hello5'
pattern = "Hello"

for match in re.finditer(pattern, string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(),
        end=match.end())
    # Виводимо кожен знайдений результат:
    print(s)

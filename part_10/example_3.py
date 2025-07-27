import re

string = "test1 test2 test3 !@$%$#^@$% 6587 65876 &@^&$,.test4 test5"

result = re.split(r"[!@#$%^&,.\s]+", string, maxsplit=10)
print(result)

print(len(result))
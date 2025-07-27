def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


operations = {
    "+": add,
    "-": subtract,
}


print(add(2, 3))
print(subtract(2, 3))
print(operations["+"](2, 3))
print(operations["-"](2, 3))
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}

print(operations["+"](2, 3))
print(operations["-"](2, 3))


data = {
    1: "y",
    2: "t",
    0: "w",
}
print(sorted(data))
data_1 = list(data.items())
print(data_1)
print(type(data_1))
data_1.sort()
print(data_1)
data_1.sort(key=lambda x: x[1])
print(data_1)
data_2 = dict(data_1)
print(data_2)
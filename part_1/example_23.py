"""my_set = {1, 2, 3}
print(my_set)
print(type(my_set))
print(len(my_set))
my_set.add(5)
print(my_set)
my_set.add("2")
print(2 in my_set)
my_set.update([1, 2, 3, 4])
print(my_set)
my_set.remove(1)
print(my_set)
my_set.discard(11)
print(my_set)
my_set.discard(5)
print(my_set)

"""
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {10, 3, 8, 5, 15}
print(my_set_1, my_set_2)
print(my_set_1 | my_set_2)
print(my_set_1.union(my_set_2))
print(my_set_1 & my_set_2)
print(my_set_1.intersection(my_set_2))
print(my_set_1 - my_set_2)
print(my_set_1.difference(my_set_2))
print((my_set_1 | my_set_2) - (my_set_1 & my_set_2))
print((my_set_1 - my_set_2) | (my_set_2 - my_set_1))
print(my_set_1 ^ my_set_2)
print(my_set_1.symmetric_difference(my_set_2))
my_list = list(range(10)) * 3
print(my_list)
print(set(my_list))
my_set = {}
print(type(my_set))
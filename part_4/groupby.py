from itertools import groupby


def bigger_than_5(digit):
    return digit > 5


my_list = [25, 13, 11, 19, 28, 20, -24, 10, -68, 0, 5, -16, 1, 30, -31, 3, 21]
group_obj = groupby(my_list, key=bigger_than_5)
for key, value in group_obj:
    print(key, list(value))
print('-' * 100)
group_obj = groupby(sorted(my_list), key=bigger_than_5)
for key, value in group_obj:
    print(key, list(value))

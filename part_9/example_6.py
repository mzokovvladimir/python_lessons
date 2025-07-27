my_list = [1, 2, 3, 4, 5, 6, 7]


def my_function_v1(some_list: list) -> list:
    new_list = []
    for item in my_list:
        if item % 2 != 0:
            new_list.append(item)
    return new_list


def my_function_v2(some_list: list) -> list:
    return [item for item in my_list if item % 2 != 0]


def my_function_v3(some_list: list) -> list:
    return (item for item in my_list if item % 2 != 0)


print(my_function_v1(my_list))
print(my_function_v2(my_list))
print(my_function_v3(my_list))

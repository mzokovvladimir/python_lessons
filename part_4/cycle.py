from itertools import cycle


def my_func(lst: list, iterations: int):
    """Функція, яка проходитиме за елементами списку lst (цілі числа) кількість разів циклічно.
    Один раз – один елемент списку.
    Після виведення останнього значення послідовності процес розпочнеться спочатку."""
    result = ''
    iter_lst = cycle(lst)
    print(type(iter_lst))
    if lst:
        for _ in range(iterations):
            result += str(next(iter_lst)) + ' '
    return result[:-1]


print(my_func([23, 55, 18, 31, 57, 61, 11], 5))
print(my_func([22, 15, 18, 12, 75, 11, 35], 15))
print(my_func([], 1000))
print(my_func([10], 7))

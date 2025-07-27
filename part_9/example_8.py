import timeit


def show_letters1(some_str):
    yield from ''.join([letter for letter in some_str if letter.isdigit()])


def show_letters2(some_str):
    return ''.join([letter for letter in some_str if letter.isdigit()])


print(type(show_letters1('qwerty')))
print(type(show_letters2('qwerty')))

'''Вимірювання часу виконання шматка коду за допомогою модуля «timeit».
Модуль timeit дозволяє виміряти час виконання будь-якого шматка коду.
Великі шматки коду не дуже зручно, але дрібні досить добре. Закидаємо рядок всередину timeit і вуаля.
'''

print("Звичайний вираз", timeit.timeit('"-".join(str(n) for n in range(10000))', number=10000))
print("Вираз-генератор", timeit.timeit('"-".join((str(n) for n in range(10000)))', number=10000))
print("list expressions", timeit.timeit('"-".join([str(n) for n in range(10000)])', number=10000))
print("MAP:", timeit.timeit('"-".join(map(str, range(10000)))', number=10000))

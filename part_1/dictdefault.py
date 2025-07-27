""" Словник із значеннями за замовчуванням.
Клас defaultdict() модуля collections нічим не відрізняється від звичайного словника за вийнятком того, що за
замовчуванням завжди викликається функція, яка повертає значення за замовчуванням для нових значень.
Тобто Клас defaultdict() являє собою словник зі значеннями за замовчуванням."""
from collections import defaultdict

seq = [('red', 81), ('green', 42), ('green', 3), ('white', 2), ('orange', 5), ('red', 15)]
my_dict = defaultdict(list)
# default_factory – тип даних або функція, яка повертає значення за замовчуванням для нових значень.

# Клас defaultdict() модуля collections повертає новий словник-подібний об'єкт. Defaultdict є підкласом вбудованого
# класу dict(). Він перевизначає один метод і додає одну доступну для запису змінну екземпляра. Решта функціональності
# така сама, як і для класу dict(), і тут вона не описана.
# Перший аргумент надає початкове значення атрибуту default_factory. За замовчуванням None. Всі інші аргументи
# обробляються так само, якби вони були передані конструктору dict(), включаючи ключові аргументи.

for key, value in seq:
    my_dict[key].append(value)

print('defaultdict(list):', sorted(my_dict.items()))


seq = [('red', 81), ('green', 42), ('green', 3), ('white', 2), ('orange', 5), ('red', 15)]
my_dict = {}
for key, value in seq:
    my_dict.setdefault(key, []).append(value)

print('setdefault:', sorted(my_dict.items()))

# Встановлення функції int() як функції default_factory, що генерує значень за умовчанням, робить defaultdict()
# корисним для підрахунку чогось:
seq1 = 'programming'
my_dict1 = defaultdict(int)
for key in seq1:
    my_dict1[key] += 1

print('defaultdict(int):', sorted(my_dict1.items()))
# Коли літера зустрічається вперше, вона відсутня у словнику d, тому функція default_factory викликає функцію int(),
# щоб надати значення лічильника за умовчанням, що дорівнює нулю.

seq = [('red', 81), ('green', 42), ('green', 3), ('white', 2), ('orange', 5), ('red', 15)]
my_dict = defaultdict(set)
for key, value in seq:
    my_dict[key].add(value)

print('defaultdict(set):', sorted(my_dict.items()))

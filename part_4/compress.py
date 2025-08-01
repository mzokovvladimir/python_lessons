from itertools import compress

# Фільтрація списку без циклу
leaders = ['Alice', 'Bob', 'Charlie', 'David']
selector = [1, 0, 1, 0]
print(list(compress(leaders, selector)))

# Припустимо, що у нас є список студентів та їх оцінки
students = ['Alice', 'Bob', 'Charlie', 'David']
grades = [90, 78, 65, 92]

# Створюємо булевий список, де True відповідає студентам, які отримали більше 80 балів
passed = [grade > 80 for grade in grades]

# Використовуємо compress для вибору лише тих студентів, які отримали більше 80 балів
passed_students = list(compress(students, passed))

print("Студенти, які отримали більше 80 балів:", passed_students)


"""
Функція compress з модуля itertools надає декілька переваг, особливо коли вам потрібно ефективно вибирати елементи з 
одного ітерабельного об'єкта на основі значень з іншого об'єкта-маски. Ось деякі переваги compress:

1. Ліниве вироблення: Як і більшість інших інструментів з itertools, compress працює ліниво, тобто вона виробляє 
значення лише тоді, коли вони потрібні. Це особливо корисно, коли вам не потрібно витрачати ресурси на обробку всіх 
елементів наперед.

2. Ефективність пам'яті: compress дозволяє вам ефективно фільтрувати елементи на основі булевої маски без створення 
нового списку. Він використовує лише ті елементи, для яких відповідні значення в масці дорівнюють True."""

data = [1, 2, 3, 4, 5]
mask = [True, False, True, False, True]

filtered_data = list(compress(data, mask))

"""
3. Зручність в застосуванні маски: compress робить простим використання булевої маски для вибору тих елементів, які 
потрібно включити в результат. Це особливо корисно, коли вам потрібно вибрати елементи на основі умови, або ж коли 
маска генерується динамічно."""


temperatures = [25, 18, 30, 22, 28]
mask = [temp > 20 for temp in temperatures]

warm_days = list(compress(temperatures, mask))
"""
4. Використання з генераторами: compress може ефективно співпрацювати з генераторами, оскільки не вимагає створення 
повноцінного списку."""


data_generator = (x for x in range(10))
mask = [True, False, True, False, True, False, True, False, True, False]

filtered_data = list(compress(data_generator, mask))
"""Загальною перевагою є те, що compress дозволяє ефективно та лінійно вибирати елементи з ітерабельного об'єкта на 
основі маски, при цьому зберігаючи ефективність ресурсів і пам'яті.
"""
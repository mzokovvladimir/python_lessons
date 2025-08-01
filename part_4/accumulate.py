"""Функція accumulate з модуля itertools в Python використовується для поелементного накопичення значень в ітерованому
об'єкт. Вона повертає ітератор, котрий по черзі повертає накопичені значення. Приклад використання:
"""
from itertools import accumulate
import operator

# Приклад 1: Додавання елементів списку
numbers = [1, 2, 3, 4, 5]
result = accumulate(numbers)
print(type(result))
print(list(result))  # Результат: [1, 3, 6, 10, 15]

# Приклад 2: Множення елементів списку
numbers = [1, 2, 3, 4, 5]
result = accumulate(numbers, operator.mul)
print(type(result))
print(list(result))  # Результат: [1, 2, 6, 24, 120]
"""У першому прикладі використовується додавання, а в другому - множення. Якщо не передати функцію другим аргументом, 
то використовуватиметься додавання за замовчуванням.
Функція accumulate корисна в ситуаціях, коли вам потрібно поступово нарощувати результат у міру проходження об'єкта, 
що ітерується.

Використання функції accumulate з модуля itertools може мати кілька переваг у певних сценаріях:

Економія пам'яті: accumulate повертає ітератор, що означає, що значення обчислюються при необхідності, а чи не 
заздалегідь створюються у пам'яті. Це може бути корисним при роботі з великими обсягами даних, де заздалегідь створити 
весь список може призвести до надмірного використання пам'яті.

Ліниві обчислення: Функція accumulate підтримує ліниві обчислення, що означає, що вона обчислює значення тільки при 
запиті. Це може бути корисним у ситуаціях, коли вам потрібно обробляти великий обсяг даних і хочете уникнути 
попереднього обчислення всіх значень.

Простота коду: Використання accumulate може зробити код більш читаним та компактним, особливо у випадках, коли вам 
потрібно виконувати покрокові обчислення чи накопичення значень.

Гнучкість: Ви можете використовувати різні функції акумуляції, передаючи їх другим аргументом. Це дозволяє виконувати 
різні види акумуляції, такі як додавання, множення, конкатенація і т. д., залежно від ваших потреб.

Однак варто пам'ятати, що в деяких випадках використання accumulate може бути неефективним або менш зручним, ніж інші 
способи обробки даних, залежно від конкретних вимог вашого завдання.
"""
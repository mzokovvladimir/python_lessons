"""zip_longest(*iterables, fillvalue=None): 
Повертає ітератор, який об'єднує значення з різних ітерабельних об'єктів. 
Різниця від zip полягає в тому, що zip_longest робить виведення до найбільшої 
довжини ітерабельного об'єкта, доповнюючи відсутні значення значенням fillvalue."""

from itertools import zip_longest

numbers = [1, 2, 3]
letters = ['a', 'b']

zipped = zip_longest(numbers, letters, fillvalue=None)

for item in zipped:
    print(item)

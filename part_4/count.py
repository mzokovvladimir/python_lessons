"""
count(start=0, step=1): 
Створює ітератор чисел, які починаються з start і збільшуються на step.
"""
from itertools import count

for i in count(start=5, step=2):
    if i > 20:
        break
    print(i)

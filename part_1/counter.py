"""
collections.Counter - вид словника, який дозволяє підраховувати кількість незмінних об'єктів
(у більшості випадків, рядків).
"""
from collections import Counter

c = Counter()
for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
    c[word] += 1

print(c)
print(c['counter'])

print(c['collections'])
# elements() - повертає список елементів у лексикографічному порядку.
c = Counter(a=5, b=3, c=0, d=-10)
print(list(c.elements()))
# most_common([n]) - повертає n елементів, що найчастіше зустрічаються, в порядку убування зустрічальності.
# Якщо n не вказано, всі елементи повертаються.

print(Counter('abracadabra').most_common(3))

# subtract([iterable-or-mapping]) - вичитування
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
print()
print('C & D:', c, d, sep='\n')
print()
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
# Найчастіше вживані шаблони для роботи з Counter:
# sum(c.values()) - загальна кількість.
# c.clear() – очистити лічильник.
# list(c) – список унікальних елементів.
# set(c) - перетворити на безліч.
# dict(c) - перетворити на словник.
# c.most_common()[:-n:-1] - n найменш часто зустрічаються елементів.
# c += Counter() - видалити елементи, що зустрічаються менше одного разу.
# Counter також підтримує складання, віднімання, перетин та об'єднання:
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)
print(c - d)
print(c & d)
print(c | d)

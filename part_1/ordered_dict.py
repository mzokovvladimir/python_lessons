"""
Упорядковані словники схожі на звичайні, але зберігають порядок вставки у них елементів. При ітеруванні за
впорядкованим словником, його елементи видаються у порядку, у якому вони були додані.

Тобто, навіть якщо значення ключа оновлюється, спочатку задане місце ключа у словнику залишається незмінним. Однак,
якщо видалити ключ і знову вставити, то він опиниться на останньому місці.

collections.OrderedDict - ще один схожий на словник об'єкт(підклас працює з версії 3.7+), але він пам'ятає порядок,
у якому йому було дано ключі.
Методи:
popitem(last=True) - видаляє останній елемент якщо last=True, і перший, якщо last=False.
move_to_end(key, last=True) - додає ключ у кінець якщо last=True, і на початок, якщо last=False.
"""
from collections import OrderedDict

my_dict = OrderedDict()
my_dict['job_title'] = 'engineer'
my_dict['portfolio'] = ['work_1', 'work_2']
my_dict['experience'] = 2.5
my_dict['job_title'] = 'software engineer'  # поки ще перший
my_dict['duration'] = 1.5
print(my_dict)

for key in my_dict:
    print(key)  # job_title, portfolio, experience, duration
print()
del my_dict['job_title']
print(my_dict, end='\n\n')
my_dict['job_title'] = 'lead software engineer'
print(my_dict, end='\n\n')

for key in my_dict:
    print(key)  # job_title, portfolio, experience, duration


"""d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(OrderedDict(sorted(d.items(), key=lambda t: t[0])))
print(OrderedDict(sorted(d.items(), key=lambda t: t[1])))
print(OrderedDict(sorted(d.items(), key=lambda t: len(t[0]))))"""
"""
Проверка на равенство одного упорядоченного словаря другому учитывает порядок их элементов: 
list(odict1.items())==list(odict2.items()). В то же время при сравнении с другими представителями отображений порядок 
во внимание не принимается: это позволяет использовать OrderedDict в тех местах, где используются обычные словари.

На заметку
По сравнению с обычными словарями для OrderedDict вопросы об эффективности использования памяти, скорости итерирования, 
быстродействия операций обновления были отодвинуты на второй план. На первом месте — операции, связанные с 
[пере]определением порядка. Поэтому упорядоченные словари выигрывают в сценариях, с частым переупорядочиванием 
элементов, подобных LRU-кешу.

В остальном, упорядоченный словарь ведёт себя аналогично обычному (наследует его свойства и методы), предлагая, однако же, дополнительные инструменты.
https://pythonz.net/references/named/mapping/
"""
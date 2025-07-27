from collections import ChainMap

# Створюємо два словники
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}

# Створюємо ланцюжок із двох словників
chain = ChainMap(dict1, dict2)
print(type(chain))
# Звертаємося до елементів ланцюжка
print(chain['one'])    # 1
print(chain['three'])  # 3

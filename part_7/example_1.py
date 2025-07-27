class LoggedObject:
    def __init__(self):
        """Використовуємо словник для збереження атрибутів"""

        super().__setattr__('_attributes', {})

    def __getattribute__(self, name):
        """Викликається при доступі до атрибутів"""

        print(f"[GETATTRIBUTE] Attempting to access '{name}'")
        try:
            return super().__getattribute__(name)
        except AttributeError:
            # Якщо атрибут не знайдено, передаємо його в __getattr__
            return self.__getattr__(name)

    def __getattr__(self, name):
        """Викликається, якщо атрибут не знайдено"""

        print(f"[GETATTR] Attribute '{name}' not found. Returning default value.")
        return None

    def __setattr__(self, name, value):
        """Викликається при спробі встановити значення атрибута"""

        print(f"[SETATTR] Setting '{name}' to '{value}'")
        if name.startswith('_'):
            # Зберігаємо службові атрибути безпосередньо
            super().__setattr__(name, value)
        else:
            # Для інших атрибутів зберігаємо значення в словник
            self._attributes[name] = value

    def __delattr__(self, name):
        """Викликається при видаленні атрибута"""

        print(f"[DELATTR] Deleting attribute '{name}'")
        if name in self._attributes:
            del self._attributes[name]
        else:
            # Якщо атрибут не знайдено, піднімаємо виключення
            raise AttributeError(f"Attribute '{name}' does not exist")


obj = LoggedObject()

obj.name = "Test Object"
obj.value = 42
print()
print(obj.name)
print(obj.value)
print()
print(obj.non_existent)
print()
del obj.name
print()
try:
    print(obj.name)
except AttributeError as e:
    print(f"Error: {e}")
print()
try:
    del obj.unknown
except AttributeError as e:
    print(f"Error: {e}")
print()
my_var = obj.value
print(my_var)
my_var2 = LoggedObject().name
print(my_var2)
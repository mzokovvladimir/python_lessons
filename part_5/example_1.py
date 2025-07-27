class Cat:
    count = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Cat.count += 1

    def _speak(self, value):
        return f"My name is {self._name} and I am {self._age} {value}"

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def __some_method(self):
        return 'some_method (Cat)'


class UpgrateCat(Cat):
    def __some_method(self):
        return 'some_method (UpgrateCat)'


my_cat = Cat("John", 36)
print(my_cat.get_name())
print(my_cat.get_age())
my_cat.set_age(25)
print(my_cat.get_age())
print(getattr(my_cat, '_Cat__some_method'))
print(my_cat.__dict__)
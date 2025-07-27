class MyClass:
    def __init__(self):
        self.__private_attr = 50

    @property
    def private_attr(self):
        return self.__private_attr

    @private_attr.setter
    def private_attr(self, value: int):
        if value < 0:
            raise ValueError('private_attr cannot be negative')
        self.__private_attr = value

    @private_attr.deleter
    def private_attr(self):
        del self.__private_attr


my_obj = MyClass()
print(my_obj.private_attr)
my_obj.private_attr = 5
print(my_obj.private_attr)
my_obj.private_attr = 15
print(my_obj.private_attr)
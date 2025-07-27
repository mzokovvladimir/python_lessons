class MyClass:
    def some_method(self):
        return f"123"


class MyClass2(MyClass):
    def some_other_method(self):
        return f"136"


class MyClass3(MyClass2):
    def some_other_method(self):
        return f"137"


class MyClass4(MyClass3, MyClass2):
    def some_other_method(self):
        return f"138"


my_obj1 = MyClass()
print(my_obj1.some_method())
my_obj2 = MyClass2()
print(my_obj2.some_method())
print(my_obj2.some_other_method())
my_obj3 = MyClass3()
print(my_obj3.some_other_method())
my_obj4 = MyClass4()
print(my_obj4.some_other_method())
print(MyClass4.__mro__)
print(MyClass4.mro())

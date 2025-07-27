class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class MyClass2(MyClass):
    pass


class MyClass3(MyClass):
    pass


class MyClass4(MyClass2, MyClass3):
    """Some text"""
    TYPE = 'MyClass4'


m_c1 = MyClass(1, 2)
m_c2 = MyClass2(10, 20)
print(m_c1)
print(type(m_c2))
print(type(MyClass))
print(isinstance(m_c1, MyClass))
print(isinstance(m_c2, MyClass))
print(isinstance(m_c1, MyClass2))
print(isinstance(m_c2, MyClass2))
print()
print(issubclass(MyClass, MyClass2))
print(issubclass(MyClass2, MyClass))
print()
print(MyClass4.__base__)
print(MyClass4.__bases__)
print(MyClass4.__mro__)
print(MyClass4.__name__)
print(m_c2.__dict__)
print(MyClass4.__dict__)
print(dir(MyClass4))
print(dir(m_c2))
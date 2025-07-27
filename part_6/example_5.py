class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


mc = MyClass(1, 3)
print(mc.__dict__)
print(MyClass.__dict__)
class MyClass:
    def __init__(self):
        self.x = 10

    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return super().__getattribute__(name)


obj = MyClass()
print(obj.x)
print(obj.y)

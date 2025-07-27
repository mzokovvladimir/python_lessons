class MyClass:
    def __init__(self):
        self.x = 10

    def __getattribute__(self, name):
        print(f"__getattribute__ called for {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f"__getattr__ called for {name}")
        return "default value"


obj = MyClass()
print(obj.x)
print(getattr(obj, 'y'))
print(getattr(obj, 'z', 'not found'))

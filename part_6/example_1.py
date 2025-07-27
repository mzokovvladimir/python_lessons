class MyClass:
    def __init__(self):
        self.x = 10


obj = MyClass()
print(getattr(obj, 'x'))  # 10
print(getattr(obj, 'y', 'default'))

class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        dct['greeting'] = lambda self: f"Hello, {self.name}!"
        return super().__new__(cls, name, bases, dct)


class Student(metaclass=CustomMeta):
    def __init__(self, name):
        self.name = name


student = Student("Max")
print(student.greeting())

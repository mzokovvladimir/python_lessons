class NameDescriptor:
    def __get__(self, instance, owner):
        print("__get__ called/name")
        return instance.__dict__.get("_name", None)

    def __set__(self, instance, value):
        print("__set__ called/name")
        if not isinstance(value, str):
            raise ValueError("Student value must be of type str")
        if not value.strip():
            raise ValueError("Student value must not be empty")
        instance.__dict__["_name"] = value.strip()

    def __delete__(self, instance):
        print("__delete__ called/name")
        raise AttributeError("Student cannot be deleted")


class AgeDescriptor:
    def __get__(self, instance, owner):
        print("__get__ called/age")
        return instance.__dict__.get("_age", None)

    def __set__(self, instance, value):
        print("__set__ called/age")
        if not isinstance(value, int):
            raise ValueError("Student value must be of type int")
        if value < 18:
            raise ValueError("Student value must be greater than 18")
        instance.__dict__["_age"] = value

    def __delete__(self, instance):
        print("__delete__ called//age")
        raise AttributeError("Student cannot be deleted")


class Student:
    name = NameDescriptor()
    age = AgeDescriptor()

    def __init__(self, name, age):
        print("__init__ called")
        self.name = name
        self.age = age

    # __slots__ = [name, age]

    def __str__(self):
        return f"{self.name} is {self.age} years old"


s1 = Student("John", 27)
print()
print(s1)
print()
print(s1.name)
print(s1.age)
"""s1.email = "<EMAIL>"
print(s1)
print(s1.email)"""

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if 18 < age < 100:
            self.__age = age

    def __str__(self):
        return f"{self.__name} is {self.__age} years old"


s1 = Student("John", 25)
print(s1.get_name())
print(s1.get_age())
print()
s2 = Student("Steave", 27)
print(s2.get_name())
print(s2.get_age())
print(s1, s2, sep="\n")

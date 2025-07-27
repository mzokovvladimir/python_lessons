class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 18 < value < 100:
            self.__age = value

    def __str__(self):
        return f"{self.__name} is {self.__age} years old"


s1 = Student("John", 25)
print(s1.name)
print(s1.age)
print()
s2 = Student("Steave", 27)
print(s2.name)
print(s2.age)
print(s1, s2, sep="\n")
s1.name = "Test name"
print(s1)

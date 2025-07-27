class MyClass:
    """Some text"""
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        """str"""
        return f"{self.surname}, {self.name}, {self.age}"

    @staticmethod
    def my_test():
        return 5


def test(x: str) -> str:
    return "My str is", x
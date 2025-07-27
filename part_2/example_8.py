def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"My decorator says: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def welcome_function(name: str) -> str:
    return f"Hello {name}!"


@my_decorator
def my_test_func():
    return "Hello World!"


print(welcome_function("Bob"))
print(my_test_func())
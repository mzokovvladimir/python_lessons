from decimal import Decimal


def my_round_decorator(digit):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            # print(f'My decorator says: {func.__name__}')
            return round(func(*args, **kwargs), digit)

        return wrapper

    return my_decorator


def my_type_decorator(cnt_type):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            # print(f'My decorator says: {func.__name__}')
            return cnt_type(func(*args, **kwargs))

        return wrapper

    return my_decorator


@my_type_decorator(Decimal)
@my_round_decorator(5)
def divide(x=10, y=20):
    return x / y


print(type(divide()), divide())

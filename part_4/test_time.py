import time


def format_round(digit=1):
    """Приклад створення декоратора з параметром"""
    def cast_decorator(function):
        """Сам декоратор"""
        def decorated_function(*args, **kwargs):
            start = time.time()
            result = function(*args, **kwargs)
            return f'Value: {result}\nDuration: {round(time.time() - start, digit)} sec'
        return decorated_function
    return cast_decorator


@format_round(2)
def my_sum(x):
    return sum(x)


my_list = list(range(10004124))
print(my_sum(my_list))

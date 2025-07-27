def custom_decorator(func):
    def decorator(*args, **kwargs):
        return list(filter(lambda x: x % 2 == 0, func(*args, **kwargs)))
    return decorator


@custom_decorator
def my_custom_func(my_nums):
    return list(map(int, my_nums.split()))


print(my_custom_func(input("Enter your numbers: ")))

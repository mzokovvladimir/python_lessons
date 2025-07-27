def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


print(factorial(5))
"""
1 2 3 4 
1 2 3 4 5
1 2 3 4 5 6 7 8 9 10 ...
"""
def my_gen(start, stop):
    for element in range(start, stop + 1):
        yield element


my_test_gen = my_gen(1, 7)
print(next(my_test_gen))
print(next(my_test_gen))
print(next(my_test_gen))
print(next(my_test_gen))
print(next(my_test_gen))
print(next(my_test_gen))
print(next(my_test_gen))
print(type(my_test_gen))
print(type(my_gen))
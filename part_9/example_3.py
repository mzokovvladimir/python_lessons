my_list = [1, 2, 3, 5, 7]
my_iter_obj = iter(my_list)
while True:
    try:
        print(next(my_iter_obj))
    except StopIteration:
        break
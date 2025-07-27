def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1


for num in count_up_to(5):
    print(num)


print(count_up_to(5))


my_test_list = [a for a in 'hello world!']
print(my_test_list)
my_test_gen = (a for a in 'hello world!')
print(list(my_test_gen))
print(my_test_gen)
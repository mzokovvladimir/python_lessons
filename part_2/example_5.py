from functools import reduce

my_list = [1, -2, 3, -10, 0]
print(list(filter(lambda digit: digit >= 0, my_list)))
my_text_d = input("Enter a numbers: ").split()
my_text_d_list = list(map(int, my_text_d))
print(sum(my_text_d_list))

product = reduce(lambda x, y: x + y, my_list)
print(product)

numbers = [1, -2, 3, -10, 0]
p = 0
for elem in numbers:
    p += elem
print(p)
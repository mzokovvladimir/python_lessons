text = input('Enter a string: ')
if not text:
    print('You did not enter a string.')
else:
    print(text)
print()
my_var = 'You did not enter a string.' if not text else text
print(my_var)
print('You did not enter a string.' if not text else text)
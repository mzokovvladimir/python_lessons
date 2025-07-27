count = 3
while count:
    login = input("Enter a number: ")
    password = input("Enter a password: ")
    count -= 1
    if login == 'admin' and password == 'admin':
        print('Welcome')
        break
else:
    print("exit")
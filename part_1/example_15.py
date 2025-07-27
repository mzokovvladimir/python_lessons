for count in range(3):
    login = input("Enter a number: ")
    password = input("Enter a password: ")
    if login == 'admin' and password == 'admin':
        print('Welcome')
        break
else:
    print("exit")
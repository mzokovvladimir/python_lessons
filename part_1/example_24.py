my_dict = {'Franco': ['book1', 'book2', 'book3'],}
print(my_dict['Franco'])
my_dict['Ukrainka'] = ['book21', 'book22', 'book23']
print(my_dict)
print(len(my_dict))
my_dict['Ukrainka'] = ['book31', 'book32', 'book33']
my_dict['Ukrainka'][1] = 'book34'
print(my_dict)
phonebook = {
    'Max': {
        'phone': '+380991659872',
        'exp': 3,
        'portfolio': ["ahjshgdfhjagsfdjhga", "jahkdgsfjhgasdjkfhgakjsdhfg"],
        'email': 'EMAIL@example.com',
    },
    'Ivan': {
        'phone': '+380991319872',
        'exp': 2,
        'portfolio': ["gdfhjagsfdjhga", "jahkdgsfjhga", "sdjkfhgakjsdhfg"],
        'email': 'EMAIL2@example.com',
    }
}
print(phonebook)
print(phonebook['Max']['email'])
print(type(phonebook['Ivan']['portfolio']))
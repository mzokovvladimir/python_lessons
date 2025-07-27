def test_function(some_text):
    global my_temp_str
    my_temp_str = my_temp_str.lower()
    return f'some_text: {my_temp_str}; {some_text}'


my_temp_str = input('Enter a string: ')
print(my_temp_str)
print(test_function(my_temp_str))
print(my_temp_str)
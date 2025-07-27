def test_function(name):
    if not name:
        return
    print(f'Hello, {name} !')

my_text = 'Some text'
test_function(my_text)
test_function()
test_function(my_text)
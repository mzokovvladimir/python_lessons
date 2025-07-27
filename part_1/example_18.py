text = input("Enter a sentence: ")
"""print(text.count('a'))
print(text.index('a'))
print(text.index('a'))
print(text.index('a', 2))
print(text.index('a', 4, 15))
print(text.find('b'))"""
if text.isdigit():
    print("This text contains numbers")
if text.isalpha():
    print("This text contains alphabets")
if text.isspace():
    print("This text contains space")
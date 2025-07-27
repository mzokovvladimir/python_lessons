class UpperCaseIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            some_char = self.text[self.index]
            self.index += 1
            if some_char.isupper():
                return some_char
        raise StopIteration


string_iter = UpperCaseIterator("HeLLo WoRLd")
for this_char in string_iter:
    print(this_char)

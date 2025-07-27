import re


string = "teSt1 test2 teSt3 test4 teSt5"
# re.subn(pattern, repl, string, count=0, flags=0)
# pattern - рядок шаблону регулярного виразу,
# repl - рядок заміни,
# string - рядок для пошуку,
# count=0 - максимальне число входжень pattern,
# flags=0 - один або декілька прапорців.
result = re.subn(r"s", "x", string, flags=re.IGNORECASE)
print(result)
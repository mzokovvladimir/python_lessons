from bs4 import BeautifulSoup
import re


result = ''
with open('index.html', encoding='UTF-8') as f:
    data = f.read()
    soup = BeautifulSoup(data, 'lxml')
    print(soup.html.text)
    print(type(soup.html.text))
    result = soup.html.text

print('Result is:', result)

phone_numbers = []
# phone_numbers += re.findall(r'\d{10}', result)
phone_numbers += re.findall(r'\d{3}-\d{3}-\d{2}-\d{2}', result)
print('phone_numbers is:', phone_numbers)

emails = []
emails += re.findall(r'\d+(\w+@\w+\.\w+)', result)
print('emails is:', emails)

from bs4 import BeautifulSoup
import re


result = ''
with open('index123.html', 'r', encoding='UTF-8') as f:
    data = f.read()

    # soup = BeautifulSoup(data, 'lxml')

    #print(type(soup.html.text))

    #result = soup.html.text
    result = data

print('\nResult is:', result)

phone_numbers = []
phone_numbers += re.findall(r'\d{3}-\d{3}-\d{2}-\d{2}', result)
print('Phone_numbers are:', phone_numbers)

emails = []
emails += re.findall(r'\w+@\w+.\w+', result)
print('Emails are:', emails)

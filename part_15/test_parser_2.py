from bs4 import BeautifulSoup
import requests as r


response = r.get('https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%80%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0'
                 '%BD%D0%B8%D0%B5')

soup = BeautifulSoup(response.text, 'lxml')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.title.parent)

# print(soup, end='\n\n')
# print(soup.prettify(), end='\n\n')

# print(soup.find('div', id="mw-page-base"), end='\n\n')

search_tags = soup.find_all('ul')
for element in search_tags:
    print(' '.join(element.text.split()))

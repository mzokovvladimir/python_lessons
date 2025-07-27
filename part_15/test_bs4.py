from bs4 import BeautifulSoup
import requests as r


response = r.get('https://alfavit.eu/index.php?route=product/category&path=_8')
print(response)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.title.parent)

# print(soup, end='\n\n')
# print(soup.prettify(), end='\n\n')

# print(soup.find('div'), end='\n\n')
search_tags = soup.find_all('p')
for element in search_tags:
    print(' '.join(element.text.split()))

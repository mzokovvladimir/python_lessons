from bs4 import BeautifulSoup
import requests as r

response = r.get(
    'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0')

# print(response)
soup = BeautifulSoup(response.text, 'lxml')
# print(end='\n\n\n')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.title.parent)
# print(soup, end="\n\n")
# print(soup.prettify(), end="\n\n")
# print(soup.find('div'), end="\n\n")
search_tags = soup.find_all("ul")
for element in search_tags:
    print(' '.join(element.text.split()))

div_content = soup.find('div', class_='vector-header-start')

if div_content:
    print(div_content.text.strip())
else:
    print("Div is not found.")
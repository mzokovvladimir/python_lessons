import requests
from bs4 import BeautifulSoup


with requests.get("http://python.org") as r:
    data = BeautifulSoup(r.text, "lxml")
    print(data.prettify())

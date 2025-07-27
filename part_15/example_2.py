"""
Цей модуль містить функції для парсингу сторінки новин і зберігання отриманих даних у JSON-файлі.

Модуль складається з таких функцій:
    - parse_news: парсить сторінку новин і отримує дані про заголовки новин та посилання на них.
    - save_to_json: зберігає дані про новини у JSON-файл.

Приклад використання:
    news_url = 'https://www.example.com/news'
    parsed_news = parse_news(news_url)
    save_to_json(parsed_news, 'news_data.json')
"""

import requests
from bs4 import BeautifulSoup
import json


def parse_news(url: str) -> list[dict[str, str]]:
    """
        Парсить сторінку новин і отримує дані про заголовки новин та посилання на них.

        Parameters:
            url (str): Посилання на сторінку новин.

        Returns:
            list[dict[str, str]]: Список словників, де кожен словник містить дані про заголовок новини та
            посилання на неї.
        """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_list = []
    for headline in soup.find_all('h2', attrs={'data-testid': 'card-headline', 'class': 'sc-4fedabc7-3 zTZri'}):
        news_title = headline.get_text(strip=True)
        news_link_element = headline.find_parent('a',
                                                 {'data-testid': 'internal-link'})  # Отримуємо елемент <a> з посиланням
        news_link = news_link_element['href'] if news_link_element else ''  # Отримуємо посилання з атрибута href
        news_list.append({'title': news_title, 'link': url + news_link})

    return news_list


def save_to_json(news_data, filename: str) -> None:
    """
        Зберігає дані про новини у JSON-файл.

        Parameters:
            news_data (list[dict]): Дані про новини у вигляді списку словників.
            filename (str): Назва файлу, у який будуть збережені дані.

        Returns:
            None
        """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(news_data, json_file, ensure_ascii=False, indent=4)


# Посилання на сайт новин, який будемо парсити
news_url = 'https://www.bbc.com'

parsed_news = parse_news(news_url)

# Збереження даних у JSON-файл
save_to_json(parsed_news, 'news_data.json')

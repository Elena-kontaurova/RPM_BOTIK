import requests
from bs4 import BeautifulSoup
import time

URL = f'https://pikabu.ru/community/mem/search'

def parser(url):
    ''' метод получения адреса'''
    response = requests.get(url, timeout=60)
    response.encoding = 'windows-1251'

    with open('html.log', 'w', encoding='utf-8') as f:
        f.write(response.text)

    bs = BeautifulSoup(response.text, 'html.parser')
    content = bs.find('div', class_='stories-feed__container')
    # tables = table.find_all('a')
    jokes = []
    for post in content.find_all('article'):
        story = post.find('div', class_='story-image__content')
        if story is None:
            continue
        img = story.find('img')
        if img is None:
            continue
        src = img.get('src')
        if src is None or src == '':
            continue
        jokes.append(src)
    return jokes

list_of_jokes = parser(URL)
print(list_of_jokes)

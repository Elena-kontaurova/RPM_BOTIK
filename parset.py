''' Файл для парсинга мемов'''
import requests
from bs4 import BeautifulSoup


URL = 'https://anekdoty.ru/'


def parser(url):
    ''' метод получения адреса'''
    response = requests.get(url, timeout=5)
    bs = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    table = bs.find_all('div', attrs={'class': 'holder-body'})
    jokes = []
    for i in table:
        dela = i.find_all('p')
        jokes.extend([c.text for c in dela])
    return jokes

list_of_jokes = parser(URL)

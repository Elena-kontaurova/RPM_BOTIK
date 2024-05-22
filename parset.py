''' Файл для парсинга мемов'''
import requests
from bs4 import BeautifulSoup


URL = 'https://topmemas.top/'


def parser(url):
    ''' метод получения адреса'''
    response = requests.get(url, timeout=60)
    bs = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    table = bs.find_all('div', attrs={'class': 'cont_item'})
    jokes = []
    for i in table:
        dela = i.find('source').get('srcset')
        mem = 'https://topmemas.top/' + dela
        jokes.append(mem)
        return jokes
list_of_jokes = parser(URL)
print(list_of_jokes)

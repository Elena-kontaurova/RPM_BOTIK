''' Файл для парсинга мемов'''
import random
import requests
from bs4 import BeautifulSoup


URL = 'https://anekdoty.ru/'


def parser(url):
    ''' метод получения адреса'''
    response = requests.get(url, timeout=5)


    bs = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')


    table = bs.find_all('div', attrs={'class': 'holder-body'})
    for i in table:
        dela = i.find_all('p')
        return [c.text for c in dela]

list_of_del = parser(URL)
random.shuffle(list_of_del)

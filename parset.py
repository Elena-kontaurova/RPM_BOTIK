''' Файл для парсинга мемов'''
import requests
from bs4 import BeautifulSoup


for i in range(11):
    URL = 'https://2fan.ru/meme-trendsmems?page={i}'


    def parser(url):
        ''' метод получения адреса'''
        response = requests.get(url, timeout=60)
        bs = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
        table = bs.find_all('div', attrs={'class': 'photo'})
        jokes = []
        for k in table:
            dela = k.find('img').get('src')
            jokes.append(dela)
        return jokes
    list_of_jokes = parser(URL)
    # print(list_of_jokes)

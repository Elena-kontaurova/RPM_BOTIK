from bs4 import BeautifulSoup
import requests

url = f'https://kartaslov.ru/книги/500_самых_свежих_анекдотов/1'
response = requests.get(url)
bs = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
texts = []

for elem in bs.find("div", attrs={'class': 'book-section'}).findAll():
    if elem["class"][0] == "book-sub-title":
        texts.append("")
    else:
        texts[-1] += elem.text

for text in texts:
    print(text)
    print()

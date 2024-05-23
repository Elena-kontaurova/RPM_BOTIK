''' Парсет сайта с мемами'''
import requests
from bs4 import BeautifulSoup
from bot.models import Image, Tag, ImageTag

async def parse_image(url):
    ''' метод получения адреса'''
    for page_number in range(1, 10):
        page_url = f'{url}?page={page_number}'
        # print(page_url)
        response = requests.get(page_url, timeout=60)
        response.encoding = 'windows-1251'

        bs = BeautifulSoup(response.text, 'html.parser')
        content = bs.find('div', class_='stories-feed__container')
        # tables = table.find_all('a')
        for post in content.find_all('article'):
            content = post.find('div', class_='story__content-wrapper')
            story = content.find('div', class_='story-image__content')
            if story is None:
                continue
            img = story.find('img')
            if img is None:
                continue
            link = img.get('src')
            if link is None or link == '':
                continue
            image, image_created = Image.get_or_create(url=link)
            for tag_a in content.find_all('a', class_='tags__tag'):
                tag_name = tag_a.text
                tag, _ = Tag.get_or_create(name=tag_name)
                if image_created:
                    ImageTag.create(image=image, tag=tag)

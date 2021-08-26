import string
import re
import requests
from bs4 import BeautifulSoup
import csv
import os

URL = 'https://cars.av.by/bmw'
HEADRS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
          'accept': '*/*'}
HOST = 'https://cars.av.by'
FILE = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADRS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = HOST + soup.find('a', class_='button--default').get('href')
    if pagination:
        return int(pagination[-1])
    else:
        return 1
    print(pagination)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='listing-item__wrap')
    cars = []
    for item in items:
        cars.append({'title': item.find('span', class_='link-text').get_text(),
                     'link': HOST + item.find('a', class_='listing-item__link').get('href'),
                     'city': item.find('div', class_='listing-item__location').get_text(),
                     'price': item.find('div', class_='listing-item__price').get_text().replace('\u2009', '').replace('\xa0р', ''),
                     })
    return cars


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Ссылка', 'Город', 'Цена'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['city'], item['price']])


def parse():
    URL = input('Vvedi URL: ')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count):
            print(f'Парсинг страницы {page} из {pages_count}')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        save_file(cars, FILE)
        print(f'Polucheno {len(cars)} auto')
        """Open file"""
        os.startfile(FILE)
    else:
        print('Error')

parse()



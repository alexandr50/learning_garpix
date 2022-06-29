import requests
import csv
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
def get_images(url):
    soup = bs(requests.get(url).content, 'html.parser')

    urls = []
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        urls.append(img_url)
        if not img_url:
            continue

    # pathname = 'C:\Users\79290\learning_garpix\learning_garpix\final_project'




    return urls, soup





print(get_images('https://stopgame.ru/news'))

from bs4 import BeautifulSoup
from bs4.element import Tag
import os
import requests
from datetime import datetime
import pandas as pd
URL = 'https://www.qwiklabs.com/public_profiles/319b29da-117c-48c7-9235-574c34e6e86e'
filename = 'Qwicklabs Web scraping/qwik.html'

if not os.path.isfile(filename):
    response = requests.get(URL)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
    del response

data = {
    'name': [],
    'date': [],
    'url': []
}

with open(filename, 'r') as f:
    bs = BeautifulSoup(f, 'html.parser')
    badges = bs.findAll(class_='profile-badge')
    for badge in badges:
        # badge:Tag =badge
        image_url = badge.find(class_='badge-image')['href'].strip()
        name = badge.find(class_='ql-subhead-1 l-mts').string.strip()
        date: str = badge.find(class_='ql-body-2 l-mbs').string.strip()[7:]
        date_t = datetime.strptime(date, '%b %d, %Y')
        data['name'].append(name)
        data['date'].append(date_t)
        data['url'].append(image_url)

df=pd.DataFrame(data=data)
print(df)
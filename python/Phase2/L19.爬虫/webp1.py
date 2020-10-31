# 403 Forbidden

import requests

url = 'https://maoyan.com/films?showType=3'
html = requests.get(url).text
print(html)
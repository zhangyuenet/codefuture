import requests

url = 'https://maoyan.com/films?showType=3&sortId=3'
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)"}
html = requests.get(url, headers=header).text
print(html)
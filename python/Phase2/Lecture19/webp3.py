import requests

url = 'https://maoyan.com/films?showType=3&sortId=3&offset='
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)"}
html = requests.get(url, headers=header).text
for i in range(0, 9):
	p_url = url + str(i * 30)
	print(p_url)
import requests
from lxml import etree

url = 'https://maoyan.com/films?showType=3&sortId=3&offset='
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)"}
html = requests.get(url, headers=header).text
data = etree.HTML(html)
maxpage = data.xpath('/html/body/div[4]/div/div[2]/div[3]/ul/li[7]/a/text()')[0]
for i in range(1, int(maxpage) + 1):
	p_url = url + str(i * 30)
	print(p_url)
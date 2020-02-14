import requests
from lxml import etree

url = 'https://maoyan.com/films?showType=3&sortId=3&offset='
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)"}
html = requests.get(url, headers=header).text

# 名称，评分，详情
data = etree.HTML(html)
names = data.xpath('//div[@class="channel-detail movie-item-title"]/@title')
infos = data.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')

print(len(names), names)
print(len(infos), infos)


# options 1
scores_int = data.xpath('//div[@class="channel-detail channel-detail-orange"]/i[@class="integer"]/text()')
scores_fra = data.xpath('//div[@class="channel-detail channel-detail-orange"]/i[@class="fraction"]/text()')
#scores_int2 = data.xpath('//i[@class="integer"]/text()')
#scores_fra2 = data.xpath('//i[@class="fraction"]/text()')

for i in range(0, len(scores_int) ):
	scores_int[i] = scores_int[i] + scores_fra[i]
print(len(scores_int), scores_int)

# options 2
scores = data.xpath('//div[@class="channel-detail channel-detail-orange"]')
scors = [x.xpath('string(.)') for x in scores]
print(len(scors), scors)





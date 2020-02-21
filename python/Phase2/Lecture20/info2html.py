#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from fake_useragent import UserAgent

url = 'https://maoyan.com/films?showType=3&sortId=3&offset='
ua = UserAgent()
header = {"User-Agent": ua.random}
html = requests.get(url, headers=header).text
# 名称，评分，详情
data = etree.HTML(html)
names = data.xpath('//div[@class="channel-detail movie-item-title"]/@title')
infos = data.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')

#print(len(names), names)
#print(len(infos), infos)

scores = data.xpath('//div[@class="channel-detail channel-detail-orange"]')
scors = [x.xpath('string(.)') for x in scores]
#print(len(scors), scors)

f = open('movielist.html', 'w')
f.write('<html><head><title>Movie List</title></head><body>')
f.write('<table border="1">')
f.write('<tr><th>name</th><th>url</th><th>score</th></tr>')# title
for i in range(0, len(names)):
	f.write('<tr>')
	f.write('<td>' + names[i] + '</td>')
	f.write('<td>' + infos[i] + '</td>')
	f.write('<td>' + scors[i] + '</td>')
	f.write('</tr>')
f.write('</table></body></html>')
f.close()







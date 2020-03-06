#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from fake_useragent import UserAgent
from matplotlib import pyplot as plt

url = 'https://www.worldometers.info/coronavirus/'
ua = UserAgent()
header = {"User-Agent": ua.random}
html = requests.get(url, headers=header).text
#获取数据
data = etree.HTML(html)
datalist = data.xpath('//table[@id="main_table_countries"]/tbody[1]/tr') # td[1]/text()
mylist = []
for countryitem in datalist:
	item = []
	name = countryitem.xpath('td[1]/text()')[0]
	if name == ' ':
		name = countryitem.xpath('td[1]/span/text()')[0]  #country name
	item.append(name)
	item.append(countryitem.xpath('td[2]/text()')[0]) # Total Cases
	item.append(countryitem.xpath('td[6]/text()')[0]) # Total Recovered
	mylist.append(item)

# print(mylist)

#draw
namelist = []
totallist = []
recoveredlist = [] 
for i in range(1,10):
	namelist.append(mylist[i][0])
	totallist.append(int(mylist[i][1].replace(',','')))
	recoveredlist.append(int(mylist[i][2].replace(',','')))


plt.bar(namelist, totallist, color = 'r', align = 'center')
plt.bar(namelist, recoveredlist, color = 'g' , width = 0.3, align = 'edge')
plt.title('Top 10')
plt.ylabel('numbers')
plt.xlabel('Country')
plt.show()













# https://www.worldometers.info/coronavirus/

# //*[@id="main_table_countries"]/tbody[1]/tr[1]/td[1]
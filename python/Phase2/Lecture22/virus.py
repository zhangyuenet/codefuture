#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from fake_useragent import UserAgent
from matplotlib import pyplot as plt

url = 'https://www.worldometers.info/coronavirus/'
#ua = UserAgent()
#header = {"User-Agent": ua.random}
#html = requests.get(url, headers=header).text

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)"}
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
	item.append(countryitem.xpath('td[4]/text()')[0]) # Total Deaths
	item.append(countryitem.xpath('td[6]/text()')[0]) # Active Cases
	item.append(countryitem.xpath('td[7]/text()')[0]) # Total Recovered
	
	mylist.append(item)

print(mylist)


#draw
namelist = []

deathlist = []
activelist = []
recoveredlist = []


for i in range(1,10):
	namelist.append(mylist[i][0])
	deathnum = mylist[i][1].replace(',','')
	if deathnum == ' ':
		deathnum = '0' 
	deathlist.append(int(deathnum))
	activelist.append(int(mylist[i][2].replace(',','')))
	recoveredlist.append(int(mylist[i][3].replace(',','')))


plt.bar(namelist, deathlist, color = 'r', align = 'center')
plt.bar(namelist, activelist, bottom = deathlist,  color = 'g' , align = 'center')
plt.bar(namelist, recoveredlist, bottom = activelist , color = 'b' , align = 'center')
plt.title('Top 10')
plt.ylabel('numbers')
plt.xlabel('Country')
plt.show()













# https://www.worldometers.info/coronavirus/

# //*[@id="main_table_countries"]/tbody[1]/tr[1]/td[1]
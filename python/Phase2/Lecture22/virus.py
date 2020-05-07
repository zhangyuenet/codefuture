#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from fake_useragent import UserAgent
from matplotlib import pyplot as plt


def ClearInt(str) :
	str = str.replace(',' , '')
	str = str.strip()
	if str == '':
		str = '0' 
	elif str == 'N/A':
		str = '0'

	return int(str)


url = 'https://www.worldometers.info/coronavirus/'
#ua = UserAgent()
#header = {"User-Agent": ua.random}
#html = requests.get(url, headers=header).text

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)"}
html = requests.get(url, headers=header).text

#获取数据
data = etree.HTML(html)
datalist = data.xpath('//table[@id="main_table_countries_today"]/tbody[1]/tr[not(contains(@class, "total_row_world"))]') # td[1]/text()
#print(len(datalist))
mylist = []
for countryitem in datalist:

	item = []
	nameitem = countryitem.xpath('td[1]/a/text()')
	if len(nameitem) >  0:
		name = nameitem[0]  #country name
	else:
		nameitem = countryitem.xpath('td[1]/span/text()')  # For diamond Princess
		if len(nameitem) > 0:
			name = nameitem[0]
	item.append(name)

	deathitem = countryitem.xpath('td[4]/text()')
	if len(deathitem) > 0:
		item.append(deathitem[0]) # Total Deaths
	
	activeitem = countryitem.xpath('td[7]/text()')
	if len(activeitem) > 0:
		item.append(activeitem[0]) # Active Cases
	
	recoveritem = countryitem.xpath('td[6]/text()')
	if len(recoveritem) > 0:
		item.append(recoveritem[0]) # Total Recovered
	
	mylist.append(item)

print(mylist)


#draw
namelist = []

deathlist = []
activelist = []
recoveredlist = []


for i in range(0,10):
	namelist.append(mylist[i][0])
	deathlist.append(ClearInt(mylist[i][1]))
	activelist.append(ClearInt(mylist[i][2]))
	recoveredlist.append(ClearInt(mylist[i][3]))


plt.bar(namelist, deathlist, color = 'r', align = 'center')
plt.bar(namelist, activelist, bottom = deathlist,  color = 'g' , align = 'center')
plt.bar(namelist, recoveredlist, bottom = activelist , color = 'b' , align = 'center')
plt.title('Top 10')
plt.ylabel('numbers')
plt.xlabel('Country')
plt.show()













# https://www.worldometers.info/coronavirus/

# //*[@id="main_table_countries"]/tbody[1]/tr[1]/td[1]
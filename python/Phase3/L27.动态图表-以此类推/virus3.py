#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA
# 国家/地区疫情数据可视化，
# Section3 实现动画

import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import sys


print('请稍后，准备数据...')
f = None


try:
	#获取程序所在路径。
	currentPath = os.path.split(sys.argv[0])[0]

	#根据程序所在路径获取数据文件的完整路径。
	filePath = os.path.join( currentPath, 'DXYArea-TimeSeries.json')
	print(filePath)
	f = open(filePath, 'r', encoding='UTF-8')
	#f = open('DXYArea-TimeSeries.json', 'r', encoding='UTF-8')

	df = pd.read_json(f.read())  #DataFrame
	
except Exception as e:
	print("Error: Load data failed: %s" % str(e))
finally:
	if f:
		f.close()


df = df[['provinceName','continentName','currentConfirmedCount', 'updateTime']]
# 解决日期问题
def number_to_date(number):
    localtime = time.localtime(number / 1000)
    return time.strftime("%Y-%m-%d", localtime)

#根据timestamp创建一列日期格式。
df['date'] = df['updateTime'].map(number_to_date)

# 每日上报数据，同一国家或地区的，只保留一个。
df = df.drop_duplicates(['provinceName', 'date'], keep='first', inplace=False)


fig, ax = plt.subplots(figsize=(15,8))
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

# 根据大洲进行分组显示
group_list = list(set(df.continentName))

color_list = ['#1DC59F','#4B1DC5','#C51D43','#97C51D', '#A01683', '#16A033' , '#A05916', '#165DA0']
group_color = dict(zip(group_list, color_list))
city_group = df.set_index('provinceName')['continentName'].to_dict()



def draw_by_date(aDay):
	dfshow = df[df.date == aDay].sort_values('currentConfirmedCount', ascending=False)
	dfshow = dfshow.head(20)
	
	ax.clear()
	ax.barh(dfshow['provinceName'], dfshow['currentConfirmedCount'], color=[group_color[city_group[city]] for city in dfshow['provinceName']])
	ax.text(1, 0.4, aDay, transform=ax.transAxes, color='#777777', size=30, ha='right', weight=800)
	for i, (value, name) in enumerate(zip(dfshow['currentConfirmedCount'], dfshow['provinceName'])):
		ax.text(value + 100, i, f'{value:,.0f}', size=12, weight=600, ha='left', va='center')


# 绘图
# 获取日期字符列表
datelist = df[df.provinceName == '湖北省']['date'].values
datelist.sort()


ani = animation.FuncAnimation(fig, draw_by_date, frames = datelist, interval=100,  repeat=False)
plt.show()

# brew install imagemagick
# ani.save('virus_animation.gif', writer='imagemagick')






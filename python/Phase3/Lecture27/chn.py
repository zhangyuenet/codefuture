#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA
# 中国城乡人口数据变化
# Section3 实现动画

import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import sys

print('请稍后，准备数据...')
currentPath = os.path.split(sys.argv[0])[0]
filePath = os.path.join( currentPath, 'chn.csv')
print(filePath)
df = pd.read_csv(filePath);



# 根据大洲进行分组显示
group_list = list(set(df.Name)) #显然是按照Name进行分类显示。也就是“城镇人口”和“乡村人口”

color_list = ['#1DC59F','#4B1DC5'] # 就剩下两类数据，所以保留两个颜色就够了。
group_color = dict(zip(group_list, color_list))


fig, ax = plt.subplots(figsize=(10,2))
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

def draw_by_date(aYear):
	aYear = str(aYear) #把年份从整数转换成字符串
	dfshow = df[['Name',aYear]]
	
	ax.clear()
	ax.barh(dfshow['Name'], dfshow[aYear], color=[group_color[name] for name in dfshow['Name']])
	ax.text(1, 0.4, aYear, transform=ax.transAxes, color='#777777', size=30, ha='right', weight=800)
	for i, (value, name) in enumerate(zip(dfshow[aYear], dfshow['Name'])):
		ax.text(value + 100, i, f'{value:,.0f}', size=12, weight=600, ha='left', va='center')
	

# 绘图
# 获取日期字符列表
datelist = range(1960, 2019)

ani = animation.FuncAnimation(fig, draw_by_date, frames = datelist, interval=100,  repeat=False)
plt.show()

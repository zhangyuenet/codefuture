#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA
# 国家/地区疫情数据可视化

import json
import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation


try:
    # 获取发病数最多的二十个国家/地区。
    f_area = open('DXYArea.json', 'r')
    vdata = json.loads(f_area.read())

    df_area = pd.read_json(json.dumps(vdata['results']))
    df_area = df_area.sort_values(
        'currentConfirmedCount', ascending=False)
    df_area = df_area.head(20)
    namelist = df_area["provinceName"].values

    print(namelist)
except:
    print("Error: Load data failed.")
finally:
    f_area.close()

try:
    f = open('DXYArea-TimeSeries.json', 'r')
    df = pd.read_json(f.read())
    df = df[['provinceName', 'continentName',
             'currentConfirmedCount', 'updateTime']]
    df = df[df['provinceName'].isin(namelist)].sort_values(
        'updateTime', ascending=True).sort_values('currentConfirmedCount', ascending=False)
except:
    print("Error: Load data failed.")
finally:
    f.close()


# 解决日期问题
def number_to_date(number):
    localtime = time.localtime(number / 1000)
    return time.strftime("%Y-%m-%d", localtime)

#根据timestamp创建一列日期格式。
df['date'] = df['updateTime'].map(number_to_date)
# 简单起见，每日上报数据，同一国家或地区的，只保留一个。
df = df.drop_duplicates(['provinceName', 'date'], keep='first', inplace=False)
#df[df.provinceName == "湖北省"].to_csv('italy.csv')

#过滤掉湖北省没有数据的情况
df = df[df.currentConfirmedCount > 0]


fig, ax = plt.subplots(figsize=(15,8))
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#plt.style.use("ggplot")

# 根据大洲进行分组显示
group_list = list(set(df.continentName))
color_list = ['#FF3366','#B88A00','#FFCC33','#CC33FF', '#1DC59F']
group_color = dict(zip(group_list, color_list))
city_group = df.set_index('provinceName')['continentName'].to_dict()


# 绘制某一日的图像
def draw_by_date(aDay):
    ax.clear()
    dfshow = df[df.date == aDay].sort_values('currentConfirmedCount', ascending=False)
    #print(dfshow)
    ax.barh(dfshow['provinceName'], dfshow['currentConfirmedCount'], color=[group_color[city_group[city]] for city in dfshow['provinceName']])
    ax.text(1, 0.4, aDay, transform=ax.transAxes, color='#777777', size=30, ha='right', weight=800)
    dx = dfshow['currentConfirmedCount'].max() / 200
    for i, (value, name) in enumerate(zip(dfshow['currentConfirmedCount'], dfshow['provinceName'])):
        ax.text(value + dx, i, f'{value:,.0f}', size=12, weight=600, ha='left', va='center')


# 绘图
# 获取日期字符列表
datelist = df[df.provinceName == namelist[0]]['date'].values
datelist.sort()

ani = animation.FuncAnimation(fig, draw_by_date, frames = datelist, interval=100, blit=False, repeat=False)
plt.show()

#  brew install imagemagick
ani.save('virus_animation.gif', writer='imagemagick')
#ani.save('virus_animation.gif', fps=20, writer='pillow')

#writer = PillowWriter(codec='h264')
#ani.save('virus.gif', writer=writer)


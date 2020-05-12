#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA
# 国家/地区疫情数据可视化
# Section1

import pandas as pd
import time
import matplotlib.pyplot as plt

try:
	f = open('DXYArea-TimeSeries.json', 'r')
	df = pd.read_json(f.read())  #DataFrame
except:
	print("Error: Load data failed.")
finally:
	f.close()

df = df[['provinceName','currentConfirmedCount', 'updateTime']]
# 解决日期问题
def number_to_date(number):
    localtime = time.localtime(number / 1000)
    return time.strftime("%Y-%m-%d", localtime)

#根据timestamp创建一列日期格式。
df['date'] = df['updateTime'].map(number_to_date)

# 举例：查看加拿大的数据
canada = df[df['provinceName'] == "加拿大"]
print(canada)

canada0420 = df[df['date'] == '2020-04-16'][df['provinceName'] == '加拿大']
print(canada0420)

# 每日上报数据，同一国家或地区的，只保留一个。
df = df.drop_duplicates(['provinceName', 'date'], keep='first', inplace=False)

# 举例：查看加拿大的数据
canada0420 = df[df['date'] == '2020-04-16'][df['provinceName'] == '加拿大']
print(canada0420)


fig, ax = plt.subplots(figsize=(15,8))
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签


dfshow = df[df.date == '2020-04-16'].sort_values('currentConfirmedCount', ascending=False)
dfshow = dfshow.head(20)
#print(dfshow)
ax.barh(dfshow['provinceName'], dfshow['currentConfirmedCount'])
ax.text(1, 0.4, '2020-04-16', transform=ax.transAxes, color='#777777', size=30, ha='right', weight=800)
for i, (value, name) in enumerate(zip(dfshow['currentConfirmedCount'], dfshow['provinceName'])):
	ax.text(value + 100, i, f'{value:,.0f}', size=12, weight=600, ha='left', va='center')
plt.show()




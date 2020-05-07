#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA
# 国家/地区疫情数据可视化
# Section1

import pandas as pd
import json
import time

try:
	f = open('DXYArea-TimeSeries.json', 'r')
	df = pd.read_json(f.read())  #DataFrame
except:
	print("Error: Load data failed.")
finally:
	f.close()


print(len(df))
print(df.columns)
print(df.values[1])
df = df[['provinceName','currentConfirmedCount', 'updateTime']]
print(df.columns)
print(df.values[1])
# 解决日期问题
def number_to_date(number):
    localtime = time.localtime(number / 1000)
    return time.strftime("%Y-%m-%d", localtime)

#根据timestamp创建一列日期格式。
df['date'] = df['updateTime'].map(number_to_date)
print(df.values[1])

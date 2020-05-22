#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA
# 国家/地区疫情数据可视化
# Section1

import pandas as pd
import time
import os
import sys

f = None

try:
	#获取程序所在路径。
	currentPath = os.path.split(sys.argv[0])[0]
	#根据程序所在路径获取数据文件的完整路径。
	filePath = os.path.join( currentPath, 'DXYArea-TimeSeries.json')
	print(filePath)
	f = open(filePath, 'r', encoding='UTF-8')
	
	df = pd.read_json(f.read())  #DataFrame
	
except Exception as e:
	print("Error: Load data failed: %s" % str(e))
finally:
	if f:
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

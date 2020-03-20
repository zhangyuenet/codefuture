#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA
# 根据国家/地区名称返回疫情数据

import json
import time

result = {}

country = input("请输入一个国家名称：")

try:
    f = open('DXYArea-TimeSeries.json' , 'r')
    vdata = json.loads(f.read())
    for data in vdata :
        if data["provinceName"] == country:
            localtime = time.localtime(data["updateTime"] / 1000)
            dt = time.strftime("%Y-%m-%d",localtime)
            result[dt] = data["confirmedCount"]
except:
    print("Error: Load data failed.")

finally:
    f.close()


for key in result.keys():
    print("%s : %s \r\n" % ( key , result[key]))


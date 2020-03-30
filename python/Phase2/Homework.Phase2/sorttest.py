#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from CodeFuture@CA

#对一个dict进行排序的例子
mydict = {'萨尔瓦多':1, '西班牙': 5, '格陵兰': 3, '巴拉圭': 2}
#准备一个空list。
datalist = []
for key in mydict.keys():
    #将dict的每一对key:value反过来保存成一个列表：包含两个元素：【value, key】,再存入list
    datalist.append([mydict[key], key])
#对列表进行排序
datalist.sort(reverse = True)
#再将列表中的数据放回到一个dict中。
newdict = {}
for item in datalist:
    newdict[item[1]] = item[0]
print(newdict)
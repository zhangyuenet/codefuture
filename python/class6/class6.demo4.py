#!/usr/bin/env python3
# -*- coding: utf-8 -*-

index = int(input('请输入一个行号：'))

f = open('test.txt', 'r')
result = f.readlines() 
f.close()
print(result[index-1])
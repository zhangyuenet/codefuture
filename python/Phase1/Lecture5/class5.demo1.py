#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = ['Tom', 'Jerry']
score = [85, 90]

num = len(name)
n = 0
while(n < num):
	print(name[n] + ':' + str(score[n]) )
	n = n + 1

print('=======================================')


result = {'Tom':85, 'Jerry':90}
for name in result:
	print(name + ':' + str(result[name]))

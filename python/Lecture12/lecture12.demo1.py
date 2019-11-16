#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## ==========================
# L2-5 Python基础4
f = open('scores.txt','r')
alist = []
for line in f.readlines():
	# strip()可以吧一行文字中前后的空格和一些换行符号去掉。
    alist.append(int(line.strip()))
f.close()
# print(alist)

## =========================
Ascored = alist[0] * 3 + alist[1] * 2 + alist[2]
Bscored = alist[3] * 3 + alist[4] * 2 + alist[5]
## ==========================
## L2-2 Python基础1
if Ascored > Bscored :
	print('A')
elif Ascored < Bscored :
	print('B')
else:
	print('T')


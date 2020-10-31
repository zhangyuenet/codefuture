#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# multi-thread SQL example
# CodeFuture@CA

# 导入socket库:
import threading
import time
import mysql.connector
import random
import sys

H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
index = 0

def loop(items):
    print('thread %s is running...' % threading.current_thread().name)
    i = 0
    while i < 10:
        name = ''.join(random.sample(H, 5))
        print(name)
        i = i + 1
        time.sleep(1)
    
    print('thread %s is finished.' % threading.current_thread().name)

threadList = []

MAX_TRD = 3 # 最多允许同时运行的线程数
if len(sys.argv) == 2:
    MAX_TRD = int(sys.argv[1])

while True:
    trdCount = threading.activeCount()
    print('当前执行线程数：%s' % (trdCount,))
    if  trdCount > MAX_TRD:
        time.sleep(5)
        continue

    t = threading.Thread(target=loop, args=(index,), name='WorkThread' + str(index))
    t.start()
    threadList.append(t)
    index = index + 1
    if index > 20:
        break

for t in threadList:
    t.join()

print('程序结束。')
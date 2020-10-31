#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# multi-thread SQL example
# CodeFuture@CA

# 导入socket库:
import threading
import time
import mysql.connector
import random

H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
index = 0

def loop(items):
    print('thread %s is running...' % threading.current_thread().name)
    conn = mysql.connector.connect(host='dev.huic.cloud', user='test', port=3300, passwd='test', database='huicyp', auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    i = 0
    while i < 100:
        name = ''.join(random.sample(H, 5))
        print(name)
        age = items + i 
        cursor.execute('INSERT INTO a_demo(`name`,age) VALUES(%s,%s)', [name, age])
        #conn.commit()
        i = i + 1
    conn.commit()
    
    cursor.close()
    conn.close()
    print('thread %s is finished.' % threading.current_thread().name)

threadList = []
while True:
    t = threading.Thread(target=loop, args=(index,), name='WorkThread' + str(index))
    t.start()
    threadList.append(t)
    index = index + 1
    time.sleep(1)
    if index > 5:
        break

for t in threadList:
    t.join()

print('程序结束。')
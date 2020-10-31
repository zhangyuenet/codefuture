#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# multi-thread SQL example
# CodeFuture@CA

# 导入socket库:
import threading
import time


index = 0

def loop(items):
    print('thread %s is running...' % threading.current_thread().name)
    time.sleep(5)
    print('thread %s is finished.' % threading.current_thread().name)

while True:
    t = threading.Thread(target=loop, args=(index,), name='WorkThread' + str(index))
    t.start()
    index = index + 1
    time.sleep(1)
    if index > 5:
        break


print('程序结束。')
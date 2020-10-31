#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# UDP Server example
# CodeFuture@CA

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    time.sleep(1)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)


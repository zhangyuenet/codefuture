#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# UDP  contacts server example
# CodeFuture@CA

# 导入socket库:
import socket
import time

contacts = {}


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
print('UDP contact server started...')

while True:
    # 接受一个新连接:
     # 接收数据:
    data, addr = s.recvfrom(1024)
    time.sleep(1)
    print('Received from %s:%s.' % addr)
    #s.sendto(b'Hello, %s!' % data, addr)
    arg = data.decode('utf-8').split(';')
    if arg[0] == 'add':
        contacts[arg[1]] = arg[2]
        s.sendto(('%s added' % arg[1]).encode('utf-8'), addr)
    elif arg[0] == 'remove':
        if arg[1] in contacts :
            contacts.pop(arg[1])
            s.sendto(('%s removed' % arg[1]).encode('utf-8'), addr)
        else:
            s.sendto('Not found'.encode('utf-8'), addr)
            
    elif arg[0] == 'find':
        if arg[1] in contacts:
            s.sendto(contacts[arg[1]].encode('utf-8'), addr)
        else:
            s.sendto('Not found'.encode('utf-8'), addr)
    print(contacts) #在服务端显示当前存储的数据












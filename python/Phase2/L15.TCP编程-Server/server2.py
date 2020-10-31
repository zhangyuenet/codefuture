#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# single thread contacts server example
# CodeFuture@CA

# 导入socket库:
import socket
import time

contacts = {}

def worker(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        arg = data.decode('utf-8').split(';')
        if arg[0] == 'add':
            contacts[arg[1]] = arg[2]
            print(contacts) #在服务端显示当前存储的数据
            sock.send(('%s added' % arg[1]).encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    worker(sock, addr) 


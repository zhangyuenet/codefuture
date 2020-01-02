#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
s.send((';'.join(sys.argv[1:])).encode('utf-8'))
print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

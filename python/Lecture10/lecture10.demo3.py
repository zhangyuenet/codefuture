#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code from: https://docs.python.org/zh-cn/3/library/turtle.html

from turtle import *
speed(0)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


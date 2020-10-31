#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *
import math

color('blue')
width(2)
# X轴
goto(0,0)
pendown()
goto(100,0)
penup()
# Y轴
goto(0,-30)
pendown()
goto(0,30)
penup()

goto(0,0)
color('red')
pendown()


x = 0
y = 0
while x < 10:
	y = math.sin(x)
	goto(x * 10  ,y * 20)
	x = x + 0.1
	
penup()
done()
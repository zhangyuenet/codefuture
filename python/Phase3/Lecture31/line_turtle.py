#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtle import *

color('blue')
width(2)
# X轴
goto(0,0)
pendown()
goto(100,0)
penup()
# Y轴
goto(0,0)
pendown()
goto(0,100)
penup()

goto(0,0)
color('red')
pendown()

goto(20,15)
goto(40,30)
goto(60,70)
goto(80,62)


penup()
done()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a module demo from Code Future'

__author__ = 'Code Future'

from turtle import *

def Draw(number, length):
	width(2)
	pencolor('blue')
	if number < 3:
		return
	angle = 360 / number
	for i in range(number):
		forward(length)
		right(angle)

	done()
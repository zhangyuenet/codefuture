#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
y1 = 2 * x + 1 
y2 = x * x
y3 = -2 * x + 1



plt.subplot(2, 2, 1) # 一行两列布局的图，且现在画的是左图
plt.plot(x,y1, color='r', linestyle='-', linewidth=1, label='2x+1')
plt.legend(loc='best')
plt.grid(color="y", linestyle=":")
plt.xlabel("x")
plt.ylabel("y1")

plt.subplot(2, 2, 2) # 一行两列布局的图，且现在画的是右图
plt.plot(x,y2, color='b', linestyle=':', linewidth=1, label='x*x')
plt.legend(loc='best')
plt.grid(color="y", linestyle=":")
plt.xlabel("x")
plt.ylabel("y2")


#plt.subplot(2, 2, 3) # 二行一列布局的图，且现在画的是整体
plt.subplot(2, 1, 2)
plt.plot(x,y3, color='m', linestyle='-', linewidth=1, label='-2x+1')
plt.legend(loc='best')
plt.grid(color="y", linestyle=":")
plt.xlabel("x")
plt.ylabel("y3")


plt.show()
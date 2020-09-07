#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
y1 = 2 * x + 1 
y2 = x * x

plt.axis([-5,5,-20,30])
# plt.axis(-5,5,-20,30) # error example

plt.xticks([x for x in range(-10,10)])
plt.yticks([x * 2 for x in range(-10,15)])

plt.grid(color="y", linestyle=":")

plt.plot(x,y1, color='r', linestyle='-', linewidth=1, label='2x+1')
plt.plot(x,y2, color='b', linestyle=':', linewidth=1, label='x*x')

#plt.legend()
#plt.legend(loc='lower right')
plt.legend(loc='best')

plt.show()


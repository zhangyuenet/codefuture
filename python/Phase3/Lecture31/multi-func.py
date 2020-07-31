#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
y1 = 2 * x + 1 
y2 = x * x

plt.plot(x,y1, color='r', linestyle='-', linewidth=1)
plt.plot(x,y2, color='b', linestyle=':', linewidth=1)

plt.show()


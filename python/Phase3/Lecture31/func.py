#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
#y = 2 * x + 1
#y = x * x * x
y = np.sin(x)

plt.plot(x,y, color='r', linestyle='-', linewidth=1)
plt.show()

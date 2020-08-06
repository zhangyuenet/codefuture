#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 1)
print(x)
y = 2 * x + 1
print(y)

plt.plot(x,y, color='r', linestyle='-',marker="*", linewidth=1)
plt.show()

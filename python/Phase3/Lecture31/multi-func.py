#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
a1 = x * x * x
b = x * x

plt.plot(x,a1, color='r', linestyle='-', linewidth=1)
plt.plot(x,b, color='b', linestyle=':', linewidth=1)

plt.show()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
 
plt.figure()
#拟合点
x0 = [1, 2, 3, 4, 5]
y0 = [1, 3, 8, 18, 36]
#绘制散点
plt.scatter(x0, y0, 25, "red")

plt.title("fit theory")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
 
#直线方程函数
def f_1(x, A, B):
    return A*x + B
 
plt.figure()
#拟合点
x0 = [1, 2, 3, 4, 5]
y0 = [1, 3, 8, 18, 36]
#绘制散点
plt.scatter(x0, y0, 25, "red")

#直线拟合与绘制
A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
x1 = np.arange(0, 6, 0.01)
y1 = A1*x1 + B1
#y1str = ('%sx+%s' % (A1,B1))
y1str = '{:.2f}x{:+.2f}'.format(A1,B1)
plt.plot(x1, y1, color='b', label=y1str)

plt.title("fit theory")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

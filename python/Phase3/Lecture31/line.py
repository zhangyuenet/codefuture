#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

x = [20, 40, 60, 80]
y = [15, 30, 70, 62]

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.xlabel('人数')
plt.ylabel('分数')
plt.plot(x, y, color="m", linestyle="--", marker="*", linewidth=1.0)

plt.savefig("line.jpg")
plt.show()
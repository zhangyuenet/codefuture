# L2-9 Turtle 绘图

## 教学目标
- 学会使用Turtle绘制函数曲线
- 继续复习使用组件
- 作业：；

## 教学设计

### 引入
有一门专门为少年儿童开发的编程语言，叫做Logo。
Logo最吸引人的功能，是它内置了一套海龟绘图（Turtle Graphics）系统。通过向海龟发送命令，用户可以直观的学习程序的运行过程，也可以用于数学教学。
我们打开Logo的海龟绘图，[https://turtleacademy.com/playground][1]
尝试一下下面的代码：
```python
forward 100 
right 90 
forward 100 
right 90 
forward 100 
right 90 
forward 100
```

我们得到了一个正方形。这和我们之前在Scratch中画图非常类似。只不过我们不是用积木而是用了代码。

### 基本绘图

Python为了让大家也能用上这样简单的绘图工具，在自己的安装程序中预装了一套海龟绘图。上面的命令都能用。我们试试看下面的Python代码(demo1)：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *

# 设置宽度:
width(4)


pencolor('blue') # 颜色
forward(100) # 前进
right(90) # 转向

pencolor('Yellow')
forward(100)
right(90)

pencolor('Red')
forward(100)
right(90)

pencolor('Green')
forward(100)
right(90)

```

运行完成后，窗口自动关闭。这时候，我们可以用下面的指令，要求窗口不要关闭，除非我们手动关闭它：
```python
# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
```

还可以用speed()来控制速度：
```python
# 设置动画速度 1速度低-10速度高
speed(10)
speed(0) # 0表示无动画
```
也可以用字符来描述速度，它和数字的对应关系如下：
"fastest": 0 最快
"fast": 10 快
"normal": 6 正常
"slow": 3 慢
"slowest": 1 最慢
也就是说：
```python
speed('normal') 等价于 speed(6)
```

我们可以使用命令来设置填充（demo2）：
```python
color('red', 'green')
begin_fill() #开始填充
circle(100)
end_fill() # 结束填充

circle(50)
```

仅仅依靠这些基本的指令，我们就可以绘制出一些意想不到的图像，例如(demo3)：
```python
from turtle import *
speed(0)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
```

大家有兴趣，可以自己绘制出很多很有意思的图像。如果需要查看一些命令的用法，可以去文档查看：
[https://docs.python.org/3.7/library/turtle.html][2]


### 学生练习
下面大家来做一个练习：
如图（pic1），如果上过我们的入门课，应该在code.org中画过这幅图。大家尝试一下用python来实现（20分钟）。
![][image-1]
【提示】如果学生完成情况较差，则给大家提示scratch算法，出示pic1.1图片。
![][image-2]

### 绘制数学函数
大家看到了我们刚才画出的图线其实都是直线。如果需要画曲线应该怎么做呢？我们先来看一个例子（demo4）：
```python
from turtle import *
import math

color('blue')
width(2)
# X轴
goto(0,0)
pendown()
goto(100,0)
penup()
# Y轴
goto(0,-30)
pendown()
goto(0,30)
penup()

goto(0,0)
color('red')
pendown()

x = 0
y = 0
while x < 10:
	y = math.sin(x)
	goto(x * 10  ,y * 20)
	x = x + 0.1
	
penup()
done()
```

大家看看运行的效果，我们得到了一个正弦曲线。
可是，这个曲线的获得，我们都是用goto得到的，也就是说，我们实际上用了一个个小的直线段做出了一条曲线。如果放大来看，实际上它们是由直线一段段组成的。这是一个重要的方法，我们可以用大量的、很短的、带有角度变换的直线段，连起来表示一条曲线。

这个例子中，也给大家说明了如何利用pendown()和penup()来控制绘图。简单来说，pendown()后，我们就会在屏幕上留下线条，而penup()后，相当于我们抬起了笔，这时候移动画笔，就不会在屏幕上留下印记了。所以我们使用程序绘图时，非常接近我们用手工绘图的场景，需要告诉计算机，在移动画笔时，笔是否与画布（纸）接触。

另外需要注意到的，我们在代码中引用了另外一个模块math。
Math中包含了非常多的数学相关的函数，有兴趣的同学可以查阅一下：
[https://docs.python.org/3.7/library/math.html?highlight=math#module-math][3]
如果其中有些学术名词搞不清楚，可以参考中文的版本。

这里要和大家解释一下，我们今天用turtle画了一个数学函数的曲线。但实际上，Python会有一个特别棒的模块专门来画各种数学函数曲线。我们以后会学到。

## 作业
今天在课堂上老师给大家展示了一个数学方程式的曲线：
```python
y = sin(x)
```
那么，请同学们尝试自己画一下下面这个数学函数的曲线：
```python
y = x * x
```
如果学过，我们应该很熟悉它的曲线形状。是一个针对Y轴对称的曲线。大家比拼一下，如何让自己画出来的曲线看上去很漂亮。

【补充题】今天老师在绘制曲线时，只是简单的画了一横一竖两条直线代表X轴和Y轴，但是在数学中，如果画坐标轴，需要加上箭头，还需要用文字标示出“X”和“Y”。你们可以在你们的图形中做到么？








[1]:	https://turtleacademy.com/playground
[2]:	https://docs.python.org/3.7/library/turtle.html
[3]:	https://docs.python.org/3.7/library/math.html?highlight=math#module-math

[image-1]:	lecture10.pic1.png
[image-2]:	https://github.com/zhangyuenet/codefuture/blob/master/python/Lecture10/lecture10.pic1.1.png
# L2-2 Python基础1 - 教学设计
## 教学目标
1. 掌握基本语法（注释，缩进，大小写）；
2. 掌握基本数据类型；
3. 数字的基本运算；
4. input（）；
5. 变量和赋值；
6. 布尔值
7. 条件语句

## 课程导入
我们在编程基础课中，学到过如下的概念，大家简单回忆一下：
- 循环；
- 条件；
- 变量；
- 函数；
- 事件；
- 函数参数；
- 二进制数及换算；
- 调试Debug；

所有的概念，在这几次的课上，我们都会涉及到。让大家了解一下，用Python如何实现我们之前在积木中实现的功能。

## 课程设计

### 基本语法
我们先学会Python的基本语法。先看第一个程序(demo1)：
```python
# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
```
大家通过阅读代码，应该能够清楚的看出它实现的功能。
与Scratch积木不同，Python使用英文字母、符号和数字等组合来编写程序，我们称之为**“代码”**。
Python代码有这样几个最基本的规则：
- 以“#”开头的语句称为**“注释”**，注释是给人看的，机器不在乎，所以可以在注释中随意写入内容。
- 大小写敏感，**print**和**Print**是不同的；
- **“缩进”**是Python的一个重要语法特点；当语句以**“冒号:”**结尾时，缩进的语句视为代码块。
为了更好的理解“缩进”。我们看看如下的代码运行情况：
```python
# print absolute value of an integer:
a = 100
if a >= 0:
print(a)
else:
print(-a)
```
运行后的错误提示：
```bash
  File "/Users/yuezhang/OneDrive/WIP/Kits_Program/codefuture/codefuture/python/class2/class2.demo1.py", line 4
    print(a)
        ^
IndentationError: expected an indented block
[Finished in 0.1s with exit code 1]
[cmd: ['/usr/local/bin/python3', '-u', '/Users/yuezhang/OneDrive/WIP/Kits_Program/codefuture/codefuture/python/class2/class2.demo1.py']]
[dir: /Users/yuezhang/OneDrive/WIP/Kits_Program/codefuture/codefuture/python/class2]
[path: /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin]
```

### 基本数据类型
大家看看如下数据，都是Python支持的基本数据类型（demo2）：
```python
a = 100
b = 100.25
c = -50.90
d = 0xff00
e = 0b1011
f = 1.2e5
g = 1.2e-2
h = "hello"
i = 'world'
j = ''' hello
world
! '''
```

Python可以处理任意大小的整数。在这里面不同特别在意。这是很棒的一点。在很多其他编程语言中，必须考虑你所使用的变量是否会出现超出限制的问题。Python在这一点上很简单。
100.25这样的数据在计算机中被称为浮点数。浮点数在Python中支持科学计数法。
字符串可以用’’或者“”（两者具体的差别下节课会讲到），以及分行的’’’ ‘’’。

### 关于变量的命名
看看这些命名，那些觉得好，那些觉得不好？（demo3）

```python
我的总金额 = 0			  # 用中文也没问题

price_count_reader = 0 	  # 无缩写
num_errors = 0            # "num" 是一个常见的写法
num_usb_connections = 0   # 人人都知道 "USB" 是什么

n = 0                     # 毫无意义.
nerr = 0                  # 含糊不清的缩写.
n_comp_conns = 0          # 含糊不清的缩写.
wgc_connections = 0       # 只有贵团队知道是什么意思.
pc_reader = 0             # "pc" 有太多可能的解释了.
cstmr_id = 0              # 删减了若干字母.

person_name =""
personName = ""
personname = ""			  #容易拼写错误
```

用中文当然也可以！但是大家想想，用中文会有什么问题？
其他的命名，老师为大家讲解优劣。
有兴趣的同学，请用搜索引擎尝试去搜索：“程序变量命名原则”，看看各种说法，选择你喜欢的方式。

### 赋值
需要说明的是，如下的代码：
```python
a = 'ABC'
```
这里的“等号=”和数学中的等号不是一个概念。这里的“=”称为赋值。赋值操作完成如下的工作：
1. 在内存中创建了一个'ABC'的字符串；
2. 在内存中创建了一个名为a的变量，并把它指向'ABC'。
顺便说一下，数学意义上的“等号”，在大部分编程语言中都用“==”表示。
还有一个例子说明了等号的概念：
```python
x = 0
x = x + 2
```
如果当成数学等式，x = x + 2不成立。但如果是**赋值**，意义很明显，让x的值从0增加到2。
下面的例子，请大家看看答案是多少？
```python
a = 'ABC'
b = a
a = 'XYZ'
print(b)
```
【学生提问】答案是多少呢？
最后一句，改变了a的值，但是没有改变b的，所以b的值是’ABC’。

### 布尔值
在Python中，可以直接用**True**、**False**表示布尔值（请注意大小写），也可以通过布尔运算计算出来
```python
>>> True
True
>>> False
False
>>> 3 > 2
True
>>> 3 > 5
False
```

布尔值可以用and、or和not运算。

and运算是与运算，只有所有都为True，and运算结果才是True：
```python
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> 5 > 3 and 3 > 1
True
```

or运算是或运算，只要其中有一个为True，or运算结果就是True：
```python
>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> 5 > 3 or 1 > 3
True
```

not运算是非运算，它是一个单目运算符，把True变成False，False变成True：

```python
>>> not True
False
>>> not False
True
>>> not 1 > 2
True
```


### 条件判断
语法规则为：
```python
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```

在写代码时，需要注意**冒号：**和**缩进**。例如如下的代码：
```python
age = 3
if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('your age is', age)
	print('teenager')
else:
	print('your age is', age)
	print('kid')
	
```
根据需要，代码中可以有多个elif。另外，要注意，if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，所以，请测试并解释为什么下面的程序打印的是teenager：
```python
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
```

【学生活动】请学生回答原因。
因此，在设计条件项的时候，要特别注意顺序。
Python还有一种很简单的条件语句：
```python
if x:
    print('True')
```
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

### Input()函数
上面的程序，要想看到不同的效果，我们需要在代码中修改：
```python
age = 3
```
可否让程序在运行的时候由用户自行输入呢？我们下面介绍的input()函数就是干这个的：
```python
age = input('age:')
if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('your age is', age)
	print('teenager')
else:
	print('your age is', age)
	print('kid')
```

运行程序后，系统等待输入，输入数字后。。。。出错了！看看错误是什么？
```bash
Traceback (most recent call last):
  File "class2.demo4.py", line 2, in <module>
    if age >= 18:
TypeError: '>=' not supported between instances of 'str' and 'int'
```

原来，`age = input('age:')` 获得的是一个字符串。字符串和整形之间是不能直接运算的。也就是说不可以出现：
```python
a = ’12’ + 8          # error
```
我们需要做一个转换：
```python
str_age = input('age:')
age = int(str_age)
if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('your age is', age)
	print('teenager')
else:
	print('your age is', age)
	print('kid')
```
`str_age`存储了一个用户输入的字符，用int()将其转换为数字并保存在age中，正确！
那我们在程序运行时尝试输入“abc”会出现如下的错误提示：
```python
Traceback (most recent call last):
  File "class2.demo4.py", line 2, in <module>
    age = int(str_age)
ValueError: invalid literal for int() with base 10: 'abc'
```
很清楚，Python发现，无法将“abc”转化为一个合法的数字。所以报错了。如何处理这种错误，我们以后讲。

### 数学运算
Python的数学运算功能特别简单，直接在命令行中就可以做运算：
```python
YuedeMacBook-Pro:class2 yuezhang$ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 23 * 3
69
```
实际工作中，很多程序员都用python直接当计算器使用。另外，Python语句都可以用这种最简单的方式运行。例如：
```python
>>> a = 12
>>> b = 34.32
>>> a = a * b
>>> print(a)
411.84
```


在代码中，我们也可以方便的进行算术运算。关于除法，大家观察如下的程序（demo6）：
```python
print(10 / 3)			# 3.333333
print(9 / 3)			# 3.0 注意，不是整数3
print(10 // 3)			# 3 整除
print(10 % 3)			# 1 余数运算
```
我们要清楚不同除法的意义和结果。


## 作业
写一个程序，允许用户输入身高和体重，按照BMI公式（BMI值 = 体重 / 身高的平方），计算BMI指数并按照下面的数值范围给出建议：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
(参考答案demo7)
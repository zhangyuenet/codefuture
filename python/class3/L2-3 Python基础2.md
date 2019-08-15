# L2-3 Python基础2
## 教学目标
1. 循环；
2. list/tuple；
3. 字符串精讲；

## 课程导入
大家回想一下，在基础课程中，我们是如何计算出1加到100的?
对的，大家都记得，我们用到了循环。我们今天会讲到Python中的循环。循环有个特别重要的作用是处理字符串和数组。所以我们，就从数组和字符串来讲起。

## 课程设计
### List/Tuple
若干有相同性质的数据组成的集合，可以用list来表示：
```python
>>> classmate = ['Eason', 'Audrey','Steven','Alice','Wilson']
>>> classmate
['Eason', 'Audrey', 'Steven', 'Alice', 'Wilson']

```
上面的classmate就是个list。list最重要的属性是什么？当然是list的元素数。很简单：
```python
>>> len(classmate)
5
```
获取classmate中每个同学的信息也不难：
```python
>>> classmate[0]
'Eason'
>>> classmate[1]
'Audrey'
>>> classmate[2]
'Steven'
>>> classmate[3]
'Alice'
>>> classmate[4]
'Wilson'
>>> classmate[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
大家一定注意，`classmate[5]`之所以出错，是因为计数是从0开始的。这里说的技术，称之为索引（index）。
除了Python，大多数编程语言的索引都是从0开始计数的，这一点要特别小心。
【学生提问】提问，如下的代码结果是什么？
```python
>>> classmate[len(classmate) - 1]
```
`len(list) - 1`是一个list的最后一个元素的索引。但是实际使用的时候不用这么麻烦，list还可以这样用：
```python
>>> classmate[-1]
'Wilson'
>>> classmate[-2]
'Alice'
>>> classmate[-3]
'Steven'
>>> classmate[-4]
'Audrey'
>>> classmate[-5]
'Eason'
```
大家应该发现规律了，index是负数时，就是从后往前的“倒数第几个”。
大家仔细想想，为什么在长度为5的list中，index=5会出错，index=-5却不会出错？
List还有很有用的特性，就是可以随时增加元素：
```python
>>> classmate.append('tom')
>>> classmate
['Eason', 'Audrey', 'Steven', 'Alice', 'Wilson', 'tom']
```
也可以减少末尾的元素：
```python
>>> classmate.pop()
'tom'
>>> classmate
['Eason', 'Audrey', 'Steven', 'Alice', 'Wilson']
```

还可以插入到指定的位置：
```python
>>> classmate.insert(1, 'tom')
>>> classmate
['Eason', 'tom', 'Audrey', 'Steven', 'Alice', 'Wilson']
```
同样可以删除指定位置的元素：
```python
>>> classmate.pop(1)
'tom'
>>> classmate
['Eason', 'Audrey', 'Steven', 'Alice', 'Wilson']
```

【学生提问】大家回答一下，如果我们偏偏要求大家用insert而不是append向list的末尾增加元素，应该怎么写？
替换list中的元素，也不难，直接找出来对应的元素，给它“赋值”：
```python
>>> classmate
['Eason', 'Audrey', 'Steven', 'Alice', 'Wilson']
>>> classmate[2] = 'ziyi'
>>> classmate
['Eason', 'Audrey', 'ziyi', 'Alice', 'Wilson']
```

我们刚才使用classmate，存储的数据都是字符，但是在一个list中，元素类型可以不同：
```python
>>> T = [1,'Tom', True]
>>> T[1]
'Tom'
```

甚至，可以在list中放入一个list:
```python
>>> T = [1, ['Tom', 'Jerry'], True]
```
【学生提问】请问T中有几个元素？
答对了！T一共包含3个元素。
```python
>>> len(T)
3
>>> T[1]
['Tom', 'Jerry']
```
【学生提问】大家猜猜怎么显示出“Jerry”？
答对了：
```python
>>> T[1][1]
'Jerry'
```

这种list，称为“二维数组”。
我想大家一定想到了，既然数组元素可以是数组，那么一个数组的数组元素中，依然可以包含数组元素。听上去绕口，但是大家能明白，可以有“三维数组”，“四位数组”，形成类似如下的表示：
```python
T[1][0][3][5]
```
不过，除非是某些数学矩阵的运算等场景，一般不这样用。
最后我们再说一种空数组，例如一个年级刚开班，还没有学生名单时，就可以这样写：
```python
>>> classmate = []
>>> len(classmate)
0
```
实际写程序时，经常会写空列表，待后续加入元素。
以上我们介绍了list，另一种列表形式称为：tuple，中文有地方翻译成“元组”。当你不能记住中文名时，只要记住英文名tuple就可以了。
Tuple和list的最主要区别是，tuple一旦创建就不可修改。tuple没有append/pop/insert。也不能针对某个元素赋值：
```python
>>> classmate = ('Tom', 'Jerry')
>>> classmate
('Tom', 'Jerry')
>>> len(classmate)
2
>>> classmate[1] 
'Jerry'
>>> classmate[1] = 'Bill'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
大家看到了，创建tuple和list的区别是括号不同。一旦创建，就不可以赋值。
但是，有一种情况，tuple中的数值是可以被改变的：
```python
>>> T = (3, ['Tom', 'Jerry'], True)
>>> T[1][1] = 'Bill'
>>> T 
(3, ['Tom', 'Bill'], True)
```
【学生提问】谁能告诉老师？为什么这样写不会出错呢？

关于tuple，最后要特别说明一下的是，只有一个元素的tuple会出现歧义：
```python
>>> T = (True)
>>> T
True
>>> T = (True,)
>>> T
(True,)
>>> len(T)
1
```

因为`（True）== True`，所以 `T = (True) ` 等价于 T = True。
所以如果希望让程序知道你在定义一个只有一个元素的tuple，增加一个逗号，增加的逗号并不会增加元素的数量。

### 循环
参见class3.demo1.py
List/tuple是编程中经常用到的结构。为了处理列表类结构，我们需要用到循环。大家迅速想一下在基础课中学过的循环结构。
Python中循环的结构有两种：
```python
for name in classmate:
     print(name)
```
另一种：
```python
num = len(classmate)
n = 0
while(n < num):
	print(classmate[n])
	n = n + 1
```
【学生提问】大家讨论一下，什么时候可能会用第一种，什么时候可能用第二种？
大家在写循环的时候，千万别忘了冒号（：）还有循环的部分必须有缩进（intent）。
循环有一个知识点是需要大家了解的，就是在循环过程中，可以用命令随时终止。
```python
# break
num = len(classmate)
n = 0
while(n < num):
	if(n > 2):
		break
	print(classmate[n])
	n = n + 1
```

【学生提问】请大家回答一下这个问题的答案，最终打印几个名字出来呢？

另一个和循环有关的命令是continue，这个命令可以让程序跳过循环体内后续的代码，进入下一个循环：
```python
classmate = ['Eason', 'Audrey','Steven','Alice','Wilson']
# continue
for name in classmate:
	if name == 'Alice':
		continue
	print(name)
```
打印出来大家看到，“Alice”的名字没有被打印出来。

大家再看看下面的代码：
```python
# continue
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)
```
【学生提问】请大家读代码，猜猜看最终打印出来的是什么？

【学生提问】下一个问题，请大家马上动手练一下，大家写一个**永远不会停止**的循环试试看？
```python
while true:
	input('name:')
```
如果大家写出了一个永远不会停的循环，可以用Ctrl + C停止程序。
当然，有时候我们确实需要一个永远不会停的循环，例如很多服务器程序，就是一个永不停歇的循环，持续的接收来自网络的消息。

### 字符串（string）
字符串，本身是一个由字符组成的tuple。例如：“ABCD”。字符串有几个问题需要考虑：
1. 字符串本身的操作：这很像tuple的操作；
2. 中文的问题；
3. 字符编码的问题。

第三个问题比较复杂，我们会用一次专题讲座的形式给大家解释。我们今天主要解决前两个问题。
首先我们看字符串的一些基本操作：
```python
t = 'ABCD'
# string item 
print( len(t) )
print( t[2] )
print( t + 'EFG')
print( 'C' in t)
print( 'Z' in t)
```
要对字符串作修改，如下的方式是不行的：
```python
>>> t = 'ABCD'
>>> t[2] = 'S'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

如果确实要修改，可以这样做：
```python
>>> t = 'ABCD'
>>> t.replace('C','S')
'ABSD'
```

关于字符串的更多信息，大家可以看看python的文档：
[https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str][1]
另外提醒大家，所有的命令不需要死记硬背，遇到的时候，通过查文档获得用法就可以了。

下面我们看看中文的问题：
首先，确认一下中文的长度。看下面两种情况：
```python
[yuezhang@YuedeMacBook-Pro:] ~ $ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15) 
>>> t = '测试'
>>> len(t)
6
```

```python
[yuezhang@YuedeMacBook-Pro:] ~ $ python3
Python 3.7.3 (default, Mar 27 2019, 09:23:15) 
>>> t = '测试'
>>> len(t)
2
```

在Python2.7和3.7中，“测试”两个汉字的长度是不同的。为什么呢？
这是因为在Python3中，所有的字符默认按照Unicode进行编码。所以不会出错。但是如果是Python2，因为没有指定字符编码，因此是按照存储的字节数来做处理的。关于这里的详细的知识我们会用一次讲座来和大家讲解。

如果是在py文件中，这种情况会更加严重，写下面的程序保存在文件中：
```python
t = '测试'
print(t)
```
用python2.7执行结果是：
```python
 $ python class3.demo3.py 
  File "class3.demo3.py", line 1
SyntaxError: Non-ASCII character '\xe6' in file class3.demo3.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```
当然，大家能猜到，用Python3.7执行不会出错：
```python
$ python3 class3.demo3.py 
测试
```
尽管我们可以保证，在我们自己的电脑上，我们使用python3，但是我们无法保障别人用什么版本的python执行我们的程序。因此，请大家养成一个好习惯可以避免这个问题，如果你的代码中需要输出中文，请在文件头包含如下内容：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

t = '测试'
print(t)

```
最上面的两行注释：
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

大家在练习的时候不需要这样做，但是如果将来要把自己写的程序交给别人使用，最好注意这一点。

我们看到字符串使用引号包含的符号串，那么大家有没有想过？如果我们的字符串本身就需要有引号怎么办？例如我们如何用字符串存储下面这句话：
```python
I like Tom's cat
```
方法是“转义字符”，在python语言中，转义字符是“\\”。使用转义字符，我们可以将引号包含在字符串中：
```python
>>> t = 'I like Tom\'s cat'
>>> print(t)
I like Tom's cat
```
同样，大家猜猜，我们如何在字符串中表示“\\”？大家觉得应该怎样写？
猜对了，就是对“\\”使用转义字符：
```python
>>> t = 'I like \\Tom\\'
>>> print(t)
I like \Tom\
```
还有一些其他转义字符，例如常用的换行符“\\n”
```python
>>> t = 'I like \n Tom'
>>> print(t)
I like 
 Tom
```
其他转义字符请大家搜索“Python转义字符”，看看还有哪些。下面给大家讲解一个方便使用Python字符串的方式：
```python
x = 'ABCD'
y = "ABCD"
z = '''ABCD'''
```
这三种形式都可以用来表示字符串。那么他们有什么区别呢？
```
>>> t = "I like Tom's cat"
>>> print(t)
I like Tom's cat
>>> t = 'I like "Tom"'
>>> print(t)
I like "Tom"
>>> t = '''I like 
... Tom
... '''
>>> print(t)
I like 
Tom

>>> 
```
看上面的代码，我们能够总结出如下三点：
（1）如果字符串中包含单引号，如果字符串用双引号包括，则无需使用转义字符；
（2）如果字符串中包含双引号，如果字符串用单引号包括，则无需使用转义字符；
（3）如果字符需要换行，可以使用三引号包括，这样可以在写代码时自由换行。
如果没有如上的三种情况，单引号，双引号和三引号，是没差别的。

字符串还有很多有意思的操作特性，我们不再一一举例子，大家请保存下面的链接，我们强烈建议你好好的读一遍。然后把这个链接保存起来，以后当遇到字符串问题时，可以翻出来看看怎么用。
[https://www.runoob.com/python/python-strings.html][2]


## 作业：
写一个程序，使用input()接收用户输入一个字符串，将该字符串顺序颠倒后用print()输出，例如：用户输入‘ABC123’，则程序输出结果应该是：‘321CBA’。
【特别提醒】其实可以有很多种方式实现该功能。大家不妨尝试一下。如果能用多种方式实现，我们有奖励！

[1]:	https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str
[2]:	https://www.runoob.com/python/python-strings.html
# L2-4 Python基础3
## 教学目标
- 字符串；
- 字符显示的格式；
- bytes；
- 数据类型的转换。

## 课程导入
在早期的计算机中，程序主要处理数字。因为计算机的主要功能是**计算**。
但是在当今的计算机和手机中，大家知道，更多的是在处理文字、图像、视频。
我们今天主要就帮助大家认识一下文字。文字主要通过**字符串（string）**类型存储。

## 教学设计

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
 $ python class4.demo2.py 
  File "class4.demo2.py", line 1
SyntaxError: Non-ASCII character '\xe6' in file class3.demo3.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```
当然，大家能猜到，用Python3.7执行不会出错：
```python
$ python3 class4.demo2.py 
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
方法是“转义字符(Escape character)”，在python语言中，转义字符是“\\”。使用转义字符，我们可以将引号包含在字符串中：
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

### 字符串显示格式
显示格式的问题，在一些教程里面称之为：**格式化（Format）**。
因为大家是否还记得上节课的作业，我们可能要输出类似下面的内容：
```python
您好，您的身高是XXX厘米，体重是XXX厘米，BMI指数是XXX，体型XXX。
```
其中，XXX的部分都是可变的。而其它部分则是根据运算结果需要显示出来的变量。
```python
>>> '您好，您的身高是 %d 厘米，体重是 %d 厘米，BMI指数是: %d，体型:%s' % (170, 70, 24.22, '正常')
'您好，您的身高是 170 厘米，体重是 70 厘米，BMI指数是: 24，体型:正常'
```

大家估计能猜到了：%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%X 占位符，后面就跟几个变量或者值，顺序要对应好。如果前面只有一个%X ，则后面的括号可以省略：
```python
>>> 'hello: %s' % 'Tom'
'hello: Tom'
```
常见的格式占位符号有：
- %d	整数
- %f	浮点数
- %s	字符串
- %x	十六进制整数

其中比较有用的，是 %f 可以指定小数的位数，或者 %d 补零的个数：
```python
>>> print('%.2f' % 3.14159265 )
3.14
>>> print('%02d' % 5)
05
```

大家大致知道用法即可，在需要的时候可以使用。
有一个简洁的办法，当你不知道用什么格式的时候，%s一般总是可以用的。
最后，要了解，如果我们的格式需要显示“%”怎么办？
用**%%** 来显示“%”
```python
>>> '增长率：%.1 %%' % 5.34532
'增长率：5.3 %'
```

### Bytes
计算机在显示时，使用“字符”：“ABC”，“123”。
但是在存储和传输时，使用**“字节”**。一个字符可能对应于多个字节。这个我们会用专题讲座的形式给大家来讲解。大家只要知道，目前在Python和当前的大部分软件中，都使用一种叫做Unicode的编码。这种编码显示如下：
```python
>>> '\u4e2d\u6587'
'中文'
```

所以，我们看到的中文字符，在电脑和网络中，都要用类似于“4e2d”这样的编码来保存。所以我们需要知道一种数据类型：bytes。未来在学习网络编程和文件存储的时候要用到。
在python中，用字母b表示bytes类型：
```python
>>> x = b'abc'
>>> y = 'abc'
```
上面的例子中间：x是bytes类型，y是字符串类型。

使用**encode** 和 **decode** 把字符串变成bytes：
```python
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```
大家只需要知道我们当前的计算机存储和传输，统一使用**utf-8**做编码类型，而显示统一使用unicode，所以，大家在碰到从文件或者网络读取数据时，是将utf-8编码的bytes解码（decode）成unicode编码的字符，在保存文件或者做网络传输的时候，将unicode字符编码(encode)成utf-8编码。

### 类型转换
【学生提问】我们先来看个问题。
```python
a1 = '3'
a2 = 4
print(a1 + a2)
```
上面的内容结果是什么？为什么？

答对了！结果是错误！因为字符串和数字类型不同，不能进行运算。
我们在之前讲过转换的办法：int()
```python
>>> print(int(a1) + a2)
7
```
大家回忆一下，我们都学习了多少种Python类型：
```python
a = 100 #int 整型
b = 100.55 #float 浮点型
c = '100' # string 字符串
d = [1,2,3] # list 列表
e = (1,2,3) # tuple 元组
f = b'abc' # bytes
```
那么，如何转换这些类型呢？
（1）**int()**可以将数字型字符串转换为整形，也可以将float类型转换为整形（取整），如果无法转换，则系统报错；
```python
>>> int('123')
123
>>> int(123.87)
123
>>> int('123abc')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '123abc'
>>> int('123.87')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '123.87'
```

(2) **float()**可以将整数和字符串转换为浮点数：
```python
>>> float(123)
123.0
>>> float('123.45')
123.45
```

(3) **str()**函数可以数字转换为字符：
```python
>>> str(123)
'123'
>>> str(-123)
'-123'
```

这里有一份“史上最强”的Python数据类型转换介绍：
[https://shockerli.net/post/python3-data-type-convert/][3]
大家可以收藏以备后用。


## 作业
（1）大家根据今天所学，并通过查阅资料，实现如下的转换：
```python
x = [1,2,'3']

经过什么样的转换，最终可以输出：'123'？
```

（2）今年人民币兑换美元从6.8:1 跌到了 7.2:1，请用代码输出今年人民币的跌幅，要求显示百分比，并保留1位小数，并要求显示时带“%%”：
```python
 change = ??????
print( '???????', change)

```




[1]:	https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str
[2]:	https://www.runoob.com/python/python-strings.html
[3]:	https://shockerli.net/post/python3-data-type-convert/
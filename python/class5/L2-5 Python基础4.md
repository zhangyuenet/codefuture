# L2-5 Python基础4
## 教学目标
- dict/set；
- 简单的文件操作；

## 课程导入
我们前面学过了list/tuple。
【学生提问】list和tuple的区别是什么？用在什么场合？ 

今天，我们将学习另外一对有些相似的数据类型：dict/set。
大家在学习的时候，多想想，它们和list/tuple的差别。

## 教学设计
### dict
我们先来看一个例子(class5.demo1.py)：
老师公布了考试成绩：Tom：85分，Jerry：90分。于是可以这样写：
```python
name = ['Tom', 'Jerry']
score = [85, 90]

num = len(name)
n = 0
while(n < num):
	print(name[n] + ':' + str(score[n]) )
	n = n + 1
```
结果是：
```python
Tom:85
Jerry:90
```

Dict类型可以很好的处理这种情况，我们看代码：
```python
result = {'Tom':85, 'Jerry':90}
for name in result:
	print(name + ':' + str(result[name]))
```
上面的result就是一种dict类型。
dict是一种 key - value的类型存储方式：
```python
key1->value1 ; key2->value2 ; …… ; keyN->valueN
```
通过定义一组key|value。可以快速通过一个key值找到一个value。这就像字典的索引表。从前到后一页页翻，可以找到一个汉字，但是太慢。通过索引，就能快速定位出一个汉字在词典中的页码，就可以很快找到它。
大家体会一下什么情况下用list，什么情况下用dict。
```python
>>> result = {'Tom':85, 'Jerry':90}
>>> result['Tom']
85
>>> result['Tom'] = 95
>>> result['Tom']
95
>>> result['tom']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'tom'
>>> result['Mike']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Mike'
```
有了dict，我们可以快速的通过索引找到对应的值，也可以修改某个索引的值。
但是如果使用了错误的索引，系统将返回错误。尤其请大家注意拼写，比如：’Tom’和’tom’是不同的索引。
我们可以有两种办法知道一个索引是否包含在dict里面：
```python
>>> 'Tom' in result
True
>>> 'tom' in result
False
>>> result.get('Tom')
95
>>> result.get('tom')
>>> 

```
如果用get无法获取到Key，则返回NULL（空值），在这里也可以自定义一个返回值：
```python
>>> result.get('tom', -1)
-1
```
Dict类型可以直接添加数据或者用update增加和修改数据，也可以用pop删除键值对。
```python
>>> result
{'Tom': 95, 'Jerry': 90}
>>> result.update({'Mike':80})
>>> result
{'Tom': 95, 'Jerry': 90, 'Mike': 80}
>>> result.pop('Mike')
80
>>> result
{'Tom': 95, 'Jerry': 90}
>>> result['Zoe'] = 65
>>> result
{'Tom': 95, 'Jerry': 90, 'Zoe': 65}
>>> result.update({'Tom':85})
>>> result
{'Tom': 85, 'Jerry': 90, 'Zoe': 65}
```

Dict讲到这里，大家基本了解了使用方式。那么请大家来回答一个问题：
【学生提问】Dict和list的区别？什么时候用dict，什么时候用list?
(学生只要回答不算离谱，都应该鼓励。)
和list比较，dict有以下几个特点：
- 查找和插入的速度极快，不会随着key的增加而变慢；
- 需要占用大量的内存，内存浪费多。
而list相反：
- 查找和插入的时间随着元素的增加而增加；
- 占用空间小，浪费内存很少。

### set
set是另一种常用的列表。我们看看set常用的操作，然后基本上就清楚了：
```python
>>> s = set(['a','b','c'])
>>> s
{'a', 'b', 'c'}
>>> s = set(['a','b','c','a'])
>>> s
{'a', 'b', 'c'}
>>> s.add('d')
>>> s
{'a', 'd', 'b', 'c'}
>>> s.add('c')
>>> s
{'a', 'd', 'b', 'c'}
>>> s.remove('c')
>>> s
{'a', 'd', 'b'}
>>> s1=set(['a','b','c'])
>>> s2=set(['b','c','d'])
>>> s1 & s2
{'b', 'c'}
>>> s1 | s2
{'a', 'b', 'd', 'c'}
```
大家观察到使用add/remove进行元素的增减，如果有重复元素，添加是无效的。set还可以用交集（&）和并集（|）运算。
这里面有一个特别需要注意的地方，请大家一定注意：
```python
>>> s = set(['a','b','c'])
>>> s
{'a', 'b', 'c'}
>>> s.add('d')
>>> s
{'a', 'd', 'b', 'c'}
```
当增加一个元素的时候，难道不是应该增加到末尾么？
这里要说明一下，dict/set类型中，显示:
```python
{'a', 'd', 'b', 'c'}
```
不代表这些显示内容是这样的排列顺序，dict/set实际的存储顺序，和key存入的顺序是没有关系的。当大家需要一个顺序列表时，一定要考虑到dict/set的情况。
【学生提问】大家考虑一下，你在什么情况下会用set?
（需要引导学生能够注意到set的元素不重复的特性）

到此为止，基本的python数据类型我们就都已经学习完成了。大家最后再回忆一下：
```python
a = 100 #int 整型
b = 100.55 #float 浮点型
c = '100' # string 字符串
d = [1,2,3] # list 列表
e = (1,2,3) # tuple 元组
f = b'abc' # bytes
g = {'a':1, 'b':2} # dict
h = set(['a','b','c']) # set
```

【在这里，最好由老师用命令行每写一个，就让学生自由回答是什么。加深同学的印象】


### 简单文件操作
程序运行过程中会产生很多数据，使用文件是最常用的一种存储数据的方法。
我们今天给大家简单的介绍用文件来读取数据的方法（demo2.py）：
```python
f = open('demo1.txt' , 'r')
print(f.read())
f.close()
```

【学生提问】“顾名思义”，是学习编程特别重要的一个方法。现在请大家根据上面的代码，告诉老师，每行代码是什么意思？
估计学生只有参数“r”无法理解。
这里的参数“r”，指的是访问模式（access mode）。访问模式有详细的说明文档，但是目前这个阶段，我们只需要记住下面这几种最常用的：

- r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
- rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。 
- w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
- wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
- a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
- ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

大家一定迫不及待了，让我们马上试试看写入(demo3.py)：
```python
f = open('test.txt', 'w')
f.write('Hello world!')
f.close()
```
大家自己试试看，将模式从”w”换成“a”的效果。
至于‘wb’和‘rb’，大家看看下面的代码（demo3.py）：
```python
f = open('test.txt', 'wb')
s = '你好'.encode('utf-7')
f.write(s)
f.close()


f = open('test.txt', 'rb')
s = f.read()
print(s)
f.close()
print(s.decode('utf-7'))
```
结合上节课讲到的encode/decode。大家看看为什么需要在这里使用编码和解码。同时，大家将程序中的’utf-7’换成大家知道的’utf-8’，看看效果是什么样的？
实际上，
（1）使用”r”模式读取数据；
（2）用”rb”模式读取bytes数据，并用”utf-8”解码。
这两种模式本质上是一样的，因为文件存储缺省使用”utf-8”编码。

大家一定要时刻保持注意，open的东西往往需要我们close。因为每一次open，都要占用系统资源，如果总是不关闭，系统占用的大量资源无法释放。文件也是中处在使用中的状态。

## 作业（参考实现demo4.py）
有时候人们会忘记自己在某些网站或者APP的用户名和密码，所以会有人将这些信息记录在文件里（当然，这种做法不安全，请大家不要模仿），这里有一个文件，内容如下：
```bash
sina.com;zhang@qq.com;1234
weixin.com;li@qq.com;abcd
bilibili.com;zhao@qq.com;asdf
iqiyi.com;wang@qq.com;9876
```
即，格式为：“网站名；用户名；密码”，每行一个。
要求写一个程序，读取这个文件，并提供查询功能。
程序启动后，要求类似如下的提示，打印出来的结果是：“用户名：XXX；密码：XXX”，譬如：
```bash
$ python3 class5.demo4.py
输入一个网站：bilibili.com
用户名：zhao@qq.com；密码：asdf
```

提示1：Python可以用readlines按行独出所有的数据，并存在list中，可以这样使用：
```bash
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
```

提示2：对于“XXXX;XXXX;XXXX”这样的字符串，可以用string.split()方法将字符串方便的拆分成三部分，并存入一个列表。具体用法，老师不讲，请大家用关键字：“python split”自行搜索。
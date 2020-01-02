# TCP编程-Server
## 课程导入
上节课我们学习了TCP/IP的基础知识，大家不用焦虑，以大家的年龄而言，只需要有印象就可以了。
我们也学习了如何发送一个数据请求，并得到反馈。大家还记得，老师演示的代码演示了从百度新闻的网站抓取了数据。作业是请大家试试自己改写程序去获取一些数据，看看这些数据。不知道大家都抓了什么数据出来？有没有遇到一些有意思的情况？

大家有没有想过，为什么我们发送一个指令，就能获得数据？实际上，在百度新闻的网站，有一个服务(service)接收到了我们发出的指令并且进行了处理。今天这节课，我们就来学习一下，如何创建一个服务并且和我们上节课学过的客户端配合起来，实现一个完整的消息发送/接收系统。

在这里，老师再次强调一下我们上节课提到的一个约定：
```python
服务端（Server）：被动接收数据并根据接收到的数据进行反应；
客户端（Client）：主动发送数据并根据获取的数据进行反应；
```


## 服务器
客户端建立连接的过程是：
```python
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('news.baidu.com', 80))
```
前面引入socket库并且创建一个socket对象的过程是一样的，但服务器不是连接远程地址，而是和一个固定的地址做绑定：
```python
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
```

这里要解释两件事：
第一，这里的IP地址127.0.0.1是怎么回事？
第二，绑定和监听的含义（bind & listen）。

127.0.0.1被称之为本机地址，在前面讲到的IPv4的规范中，127.x.x.x都被保留出来，也就是说，互联网上的任何服务器都不会出现127.x.x.x的地址。这些地址都用于内部使用。细节有些复杂，大家目前只需要了解，127.0.0.1代表了本机地址，在自己的电脑上测试程序时，可以用127.0.0.1代替本地IP地址进行测试。

我们上节课讲了，很多个应用程序要通过同一个IP地址获取数据包时，为了区分是那个程序的，需要用端口号做区分，不同服务程序启动时，端口号必须不同。用绑定（bind）的方式，告诉系统，所有发送到127.0.0.1地址，9999端口号的数据要由我来处理。发送通知后，还需要做一个动作，就是“坐在家里等快递”，这个过程称之为“监听”(listen)，这样可以确保包裹到了能够得到及时的处理。listen的参数是个整数，标明了同时允许的最大连接数，也就是同一时刻最多允许多少个快递员放快递进来。

服务器，因为需要被动接收数据并进行处理，所以我们至少一点，这个程序需要长时间运行，而非运行一次后就立刻退出。在Python中，可以用这种方式让一个程序长时间运行而不退出：
```python
while true:
	# do something.
	
	if 某一些退出条件 :
		break

```

Python中，长运行的程序大体上类似于上面的写法。既可以让程序长时间运行，也可以让程序在某些条件下退出。大家回忆一下，上节课我们也用到了类似的写法：
```python
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
```

在这里，服务器要处理接收到的数据包，我们也用一个长运行的while循环：
```python
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    worker(sock, addr) 
```
Socket.accept()方法会等待连接，一旦有连接进入，就返回客户端连接对象。
我们用一个函数worker()来处理客户端的连接响应，代码如下：
```python
def worker(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('received %s;' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
```

大家阅读一下代码，大致能够理解服务器做了如下处理：
1. 在服务器上打印出来这个客户端连接来自哪里（addr）；
2. 向客户端发送了“欢迎”；
3. 接受数据，其中，每接受一包数据，休息一秒（为了演示方便显示）；
4. 如果接受不到数据了，或者接收到了数据“exit”，停止处理；
5. 向客户端发送消息接收到了什么数据；
6. 关闭客户端连接；
7. 在服务器端打印出来连接关闭；

整个服务端完整的代码如下(server.py)：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# single thread Server example
# CodeFuture@CA

# 导入socket库:
import socket
import time

def worker(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Received %s;' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    worker(sock, addr) 

    
```

需要注意的是，需要先定义worker()函数，才能在主程序中使用它，因此需要把worker函数写在前面，server的处理逻辑写在后面。

## 再写一个客户端
为了验证我们刚才写的服务器，我们写个简单的客户端，代码如下：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

for data in [b'message1', b'message2', b'message3', b'message4', b'message5']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```

和上节课我们写过的客户端程序非常像，请大家注意，在发送完五条数据后，客户端发送了“exit”，而按照服务器代码的设计，遇到“exit”，服务器会知道客户端完成了既定工作，可以中断连接了。用这样的设计，我们就实现了一种最简单的“**协议（protocol）**”。
协议简单来说，就是客户端和服务器之间的一种约定，大家只要都遵守这种“约定”就可以彼此理解对方的想法。好比我们和好朋友之间约定：如果发送的包裹上面画一个“红心”，就代表包裹里面是我最喜欢的书；如果画一个“箭头”，则代表包裹中是我送的玩具，等等。
从实际工作来说，各种通信协议往往都很复杂，但从本质上，和我们的“exit”一样，都是一些特定符号的组合。

我们测试一下我们的服务器和客户端，首先启动服务器：
```python
$ python3 server.py
Waiting for connection...
```
服务器顺利启动，开始等待连接进入。
然后我们启动客户端：
```bash
$ python3 client.py
Welcome!
Received message1;
Received message2;
Received message3;
Received message4;
Received message5;

```
客户端顺利执行。而这时，服务器输出了如下信息：
```bash
Accept new connection from 127.0.0.1:62140...
Connection from 127.0.0.1:62140 closed.
```
客户端可以反复启动，服务端也将反复的打印上述信息。
最后大家注意，客户端执行完成就直接退出了。而服务器是不会退出的，除非我们输入Ctrl+C命令强制退出。

## 设计一个简单的协议
刚才我们讲到了协议（Protocol），这在编程中是个重要的概念。大体上，两个设备通信，大家要么遵从某种设计好的协议，要么根据实际需要自行设计一套协议。在今天的课程中，我们尝试自行设计一套协议，前面讲过，所谓协议，就是一套规则。我们来定义这套规则。
```bash
需求：我们希望可以向服务器发送一条通信记录，并且可以通过同样的客户端查询该记录。
命令1: 添加/修改一条记录
add;[姓名];[手机号码]
exit

服务器响应：
[姓名] added!

为了简便起见，当服务器发现同样的姓名已经存在时，直接用新的记录覆盖，相当于更新了该姓名的手机号。

例如：我们需要向服务器添加一条记录时，发送如下消息：
add;zhangsan;13800138000
exit

服务器响应为：
zhangsan added!

命令2: 删除一条记录
remove
[姓名]
exit

服务器响应为：
[姓名] removed！
或者：
Not found!

例如：我们需要向服务器删除一条记录时，发送如下消息：
remove;zhangsan
exit

服务器响应为：
zhangsan removed!
或者：
Not Found!


命令3: 查询一条记录
find;[姓名]
exit

服务器响应为：
[手机号]
或者
Not Found!

例如：我们向服务器发送一条查询记录：
find;zhangsan
exit

服务器响应为：
13800138000
或者
Not Found!

```

以上的设计，说难不难，但也不简单。我们一起来实现一条语句。
首先我们需要改造客户端。Add语句如果我们不想写死，就需要让程序在执行时让用户输入，我们之前学过一种方式input()，获得用户参数，今天我们用另一种方式：程序参数。程序参数顾名思义，是在程序启动时获得的参数，在Python中，简单的参数处理用内置的sys模块就可以处理（复杂的推荐使用getopt模块处理，有兴趣的同学可以查查看），基本用法很简单：
`sys.argv` 是命令行参数列表。
`len(sys.argv)` 是命令行参数个数。
注：`sys.argv[0]` 表示脚本名。
用例子来看就清楚了：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)
```
执行以上代码，输出结果为：
```bash
$ python test.py arg1 arg2 arg3
参数个数为: 4 个参数。
参数列表: ['test.py', 'arg1', 'arg2', 'arg3']
```

所以，我们可以简单的用参数吧命令通过client传递给server (client2.py)：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
s.send((';'.join(sys.argv[1:])).encode('utf-8'))
print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```

这里面关键的一行是：
```python
s.send((';'.join(sys.argv[1:])).encode('utf-8'))
```
大家再去查查看字符串join和split的用法，他们几乎总是成对出现，我们等会就会用到split。
Join方法将一个list用“；”连接成一个字符串，这是个非常有用的办法，请大家一定记住。
另外，我们用`sys.argv[1:]` 来传递给服务器的参数。在list中，`[1:]`代表index从1到最后的所有内容。为什么这样写？大家想想？

【学生提问】为什么我们不传递sys.argv，而要忽略第一个参数？

大家答对了，第一个参数是程序名称本身，服务器并不需要这个名称，所以我们从index=1开始，忽略掉这个程序名称。

现在我们马上试试看，在server没有改动的情况下：
```bash
 $ python3 client2.py add zhangsan 12345
Welcome!
Received add;zhangsan;12345
```

这样一来，所有的命令都可以通过简单的参数方式发送了。那么重要的工作就在服务端。我们来处理Add的情形：
因为要保存姓名和电话号码，大家想想，用什么数据结构比较方便：

【学生提问】从下面的结构中选择出来适合保存姓名和电话的数据结构：
字符串/数组/list/tuple/dict/set 
【同时请学生回忆一下这些类型之间的区别】

很棒，我们用dict可以很好的解决这个问题（当然，用list或者其它也完全可以达到目标）。
我们先定义一个空的dict:
```bash
contacts = {}
```

然后在接受数据的地方处理指令：
```bash
        arg = data.decode('utf-8').split(';')
        if arg[0] == 'add':
            contacts[arg[1]] = arg[2]
            sock.send(('%s added' % arg[1]).encode('utf-8'))
```

大家看到了，因为发送的时候用了join将列表连接成字符串，就可以在接受的时候用split将字符串拆分成列表，他们配对使用，就会很方便。  

完整代码如下（server2.py）：
```bash
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# single thread contacts server example
# CodeFuture@CA

# 导入socket库:
import socket
import time

contacts = {}

def worker(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        arg = data.decode('utf-8').split(';')
        if arg[0] == 'add':
            contacts[arg[1]] = arg[2]
            print(contacts) #在服务端显示当前存储的数据
            sock.send(('%s added' % arg[1]).encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    worker(sock, addr) 

```
好了，我们分别运行一下server2.py和client2.py。看看结果是正常运行的。现在到了大家练习的时间，剩下的部分，就是今天的作业啦，
## 作业
继续在老师的代码基础上，在客户端实现remove和find命令。

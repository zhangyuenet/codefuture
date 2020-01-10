# 多线程和UDP

## 教学目标
1. 了解线程的基本概念；
2. 了解如何使用多线程执行多任务；
3. 学习如何使用UDP连接；


## 课堂导入
我们在服务端listen的函数中，定义了我们允许同时接受5个客户端连接，现在就让我们来试试看，如果有多个客户端同时连接会有什么情形发生。
启动上节课（Lecture15）的server.py和client.py：
在启动服务端的情况下，打开两个命令行窗口，启动第一个客户端，然后紧接着马上再启动第二个。我们会看到。第二个客户端启动后并没有马上显示welome，而是要等第一个客户端全部执行完，才能开始正常执行第二个客户端的程序。

这说明，我们写的服务端程序，同一时刻只能处理一个客户端的连接。到这里，我们肯定要问一个问题，可否让我们的程序同时处理多个客户端连接。毕竟我们知道，当有好的电影在视频网站发布的时候，可能有好几百万人同时连接服务器观看的。

为了实现这个目标，我们在这节课要学习一个新的概念：多线程。

## 计算机是怎么同时运行多个程序的？
同时处理多个任务，这件事情好像计算机做的不错：
* 我们可以一边听歌一边浏览网页：音乐播放器和浏览器在同时工作；
* 我们可以一边聊天一边看电影：聊天工具，电脑既能处理微信消息，也能同步下载电影数据；
以上的场景，都是多任务的场景。对于大家来说，都是司空见惯的使用方式。可是，这对于计算机而言，并不简单。实际上，一个CPU在同一时刻，只能处理一个程序指令。那么大家是如何感受到多个程序在同时执行的呢？在这里简单解释一下：
“**进程** ”：计算机运行程序的基本单元，一个进程可以称之为一个“任务”。计算机为了同时执行多个“任务”，采用了“**分片**”的方式，也就是在很短的时间内分别执行每一个进程，从而让人感觉每个任务都在同时进行的假象。
用下面这张图做个简单的说明：
![进程][image-1]

在一个进程，或者说在一个任务中，也要完成不同的工作。例如音乐播放器，一方面需要在界面上显示文字和图像、还要响应用户鼠标点击的操作、还要从网络下载音乐和歌词。这些“子任务”可以用“**线程**”来实现。一个**进程**可以包含多个线程，但至少包含一个**线程**。一个进程内的所有**线程**共享进程内的所有资源。如图所示：
![thread][image-2]

建议大家读一下下面的短文，马上就可以很清楚进程、线程和锁的基本概念：
[https://www.ruanyifeng.com/blog/2013/04/processes\_and\_threads.html][1]

## 在代码中使用多线程
```python
import threading

t = threading.Thread(target=worker, args=(sock, addr))
t.start()
```

Python内置了多线程的函数库，在使用的时候引用threading即可。命令很简单：
* 创建一个函数，写入需要在线程（子任务）中执行的代码；
* 创建一个线程：指定上面的函数并给定参数；
* 启动这个线程；

我们用多线程来改造服务端代码（serverthread.py）：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# multi-thread Server example
# CodeFuture@CA

# 导入socket库:
import socket
import threading
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
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=worker, args=(sock, addr))
    t.start()

```

我们再试试改写后的效果。启动server2.py，再分别启动多个客户端client.py，大家可以看到，客户端已经不需要等待其它客户端执行完毕就可以开始执行了。

## UDP 
大家不知是否还记得，在Lecture14中，Client编程中，我们讲过创建Socket连接的命令是：
```python
socket.socket([family[, type[, proto]]])
```

其参数含义为：

**family**: 套接字名称协议，可以使用`AF_UNIX`   或者 `AF_INET`,
前者是一种UNIX命名方式，在网络中，用一个字符串标明地址。我们常用的是后者，使用IP+端口标明地址。实际上，在Python新版本中，还支持参数`AF_INET6`，大家猜猜看，这个参数是干啥的？ 

**type**: 套接字类型可以根据是面向连接的还是非连接分为 `SOCK_STREAM  ` 或者 `SOCK_DGRAM ` 。我们一般用面向连接的系统。

今天我们会跟大家讲一下另一个参数 `SOCK_DGRAM `的用法。`SOCK_DGRAM`参数用来建立一个UDP连接。
我们之前建立的连接都是TCP连接，这是一种安全而稳定的连接，而UDP连接是一种不很安全稳定，但是方便快捷的数据传输方式。只要知道对方的地址（IP地址+端口号），无需建立连接，直接发送数据，不过，对方能否收到，就不管了。是不是很任性？

这种方式适用于很多消息推送的场合，对方是否收到并不关键和重要的场合。这有点像我们日常生活中上门发放小广告的行为。因为并不需要用户签收，也不需要记录是否投递成功。

我们看看具体的用法，先看看server的代码（serverudp.py）：
```python
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    time.sleep(1)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
```

【学生提问】谁能回答一下？这段Server代码和之前的代码除了在创建Socket时参数“`socket.SOCK_DGRAM`”不同之外，最大的差别是什么？
【提示学生少了一个步骤，listen】

客户端相应也简单了（clientudp.py）：
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'message1', b'message2', b'message3', b'message4', b'message5']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
```

【学生提问】大家再找找客户端和之前的差异在哪里？
【TCP是connect后send，UDP是直接sendto】

大家试着运行一下，基本上和之前的程序看不出什么差别来。因为我们的场景非常简单，基本也不会出现数据丢失的情况。

未来如果要求大家根据某个server的要求让大家写一个client，大家请一定首先搞清楚，这个服务器支持的是TCP还是UDP。

我们的serverudp.py目前是个单线程的程序，我们尝试同时启动两个客户端试试看。
大家发现了没有，为什么没有出现今天上课开始的一幕，也就是没有说一个客户端一定要等到第二个客户端执行完成才开始执行？看上去好像多线程的运行效果，两个客户端都在同时运行，没有等待。

【学生提问】为什么在这里两个客户端没有出现等待的情况？
【提示学生，TCP客户端为什么会等待，实际上等待的是连接，因为UDP没有连接，所以无需等待。】

## 作业
找出来上节课我们自己写的协议，也就是实现了add，remove和find功能的server和client程序，尝试将它们改造成udp的版本。
【参考答案】contactclientudp.py和contactserverudp.py
如果学生难度太大，则可以吧server的一部分代码写给学生，比如Add，让学生继续修改remove和find中的部分，但至少要求学生独立完成client的改造。








[1]:	https://www.ruanyifeng.com/blog/2013/04/processes_and_threads.html

[image-1]:	process.jpg
[image-2]:	threading.png
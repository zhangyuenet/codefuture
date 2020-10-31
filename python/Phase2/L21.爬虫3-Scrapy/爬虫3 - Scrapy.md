# 爬虫3 - Scrapy
## 教学目标
1. 学会进阶的命令行参数；
2. 初步了解Scrapy；
## 课程导入
> Maoyan.com 作为爬虫训练的对象，随着猫眼网站的技术迭代，导致我们的爬虫程序并不十分稳定。我们这次课程该用xhsd.cn新华书店，中国大陆最有名的线下实体书店的网站来做范例。

前两节课，我们对爬虫程序做了两方面的工作：
1. 分析数据；
2. 获取数据；
3. 保存数据；
今天我们会学习一个在爬虫领域非常有名的模块，大量非常专业的应用厂商，都是在用这个工具。
## Scrapy
官方网站在这里：[https://scrapy.org/][1]
安装很标准：
```python
pip3 install Scrapy
```
我们马上进入实用环节：

## 分析爬取对象
我们这次的目标是新华书店的计算机类图书：
[https://www.xhsd.cn/lb.jsp?pid=0401010000][2]
我们打开网页观察一下，页面上有用的信息包含这些：书名，作者，图片，价格，详情链接。我们争取将这些信息都抓出来。
其中，“作者”的处理要稍微麻烦一些，等会会说到。

## 创建工程
我们首先需要创建一个工程：
```python
scrapy startproject mySpider
```
其中， mySpider 为项目名称，可以看到将会创建一个 mySpider 文件夹，请大家观察一下目录结构。
下面来简单介绍一下各个主要文件的作用：

scrapy.cfg: 项目的配置文件。
mySpider/: 项目的Python模块，将会从这里引用代码。
mySpider/items.py: 项目的目标文件，也就是定义我们需要获取那些数据。
mySpider/pipelines.py: 项目的管道文件（暂时不需要知道）。
mySpider/settings.py: 项目的设置文件。
mySpider/spiders/: 存储爬虫代码目录，我们的工作代码主要在这里。

大家打开看看settings.py文件，有没有找到熟悉的`USER_AGENT `属性。我们可以按照前几节课设置的UserAgent在这里进行设置，不管使用固定的还是用FakeUserAgent库都可以。今天老师用自己电脑上Chrome浏览器的UserAgent:
```python
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)'

```

## 定义数据结构
根据我们前面说的，希望获取的信息是：
- 书名，
- 作者，
- 图片，
- 价格，
- 详情链接
打开mySpider目录下的items.py。Item 定义结构化数据字段，用来保存爬取到的数据，有点像 Python 中的 dict，但是提供了一些额外的保护减少错误。代码如下：
```python
import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    photo = scrapy.Field()
```

## 制作爬虫
我们前面的课程里面已经很清楚，这里一定有两步，一步是获取数据，一步是分析数据。我们首先来获取数据。
在mySpider目录下输入命令：
```python
scrapy genspider booklist "xhsd.cn"
```
打开 mySpider/spider目录里的 booklist.py，默认增加了下列代码:
```python
import scrapy

class ItcastSpider(scrapy.Spider):
    name = "booklist"
    allowed_domains = ["xhsd.cn"]
    start_urls = ['http://www.xhsd.cn/']

    def parse(self, response):
        pass
```
其实也可以由我们自行创建booklist.py并编写上面的代码，只不过使用命令可以免去编写固定代码的麻烦（编程中经常如此）。

要建立一个Spider， 你必须用scrapy.Spider类创建一个子类，并确定了三个强制的属性 和 一个方法。

name：这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。

`allowed_domains`: 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。

`start_urls` ：爬取的URL 列表

parse(self, response) ：解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：

- 负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
- 生成需要下一页的URL请求。

下面我们来修改`start_urls` 的值：
```python
start_urls = ['https://www.xhsd.cn/lb.jsp?pid=0401010000']
```

修改下面parse()：
```python
def parse(self, response):
    filename = "booklist.html"
    open(filename, 'w').write(response.body.decode('utf-8'))
```

我们快速运行一下看看是否能吧数据抓下来，在mySpider中执行：
```python
scrapy crawl booklist
```

应该会出现很多信息，如果出现如下的信息，说明爬虫顺利执行：
```python
[scrapy.core.engine] INFO: Spider closed (finished)
```
如果网络正常，应该会出现booklist.html，打开文件仔细看看有没有我们想要的图书信息。提示一下，可以搜索一下`class="tab_box5"`，在这里仔细观察一下HTML页面非常有助于我们下一步的工作。
取到了数据之后，就可以来分析我们需要的数据了。
这次的数据结构有些复杂但是每个数据也都能找到明显的特征：
首先，只要仔细找，就能发现所有的图书数据都在下面的结构中：
```html
<div class="tab_box5">
	<table width="930" ...>
	<table width="930" ...>
	<table width="930" ...>
	<table width="930" ...>
	<table width="930" ...>
	......
</div>
```

每个table分别代表了一行，所以界面上一共五行。在table内部，也就是界面上一行（一排）图书的内部结构也是分行显示的。
- 第一行：图片信息；
- 第二行：图书名称和详情链接；
- 第三行：作者信息；
- 第四行：价格；
其余不用关心。
每一行都有五个td组成，也就是五列。我们吧XPATH直接写出来让大家感受一下：
```python
        names = response.xpath('//div[@class="tab_box5"]/table/tr/td/div/a/@title').extract()
        #print(len(names))
        photos = response.xpath('//div[@class="tab_box5"]/table/tr/td/div/a/img/@src').extract()
        #print(len(photos))
        urls = response.xpath('//div[@class="tab_box5"]/table/tr/td/div/a/@href').extract()
        #print(len(urls))
        prices = response.xpath('//td[@class="gray14"]/span[@class="red14"]/text()').extract()
        #print(len(prices))
```

至于“作者”，就麻烦一些了。大家试试看下面的语句返回是多少：
```python
authors = response.xpath('//div[@class="gray12"]/text()').extract()
print(len(authors))
```
运行一下可以发现，获取的值为23。而不是上面这些数据得到的25。
【学生提问】这是为什么？我们回到网站看一下，看看“作者”的内容有什么与众不同之处？

哈，应该发现了，原来是两本书没有作者。
这时，有25个书名，就只有23个作者。我们如何处理这种情况呢？
```python
        authors = response.xpath('//div[@class="gray12"]')
        auths = []
        for author in authors:
        	auth = author.xpath('text()').extract()
        	if len(auth) == 1:
        		auths.append(auth[0])
        	else :
        		auths.append(' ')
        print(len(auths))
```

大家看看，这样写，作者就有25个了。因为我们处理了作者数据为空的情况。类似的异常数据处理，在爬虫制作的过程中比比皆是，需要根据具体情况具体分析。

拿到数据后，我们要让系统知道我们需要的数据是哪些：
```python
from mySpider.items import BookItem  

      items = []
        for i in range(0, len(names)-1):
        	item = BookItem()
        	item['name'] = names[i]
        	item['url'] = urls[i]
        	item['author'] = auths[i]
        	item['price'] = prices[i]
        	item['photo'] = photos[i]
        	items.append(item)

        return items
```

这有什么用呢？可以用来输出和保存数据。整个代码类似于这样：
```python
# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import BookItem


class BooklistSpider(scrapy.Spider):
    name = 'booklist'
    allowed_domains = ['xhsd.cn']
    start_urls = ['https://www.xhsd.cn/lb.jsp?pid=0401010000']

    def parse(self, response):
        #filename = "booklist.html"
        #open(filename, 'w').write(response.body.decode('utf-8'))
        names = response.xpath('//div[@class="tab_box5"]/table/tr/td/div/a/@title').extract()
        print(len(names))
        photos = response.xpath('//div[@class="tab_box5"]/table/tr/td/div/a/img/@src').extract()
        print(len(photos))
        urls = response.xpath('//div[@class="tab_box5"]/table/tr/td/div/a/@href').extract()
        print(len(urls))
        prices = response.xpath('//td[@class="gray14"]/span[@class="red14"]/text()').extract()
        print(len(prices))
        

        authors = response.xpath('//div[@class="gray12"]')
        auths = []
        for author in authors:
        	auth = author.xpath('text()').extract()
        	if len(auth) == 1:
        		auths.append(auth[0])
        	else :
        		auths.append(' ')
        print(len(auths))

        items = []
        for i in range(0, len(names)-1):
        	item = BookItem()
        	item['name'] = names[i]
        	item['url'] = urls[i]
        	item['author'] = auths[i]
        	item['price'] = prices[i]
        	item['photo'] = photos[i]
        	items.append(item)

        return items
```

## 保存数据
大家是否还记得我们上节课提到的CSV格式？非常棒的是，scrapy就支持csv。
只需要简单的执行命令就可以将爬虫的结果输出成CSV：
```python
scrapy crawl booklist -o booklist.csv
```
大家可以用excel打开csv文件看看数据是否正确了。

## 总结
今天的内容有些难度。主要是关于XPATH，即使对专业程序员，也并不总能写正确XPATH。大家在学习今天的内容写XPATH时，一个好办法是从最简单的开始一步步调试。例如首先看看：
```python
response.xpath('//div[@class="tab_box5"]')
```
看看获取的数据是什么样的，然后再看看：
```python
response.xpath('//div[@class="tab_box5"]/table/tr/td')
```
类似这样逐级深入，总能慢慢的发现接近目标了。
至于另外两个xpath:
```python
response.xpath('//div[@class="gray12"]') # 作者
response.xpath('//td[@class="gray14"]/span[@class="red14"]/text()')
```
是相对容易的特征。

## 作业
1. 大家尝试自己安装scrapy并创建一个scrapy工程，按照老师的演示，自己走一遍，看看遇到了哪些问题；
2. 在完成第一个任务的基础上，结合前几节课所学的内容，尝试获取更多页面的数据（例如前十页）。

[1]:	https://scrapy.org/
[2]:	https://www.xhsd.cn/lb.jsp?pid=0401010000
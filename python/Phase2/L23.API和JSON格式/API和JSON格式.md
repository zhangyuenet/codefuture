# 数据格式：JSON和CSV

## 教学目标
1. 了解API，复习HTTP GET；
2. 学习JSON数据格式；
3. 复习dict；

## API和HTTP GET
不同于爬虫获取数据记录，我们这节课将使用网络API来获得病毒数据。首先大家需要学习一个在编程领域非常关键的概念：API。
```python
 API ： Application Programming Interface 应用程序接口
```
API实际上是软件系统不同组成部分衔接的约定。一般来说，这个约定至少应该包含：
- 从哪里获取数据；
- 获取数据的命令是什么样的；
- 返回的数据结果格式说明；
所以当你听说某个数据开放了API后，你就可以无需使用爬虫去从网页里面抓取了。因为现在有大量的科学家和研究机构要使用各国的病毒发病数据进行研究。因此，互联网也出现了病毒发病数据的API。
我们今天首先不看代码，先看看一个开放出来的API是什么样子的：
中文版： [https://lab.isaaclin.cn/nCoV/zh][1]
英文版： [https://lab.isaaclin.cn/nCoV/en][2]

**需要特别说明：在当前时间（2020年3月18日），这套API被大量研究机构引用，因此他的API访问并不稳定。因此老师在授课时，可以选择API方式获取数据，也可以选择数据仓库获取CSV/JSON文件的方式。**

大家看第一个接口的定义：
首先告诉了大家获取数据的链接：/nCoV/api/overall
那么结合网站，获得完整的访问地址是：`lab.isaaclin.cn/nCoV/api/overall `
先看返回数据，大家通过读取列表，应该能够看到数据还是相当完善的。
【如果API访问数据失败】可以查看 [https://github.com/BlankerL/DXY-COVID-19-Data/blob/master/json/DXYArea.json][3]

现在我们回到API定义页面，我们来看看有两个地方应该是大家不懂的：
1. 请求方式GET；
2. 变量名；
这两个地方应该已经让大家糊涂了。什么是请求方式？变量名听上去和函数的变量名（参数）相像，但是如何传递这个变量名？
这里要唤醒大家的记忆，大家回忆一下我们很久以前学过的一段代码：
```python
# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('news.baidu.com', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: news.baidu.com\r\nConnection: close\r\n\r\n')
# 接收数据:
。。。。。。

```

这段代码，显然是从百度新闻网站上获取数据（他的作用，就相当于我们在浏览器地址栏中输入news.baidu.com并按下回车）。
大家仔细看这一句：
```python
s.send(b'GET / HTTP/1.1\r\nHost: news.baidu.com\r\nConnection: close\r\n\r\n')
```

大家看到**GET**了。在客户机和服务器之间进行请求-响应时，两种最常被用到的方法是：GET 和 POST。
- **GET** - 从指定的资源请求数据；
- **POST** - 向指定的资源提交要被处理的数据。
因为我们是从网站上获取数据，因此我们用GET，以后我们学习向网站提交数据时，就需要用POST，比如在网站上填写了一份调查问卷，或者上传了自己的照片，在提交时，就是POST操作。

GET清楚了，那么参数呢？我们先看几个链接：
[https://lab.isaaclin.cn/nCoV/api/overall?latest=1][4]
以及：
[https://lab.isaaclin.cn/nCoV/api/area?latest=1&province=%E5%8A%A0%E6%8B%BF%E5%A4%A7][5]

【如果API访问困难则讲解时忽略参数部分】
大家一下就看明白了，所谓的请求参数，就是链接地址中**问号**后面、用**&**分隔的部分，它的格式是这样的：
```python
完整的访问地址?参数1=value1&参数2=value2&参数3=value3。。。。。。
```

## 获取JSON数据
【如果访问API数据失败，则使用离线数据】
API地址：[https://lab.isaaclin.cn/nCoV/api/overall][6]
数据仓库地址：[https://github.com/BlankerL/DXY-COVID-19-Data/blob/master/json/DXYOverall.json][7]

我们今天要学习一个新的数据格式，也是在网络中非常常见的格式，JSON。
我们先看看JSON的数据格式的样式。
为了快速了解JSON格式，我们先从简单一点的数据入手。先看例子（jsontest.py）：
```python
import json

# 将Python数据结构编码为JSON格式。
dictlist = [{'name':'Tom', 'age': 14}, {'name':'Jerry', 'age':13} ]
jsondata = json.dumps(dictlist, sort_keys=True, indent=4, separators=(',', ': '))
print(jsondata)

# 将JSON格式的数据转换为Python对象
jsonstring = '[{"name":"Tom", "age": 14}, {"name":"Jerry", "age":13} ]'
alist = json.loads(jsonstring)
print(alist)
```

大家注意：
1. Json对象是Python内置对象，无需额外安装即可支持，使用时import即可；
2. dictlist是一个list，其中每个元素是dict。一般的，JSON转换为Python对象也是类似的格式，dict或者list；
3. 代码中的样式，就是惯常情况下，最常用的JSON显示格式。

好了，对JSON有了一点了解后，我们再来看这个文件：
离线文件：DXYOverall.json
```bash
{
    "results": [
        {
            "currentConfirmedCount": 7440,
            "confirmedCount": 81238,
            "suspectedCount": 190,
            "curedCount": 70548,
            "deadCount": 3250,
            "seriousCount": 2314,
            "currentConfirmedIncr": -744,
            "confirmedIncr": 87,
            "suspectedIncr": 35,
            "curedIncr": 823,
            "deadIncr": 8,
            "seriousIncr": -308,
            "generalRemark": "1. 3 月 12 日国家卫健委确诊补订遗漏 12 例确诊病例（非 12 日新增），暂无具体省份信息。 2. 浙江省 12 例外省治愈暂无具体省份信息。",
            "abroadRemark": "",
            "remark1": "易感人群：人群普遍易感。老年人及有基础疾病者感染后病情较重，儿童及婴幼儿也有发病",
            "remark2": "潜伏期：一般为 3～7 天，最长不超过 14 天，潜伏期内可能存在传染性，其中无症状病例传染性非常罕见",
            "remark3": "宿主：野生动物，可能为中华菊头蝠",
            "remark4": "",
            "remark5": "",
            "note1": "病毒：SARS-CoV-2，其导致疾病命名 COVID-19",
            "note2": "传染源：新冠肺炎的患者。无症状感染者也可能成为传染源。",
            "note3": "传播途径：经呼吸道飞沫、接触传播是主要的传播途径。气溶胶传播和消化道等传播途径尚待明确。",
            "updateTime": 1584597416803
        }
    ],
    "success": true
}
```
分析Json数据的关键是观察括号的类型：
```bash
{ } 这是一个dict；
[ ] 这是一个list。 
```
所以，我们知道这个数据的格式是一个dict，包含两个key/value。
其中第一个key=“results”的value是一个list，而这个list只包含了一个dict。大部分数据都存储在这个dict中。

我们现在用代码来读取其中的两个数据：确诊数量（confirmedCount）和日期（updateTime）。（getoverall.py）
```python
import requests
import json

url = 'https://lab.isaaclin.cn/nCoV/api/overall'
data = requests.get(url).text
alist = json.loads(data) #a dict
results = alist["results"] #a list
result = results[0] # a dict

print("总确诊数：%s, 日期：%s" % (result["confirmedCount"], result["updateTime"] ))
```

如果API访问正常的话应该可以正常运行。但是，日期看上去是个很长的数字：
```python
 "updateTime": 1584597416803
```

这里要和大家提一下，在各种编程语言中，都支持一种叫做UNIX时间的格式。是UNIX或类UNIX系统使用的时间表示方式：从UTC1970年1月1日0时0分0秒起至现在的总秒数（不考虑闰秒）。 
在多数Unix系统上Unix时间可以透过`date +%s `指令来检查当前的unix时间。
UNIX时间可以转化为我们可以识别的时间。不过我们在看到这种类型的时间表示时，首先要区分它是10位的还是13位的。Python系统中可以直接处理10位的，例如：
```python
>>> import time
>>> time.time()
1584632737.5591328
>>> print(int(time.time()))
1584632762
```
大家应该能猜到了，要转换13位的格式，只需要吧小数点后面的数字“挪用”几位就可以了：
```python
>>> print(int(time.time() * 1000))
1584632974689
```
反过来也容易：
```python
>>> strtime = '1584632762'
>>> strtime = '1584632762'
>>> timedata = time.localtime(int(strtime))
>>> dt = time.strftime("%Y-%m-%d %H:%M:%S", timedata)
>>> print(dt)
2020-03-19 23:46:02


>>> strtime2 = '1584633007875'
>>> timedata2 = time.localtime(int(strtime2) / 1000)
>>> dt = time.strftime("%Y-%m-%d %H:%M:%S", timedata)
>>> print(dt)
2020-03-19 23:46:02
```

所以回到我们的代码，只需要做一下处理即可拿到可识别的时间：
```python
localtime = time.localtime(result["updateTime"] / 1000)
dt = time.strftime("%Y-%m-%d",localtime)

print("总确诊数：%s, 日期：%s" % (result["confirmedCount"], dt))
```

【如果访问API失败，则演示getoverallfromfile.py】

我们再来看另一个API：
[https://lab.isaaclin.cn/nCoV/api/area?latest=1][8]
通过这个地址获得的数据可以获得全球各国最新的数据。我们再练一次，通过全球数据拿到国家名称和对应的发现病例数(getarea.py)：
```python
import requests
import json
import time

url = 'https://lab.isaaclin.cn/nCoV/api/area?latest=1'
data = requests.get(url).text

world = {}

alist = json.loads(data) #a dict
results = alist["results"] #a list
print(len(results))
for result in results:
    world[result["countryName"]] = result["confirmedCount"]
print(world)
```

【如果访问API失败，则演示getareafromfile.py】

到这里，我们显示出来的数据看上去并不方便，因为它没有被排序。我们希望根据案例数被排序。

## 作业
今天的作业就是大家来改造这个程序，我们输出的数据能够按照案例数从多到少排序。（参考getarea.py或getareafromfile.py）
【提示】dict的Value排序，基本思路是：
1. 将Key/Value放入一个list： `[ [value1, key1], [value2, key2], [value3, key3], ... ]`
2. 对list排序；
3. 将list中排好序的数据放回到dict。

## 补充内容
引导学生下载DXYArea-TimeSeries.json文件，做更复杂的数据分析。参见并演示getcountry.py











[1]:	https://lab.isaaclin.cn/nCoV/zh
[2]:	https://lab.isaaclin.cn/nCoV/en
[3]:	https://github.com/BlankerL/DXY-COVID-19-Data/blob/master/json/DXYArea.json
[4]:	https://lab.isaaclin.cn/nCoV/api/overall?latest=1
[5]:	https://lab.isaaclin.cn/nCoV/api/area?latest=1&province=%E5%8A%A0%E6%8B%BF%E5%A4%A7
[6]:	https://lab.isaaclin.cn/nCoV/api/overall
[7]:	https://github.com/BlankerL/DXY-COVID-19-Data/blob/master/json/DXYOverall.json
[8]:	https://lab.isaaclin.cn/nCoV/api/area?latest=1
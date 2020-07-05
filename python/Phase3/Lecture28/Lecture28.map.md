# Lecture28 地图

## 课程导入
我们在前面的几节课中，主要学习了两部分内容：
1. 处理数据：Pandas是我们过滤和筛选数据的利器；
2. 绘制图形：从简单的柱状图到动画，我们大致了解了绘制的原理；

今天开始，我们将接触另一种类型的图形，很有用，也很好玩。首先看效果：map\_beijing.html。
一副完整的世界地图，鼠标滑动到某些国家和地区，可以显示出对应的信息。

大家猜想一下，需要多少行代码来实现这个效果？
今天我们来给大家讲如何绘制地图。教学的目标如下：

## 教学目标
- 可以用自行编造的数据填充中国地图、中国某区域地图、世界地图；

## 安装组件
和任何新项目一样，我们首先考察依赖的组件。我们选用pyecharts。关于这个项目的介绍在这里：
[ https://pyecharts.herokuapp.com/ ]()
在这里要简单介绍一下。
Echarts是中国公司百度的一个数据可视化项目库，这个库给所有人公开使用，不过Echarts用的是JavaScript，以后我们有机会可以学习这个语言。为了让Python使用者可以用上这个项目库，三位开发者开发了PyEcharts库，这个库的作用就是使用Python代码生成Echarts图表。
PyEcharts库主要有两个版本，v0.5.x可以支持老版本的python（2.7），但是已经不再维护了。新版本v1只支持Python3.6以上。老师电脑上安装的是截止写作时最新的版本1.8.1。本教程也以该版本为准。
之所以要讲一下版本，是因为目前在网上能够搜到的很多关于Python绘制地图的教程，还有很多是基于PyEcharts v.0.5的，而因为版本不兼容，这些教程中的代码，在v1.0以上的版本中无法正常运行。这个是同学们需要了解的。

下面我们来安装组件：
```bash
pip3 install pyecharts
# 中国大陆学生可以用下面的方式安装：
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts
```

【特别提示】如果你在网上看到了一些关于地图的好的例子希望学习或者使用，但他们如果基于旧版本的PyEcharts，你可以卸载我们刚才安装的最新版本，转而安装一个老版本以运行你需要的程序：
```bash
# 首先卸载新版本pyecharts
pip uninstall pyecharts
# 安装0.5.11版本
pip install pyecharts==0.5.11
```

为了缩减项目本身的体积以及维持 pyecharts 项目的轻量化运行，pyecharts 将不再自带地图 js 文件。如用户需要用到地图图表（Geo、Map），可自行安装对应的地图文件包。否则在用到这两个包的时候，无法完整的显示地图效果。因此，要使用地图功能，我们还需要下载下面三个包：
```bash
pip3 install echarts-countries-pypkg 
pip3 install echarts-china-provinces-pypkg
pip3 install echarts-china-cities-pypkg
```
望文生义，我们应该能猜出这三个安装包分别包含的是那些地图。

## 中国地图
首先大家来看中国地图：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Map

provinces = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
values = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]

c = (
    Map()
    .add("学生地域分布", [list(z) for z in zip(provinces, values)], "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="全国分布图"))
    .render("map_china.html")
)
```
执行程序后，目录下应该出现了一个文件map_china.html。用浏览器打开，看看效果。
在代码中列出的省份和数字，应该已经对应在地图上了。怎么样？出乎意料的简单吧？

## 链式操作

我们简单分析一下代码。
首先，provinces和values保存了要展示的数据。
其次代码的主体的部分是一个称之为c的变量。这个变量使用一个叫做Map()函数创建。Map()函数创建对象并没有像我们惯常看到的那样在括号中提供参数的方式。而是采用了一种“链式调用”。这种调用形式需要作为初学者的同学们了解，能读懂即可，但不要求会写。

传统的函数在调用时是这样写的：
```python
Foo(title, options, output, data, others)
```
使用链式调用可以写成类似的方式：
```python
a = Foo().settitle('aa').setoptions('bbb').setoutput('ccc').setdata('ddd')
```
这样写和之前比有什么好处呢？这时候，括号就该起作用了：
```python
a = (Foo()
    .settitle('aa')
    .setoptions('bbb')
    .setoutput('ccc')
    .setdata('ddd'))
```
大家看，这样的写法是不是看上去每行的代码变短了，结构也更加清晰？
所以简单总结一下大家了解：一些功能强大的函数，往往需要很复杂的参数（比如咱们正在用的地图）,如果用传统的参数式写法，会导致代码太长，可读性差，并且容易出错。因此，使用链式操作配合括号的使用，可以让代码的可读性变得更强。当然，链式操作的好处不止于此。在本节课的最后，附带了一个链式操作的实现方式，有兴趣的同学可以揣摩了解一下。

回到地图上来，Map()的链式操作，用三行代码提供了参数。我们逐一讲解：

## ZIP数据
第一行：
```python
.add("学生地域分布", [list(z) for z in zip(provinces, values)], "china")
```
包含了三个参数：
- 标题；
- 数据包；
- 地图类型；

地图类型是china，我们大胆的猜测一下，world应该就是世界地图，等会我们试试看。
这里面大家又看到了似曾相识的写法：
```python
[list(z) for z in zip(provinces, values)]
```
在绘制动画时，我们遇到过zip，当时简单介绍过：zip可以将两个list打包组合成一个。今天我们稍微详细点介绍一下它的用法。

```python
provinces = ["福建", "山东", "北京"]
values = [155, 10, 66]
test = zip(provinces, values)
print(test)  #<zip object at 0x108a81d20>
list(test) #[('福建', 155), ('山东', 10), ('北京', 66)]
```
可以看到zip的主要功能就是将数组组合在一起。大家在看一个实验就清楚了，我们改造上面的代码：
```python
data = [("福建",155),("山东",10),("北京",66)]
c = (
    Map()
    .add("学生地域分布", data, "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="全国分布图"))
    .render("map_china.html")
)
```
大家可以看到，不用zip，直接用data表述数据，效果是一样的。
所以，如果以后同学们制作图表时，如果数据量不大，也完全可以自己写成data的格式用，这样就无需zip。但是大多数情况，当数据量比较大时，数据会存在不同的列中，这时候，用zip把两列数据组合起来就很有用了。

回到地图。另两个参数比较简单：
```python
.set_global_opts(title_opts=opts.TitleOpts(title="全国分布图"))
.render("map_china.html")
```

一个指定了地图的title，另一个指定了输出的文件名。
最后，我们看看Map()的返回值，也就是c的值是什么。打印一下能看到，它返回了图像的完整路径。

## 世界地图
好，我们刚才猜测到了，如果更改地图类型，也许我们就可以拿到世界地图了。很正确，的确如此，我们看代码：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Map

countries = ["Canada", "USA", "China", "India", "Japan", "Spain", "Russia", "Thailand"]
values = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]

c = (
    Map()
    .add("全球学生地域分布", [list(z) for z in zip(countries, values)], "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
    .render("map_world.html")
)
```
这里面增加了几个对大家有用的参数：
```python
# 这个开关可以控制是否在地图上显示国家名称，当采用世界地图时，为了不要太乱，最好还是加上is_show=False关闭显示名称。
.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# 这个开关可以在地图旁边显示一个数据筛选条，大家尝试拖动调整一下筛选条的值，就能看到它实际上是一个过滤器，方便的将某一数据范围内的数据显示在地图上。
visualmap_opts=opts.VisualMapOpts(max_=200),
```
让我们观察一下生成的地图，大家有没有发现问题？

我们在列表中有美国“USA”，可是在地图中没有显示，原来，我们把美国的名称写错了。但是正确的名称是什么呢？很简单，当大家不知道地图上具体的行政区域是什么名字时，只需要先创建一个地图，然后用鼠标在需要的区域上悬浮，自然能看到名称了，原来，美国在地图中的名称是“United States”，大家注意，地图组件要求大家大小写正确。

好了，今天的内容已经差不多了，最后，中国大陆学生当然经常还会用到和自己家乡相关的地图。这个也很简单，我们直接看看北京地图的代码：

```python
provinces = ["东城区", "西城区", "海淀区", "朝阳区", "大兴区", "房山区", "昌平区", "延庆区", "顺义区"]
values = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
 
c = (
    Map()
    .add("学生地域分布", [list(z) for z in zip(provinces, values)], "北京")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="北京地区"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
    .render("map_beijing.html")
)
```

# 作业

编造一点数据，创建一个你的家乡的地图把！


# 附录： 构造一个链式操作

有兴趣的同学，可以直接运行linkoper.py，看看两种写法有什么差异和相同之处。大致就明白链式操作了。除了让代码变得简洁，链式操作还有个很重要的好处就是灵活，无需实现设定好各种参数类型，用户可以根据实际情况传入各种参数来执行代码。这是一种非常灵活高效的编程方式。


# HTML
## 课程引入
我们在前面的课程中，尝试着在服务器和客户端之间传递了各式各样的消息。但是在实际生活中，我们浏览网站时，会发现数据的种类的复杂度绝对是非常高的。因此用我们前几节课设计的简单协议的方式，显然是无法用来传递复杂信息的。在现实的编程世界中，有很多种称之为“标记语言”的语言，来完成复杂结构信息的传递，其中最有名的就是HTML（文本标记语言，Hypertext Markup Language），是用于描述网页文档的一种标记语言。以后我们还会学到其它标记语言。

## 标记语言
【以下内容来自于wikipedia】
标记语言（也称置标语言、标记语言、标志语言、标识语言、markup language）是一种将文本（Text）以及文本相关的其他信息结合起来，展现出关于文档结构和数据处理细节的计算机文字编码。与文本相关的其他信息（包括例如文本的结构和表示信息等）与原来的文本结合在一起，但是使用标记（markup）进行标识。当今广泛使用的标记语言是超文本置标语言（HyperText Markup Language，HTML）和可扩展置标语言（eXtensible Markup Language，XML）。标记语言广泛应用于网页和网络应用程序。标记最早用于出版业，是作者、编辑以及出版商之间用于描述出版作品的排版格式所使用的。
## HTML基本语法
一个网页对应于一个HTML文件，HTML文件以.htm或.html为扩展名。可以使用任何文本编辑器生成HTML，我们前面讲到的各种代码编辑器都可以编辑HTML。 超文本标记语言标准的HTML文件都具有一个基本的整体结构，即HTML文件的开头与结尾标志和HTML的头部与实体2大部分。有3个双标记符用于页面整体结构的确认。

## 学习HTML的目的
在进入详细学习之前，请大家务必了解我们这节课安排学习HTML的目的：
1. 能看懂未来要使用的HTML文件，懂得在众多标记中间寻找有用的信息；
2. 理解HTML最常用的标记和格式的意义，能够编辑一些简单的HTML格式。
有了这两点，我们第一可以利用既有HTML文件，第二可以用HTML标记输出一些格式文本。
### HTML标签
我们先看最基础的HTML代码：
```html
<html>
	<head>
		<title>Page Name</title>
	</head>
	<body>
		Hello HTML!
	</body>
</html>
```
在这里首先要强调一下，HTML中是不需要缩紧的，这一点和Python不同。大家在未来看到很多地方看到缩进格式，只是为了阅读的方便。事实上，HTML是通过标记符：`<tag></tag>`来区分内容的，就算吧所有的内容都写成一行也是没关系的。
将上面的内容可以直接存为一个.html文件，文件名随意。在任何系统中都可以用浏览器直接打开它。大家注意观察一下现实效果中，“Page Name”显示在了什么地方。

我们自然希望显示的多样性，因此我们先看看怎么让显示的花样多一些：
```html
<p>This is a paragraph</p>
<br> (line break)
<hr> (horizontal rule)
<pre>This text is preformatted</pre>
<em>This text is emphasized</em>
<strong>This text is strong</strong>
<code>This is some computer code</code>
<b>This text is bold</b>
<i>This text is italic</i>
```
大家看看效果。顺便说一句，HTML其实学起来并不复杂，试着写一下，然后不断的看效果就对了。
下面这些是常用的链接样式：
```html
<a href="http://www.example.com/">This is a Link</a>
<a href="http://www.example.com/"><img src="URL"
alt="Alternate Text"></a>
<a href="mailto:webmaster@example.com">Send e-mail</a>
A named anchor:
<a name="tips">Useful Tips Section</a>
<a href="#tips">Jump to the Useful Tips Section</a>
```
在制作网页的时候，anchor是个很有用的技巧，大家值得揣摩一下。


各种个样的列表：
无序列表：
```html
<ul>
	<li>First item</li>
	<li>Next item</li>
</ul>
```

有序列表：
```html
<ol>
	<li>First item</li>
	<li>Next item</li>
</ol>
```

相对比较麻烦的是表格：
```html
<table border="1">
	<tr>
  		<th>header1</th>
  		<th>header2</th>
	</tr>
	<tr>
  		<td>first line text</td>
  		<td>first line text</td>
	</tr>
	<tr>
  		<td>second line text</td>
  		<td>second line text</td>
	</tr>

</table>
```

需要强调的是：
- 所有的标记不区分大小写，但是国际标准已经推荐使用小写，并且会在未来强制执行；
- 注意有些标记必须配对（例如`<td></td>`），有些不需要（例如`<br>`）但是对于不需要配对的符号，也推荐这样的写法：`<br/>`；

【学生活动】我们来做一个简单的练习，大家用HTML编辑一个包含一周课程的课程表。
【教师根据学生的反馈，只要能写出HTML元素并在浏览器中浏览即可，后面作业还会继续这部分，所以不用花费太长时间，3-5分钟练练手即可。】

## HTML 样式
如果大家做得还算顺利，我们已经可以简单的使用标签了。但是这显然不够，因为“太丑”。我们看到的网页，大部分是包含“样式（Style）”的。在HTML中，样式统一用style属性来表示。

在这里补充一下属性的概念，不同的标签可能包含不同的属性。例如：
```html
<a href="http://www.example.com/">This is a Link</a>
```
href就是标签`<a></a>`的重要属性：链接的地址。
属性写在标签名称加一个空格后。
有一些属性是所有标签都有的，比如id，再比如现在要讲的Style。
样式的基本用法如下：
```html
<p style="background-color:red">This is a paragraph</p>
```

大家可以试试刚才讲的标签，都可以加这样的样式。另外，大家望文生义，猜猜看，是否可以将red换成其它，比如green？

其它重要的样式还包括：
```html
<p style="background-color:blue;font-family:arial;color:red;font-size:20px;">This is a paragraph</p>

```

【学生练习】我们学习了一些简单的样式，如果需要更多的怎么办？上网查查是最有效的办法。例如，大家可以尝试自己搜索一下如何让文字居中对齐？
应该如何设置关键字，是能够实现快速搜索的最重要的技巧。多搜搜看，你会发现自己找答案的能力越来越强。
【教师活动】引导学生设置关键字：html, style，align或者中文“对齐”。
从而找到样式text-align。

### HTML的更多知识
HTML 更多的标签和样式，老师不建议特别花时间去学。用到的时候去检索是最好的办法。
我们只需要有一个感性的认识和概念，就可以帮助我们完成一些工作。例如下面这个例子：
【教师活动】老师打开如下链接：
[https://maoyan.com/films?showType=3][1]
打开源代码，学生能在源代码中找到《速度与激情8》的评分是多少么？
【注意是9.3而不是9，因为整数部分和小数部分分开显示了】
```html
<i class="integer">9.</i><i class="fraction">3</i>
```

如果完全没有HTML的基础，可能看到一大堆符号就已经乱套了，但是学过一点之后，我们就明白，在尖括号中的部分，有标签，有属性，有样式。有些东西虽然不了解是干什么的，但是我们可以忽略这些东西直接找到所需要的信息。

之所以拿这个页面举例子，是因为我们后面的爬虫就要在这个页面上工作了。

大家看看这个页面的源代码中，有多少标签、属性和样式是自己没见过的？
样式相当复杂，标签可以通过如下的资料库查询：
[https://www.w3school.com.cn/tags/index.asp][2]
对应的英文版在这里：
[https://www.w3schools.com/tags/default.asp][3]
遇到不了解的标签，去这里看看，然后自己试试。很快就能掌握。

### 更多补充
因为本课程是Python课程，在这里讲到HTML，主要是因为后面我们的网络程序要操作HTML文件，甚至要用HTML生成一些带有简单格式的文件输出。所以用一节课的时间简单介绍。给大家留下印象。有兴趣的同学可以业余时间尝试一下，遇到问题可以找老师或者助教。
如果将来大家有机会学习JavaScript，我们再来仔细的讨论HTML，越是看上去简单的东西，用起来越是千变万化。
在这里补充两点：
1. 要习惯性的用浏览器查看网页的源代码，chrome或者IE都可以方便的查看源码，大家现在就试试看；
2. 阅读HTML代码，经常需要“望文生义”，字面上的意思，往往就是它的真实含义（例如上面例子中的“integer/fraction”）。
3. HTML最简单也最重要的学习方式，就是自己试试看；
4. 关于HTML5，很多同学可能听说过HTML5，现在很多完全不懂编程的人都会提到H5。实际上这里面可能有一些偏差。HTML5是对过去HTML的一个补充和增强，例如，传统的HTML对多媒体的处理是不足的，只能依靠Flash这样的第三方工具来解决动画播放的问题，但是HTML5中，多媒体相关支持强大了很多，这直接导致flash动画基本走向消亡。类似的变化，体现在HTML5的标准扩充中，在上面提到的资料库中，有清楚的表明那些标记是HTML5新增的，大家有兴趣可以看看。另一方面，广义的HTML5，也就是大家嘴上最常说的H5，实际上指的是包括HTML、CSS和JavaScript在内的一套技术组合。动态网页技术的发展，暂时不是我们Python课的重点，因此这块我们暂时不用涉及。

## 作业
想办法不断的完善自己的课程表，看谁用HTML做的课程表最酷。
不会的部分，优先自己搜索查阅资料，如果还无法解决，可以找老师或者助教。

[1]:	https://maoyan.com/films?showType=3
[2]:	https://www.w3school.com.cn/tags/index.asp
[3]:	https://www.w3schools.com/tags/default.asp
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Map

provinces = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
values = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]

data = [("福建",155),("山东",10),("北京",66)]
 
c = (
    Map()
    .add("学生地域分布", [list(z) for z in zip(provinces, values)], "china")
    #.add("学生地域分布", data, "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="全国分布图"))
    .render("map_china.html")
)

print(c)
print(type(c))


#d = Map().add("学生地域分布", [list(z) for z in zip(provinces, values)], "china").set_global_opts(title_opts=opts.TitleOpts(title="全国分布图")).render("map_china2.html")
#print(d)
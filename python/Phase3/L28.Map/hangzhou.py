#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Map

provinces = ["上城区", "下城区", "江干区", "未知区", "萧山区", "余杭区","西湖区","拱墅区"]
values = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
 
c = (
    Map()
    .add("学生地域分布", [list(z) for z in zip(provinces, values)], "杭州")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="杭州地区"),
        visualmap_opts=opts.VisualMapOpts(max_=160),
    )
    .render("map_hangzhou.html")
)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Map

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
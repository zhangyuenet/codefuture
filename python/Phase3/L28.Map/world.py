#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Map

countries = ["Canada", "United States", "China", "India", "Japan", "Spain", "Russia", "Thailand"]
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
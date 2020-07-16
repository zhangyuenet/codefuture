#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

provinces = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
values = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]

c = (
    Geo()
    .add_schema(maptype="china")
    .add(
        "geo",
        [list(z) for z in zip(provinces,values)],
        type_=ChartType.HEATMAP,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo-HeatMap"),
    )
    .render("geo_heatmap.html")
)
